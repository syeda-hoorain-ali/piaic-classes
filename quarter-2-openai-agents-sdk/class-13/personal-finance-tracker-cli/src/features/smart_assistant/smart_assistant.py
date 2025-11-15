import csv
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
import questionary
import os

console = Console()

TRANSACTIONS_FILE = "finance_tracker/database/transactions.csv"
BUDGET_FILE = "finance_tracker/database/budgets.txt"

# Budget Categories (from GEMINI.md)
BUDGET_CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]
INCOME_CATEGORIES = ["Salary", "Freelance", "Business", "Investment", "Gift", "Other"]

def _load_transactions():
    transactions = []
    try:
        with open(TRANSACTIONS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        pass
    return transactions

def _get_budgets():
    budgets = {}
    if not os.path.exists(BUDGET_FILE):
        return budgets
    with open(BUDGET_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                category, amount_paisa = row
                budgets[category] = int(amount_paisa)
    return budgets

def _get_current_month_transactions(transactions):
    current_month_str = datetime.now().strftime("%Y-%m")
    return [t for t in transactions if t["Date"].startswith(current_month_str)]

def _calculate_monthly_spending_by_category(transactions):
    spending_by_category = {category: 0 for category in BUDGET_CATEGORIES}
    for t in transactions:
        if t["Type"] == "Expense" and t["Category"] in spending_by_category:
            spending_by_category[t["Category"]] += int(t["Amount"])
    return spending_by_category

def _calculate_total_income_expenses(transactions):
    total_income = 0
    total_expenses = 0
    for t in transactions:
        amount = int(t["Amount"])
        if t["Type"] == "Income":
            total_income += amount
        else:
            total_expenses += amount
    return total_income, total_expenses

def daily_financial_check():
    console.print(Panel("[bold blue]📊 Daily Financial Check[/bold blue]", expand=False))
    transactions = _load_transactions()
    current_month_transactions = _get_current_month_transactions(transactions)

    today = datetime.now().date()
    today_str = today.strftime("%Y-%m-%d")

    today_spending = sum(int(t["Amount"]) for t in transactions if t["Date"] == today_str and t["Type"] == "Expense")

    budgets = _get_budgets()
    total_monthly_budget = sum(budgets.values())

    # Calculate remaining days in month
    _, num_days_in_month = (today.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    remaining_days = num_days_in_month - today.day + 1

    # Calculate average daily spending for the month so far
    total_expenses_this_month = sum(int(t["Amount"]) for t in current_month_transactions if t["Type"] == "Expense")
    days_passed = today.day
    average_daily_spending_so_far = total_expenses_this_month / days_passed if days_passed > 0 else 0

    # Estimate remaining daily budget based on total monthly budget and spending so far
    estimated_remaining_budget = total_monthly_budget - total_expenses_this_month
    remaining_daily_budget = estimated_remaining_budget / remaining_days if remaining_days > 0 else 0

    console.print(f"Date: [bold]{today_str}[/bold]")
    console.print(f"Today's Spending: [bold red]Rs {today_spending / 100:.2f}[/bold red]")

    if remaining_daily_budget >= 0:
        console.print(f"Estimated Remaining Daily Budget: [bold green]Rs {remaining_daily_budget / 100:.2f}[/bold green] ✅")
    else:
        console.print(f"Estimated Remaining Daily Budget: [bold red]Rs {remaining_daily_budget / 100:.2f}[/bold red] ⚠️")

    console.print("\n[bold yellow]⚠️ Alerts:[/bold yellow]")
    spending_by_category = _calculate_monthly_spending_by_category(current_month_transactions)

    has_alerts = False
    for category, spent_amount in spending_by_category.items():
        budget_amount = budgets.get(category, 0)
        if budget_amount > 0:
            utilization_percent = (spent_amount / budget_amount) * 100
            if utilization_percent >= 80:
                console.print(f"  • [bold yellow]{category}[/bold yellow] category at [bold]{utilization_percent:.0f}%[/bold] of budget (Rs {spent_amount / 100:.2f} / Rs {budget_amount / 100:.2f})")
                has_alerts = True

    # Large transaction alert (e.g., >20% of average daily spending)
    if average_daily_spending_so_far > 0:
        large_transaction_threshold = average_daily_spending_so_far * 2 # 200% of average daily spending
        for t in transactions:
            if t["Date"] == today_str and t["Type"] == "Expense" and int(t["Amount"]) > large_transaction_threshold:
                console.print(f"  • Large transaction detected: [bold red]Rs {int(t['Amount']) / 100:.2f}[/bold red] ({t['Category']}: {t['Description']})")
                has_alerts = True

    if not has_alerts:
        console.print("  No significant alerts today. Keep up the good work!")

    console.print("\n[bold green]💡 Tip:[/bold green]")
    if remaining_daily_budget >= 0:
        console.print("  You're on track! Consider moving some funds to savings if you have extra.")
    else:
        console.print("  You're slightly over budget today. Review your recent expenses and try to cut back where possible.")

def smart_recommendations():
    console.print(Panel("[bold blue]🧠 Smart Recommendations[/bold blue]", expand=False))
    transactions = _load_transactions()
    current_month_transactions = _get_current_month_transactions(transactions)

    total_income, total_expenses = _calculate_total_income_expenses(current_month_transactions)
    spending_by_category = _calculate_monthly_spending_by_category(current_month_transactions)
    budgets = _get_budgets()

    console.print("[bold underline]Spending Analysis:[/bold underline]")
    if total_expenses > 0:
        sorted_spending = sorted(spending_by_category.items(), key=lambda item: item[1], reverse=True)
        console.print("Top 3 spending categories this month:")
        for i, (category, amount) in enumerate(sorted_spending[:3]):
            if amount > 0:
                console.print(f"  {i+1}. [bold]{category}[/bold]: Rs {amount / 100:.2f}")

        console.print("\n[bold]Recommendations to reduce spending:[/bold]")
        for category, spent_amount in sorted_spending:
            if spent_amount > 0:
                budget_amount = budgets.get(category, 0)
                if budget_amount > 0 and spent_amount > budget_amount:
                    console.print(f"  • [bold red]Reduce {category}[/bold red] spending. You are Rs {(spent_amount - budget_amount) / 100:.2f} over budget.")
                elif spent_amount > (total_expenses * 0.2): # If a category is more than 20% of total expenses
                    console.print(f"  • Consider cutting back on [bold]{category}[/bold] expenses, which are a significant portion of your spending.")
    else:
        console.print("No expenses recorded this month yet.")

    console.print("\n[bold underline]Savings Opportunities:[/bold underline]")
    if total_income > 0:
        savings = total_income - total_expenses
        savings_rate = (savings / total_income) * 100 if total_income > 0 else 0
        console.print(f"Current Savings Rate: [bold]{savings_rate:.2f}%[/bold]")

        if savings_rate < 10:
            console.print("  • Your savings rate is low. Aim for at least 10-15% of your income.")
            console.print("  • Try implementing the [bold]50/30/20 rule[/bold]: 50% needs, 30% wants, 20% savings/debt.")
        elif savings_rate >= 10 and savings_rate < 20:
            console.print("  • Good job on saving! Consider increasing your savings goal to build wealth faster.")
        else:
            console.print("  • Excellent savings rate! Keep up the great work and explore investment opportunities.")
    else:
        console.print("No income recorded this month yet to calculate savings.")

    console.print("\n[bold underline]Budget Adherence:[/bold underline]")
    if budgets:
        over_budget_categories = [cat for cat, budget in budgets.items() if spending_by_category.get(cat, 0) > budget]
        if over_budget_categories:
            console.print("[bold red]⚠️ You are over budget in the following categories:[/bold red]")
            for cat in over_budget_categories:
                console.print(f"  - {cat}")
            console.print("  • Review your budgets and adjust spending or reallocate funds.")
        else:
            console.print("[bold green]✅ You are within budget for all categories this month. Great job![/bold green]")
    else:
        console.print("No budgets set. [bold yellow]Consider setting budgets for better financial control.[/bold yellow]")

def spending_alerts_system():
    console.print(Panel("[bold red]🚨 Spending Alerts System[/bold red]", expand=False))
    transactions = _load_transactions()
    current_month_transactions = _get_current_month_transactions(transactions)

    today = datetime.now().date()
    today_str = today.strftime("%Y-%m-%d")

    total_income_this_month, _ = _calculate_total_income_expenses(current_month_transactions)
    spending_by_category = _calculate_monthly_spending_by_category(current_month_transactions)
    budgets = _get_budgets()

    has_alerts = False
    console.print("[bold underline]Budget Warnings (>80% Used):[/bold underline]")
    for category, spent_amount in spending_by_category.items():
        budget_amount = budgets.get(category, 0)
        if budget_amount > 0:
            utilization_percent = (spent_amount / budget_amount) * 100
            if 80 <= utilization_percent < 100:
                console.print(f"  • [bold yellow]Warning:[/bold yellow] [bold]{category}[/bold] is at [bold]{utilization_percent:.0f}%[/bold] of budget (Rs {spent_amount / 100:.2f} / Rs {budget_amount / 100:.2f}).")
                has_alerts = True
            elif utilization_percent >= 100:
                console.print(f"  • [bold red]OVER BUDGET:[/bold red] [bold]{category}[/bold] is at [bold]{utilization_percent:.0f}%[/bold] of budget (Rs {spent_amount / 100:.2f} / Rs {budget_amount / 100:.2f}).")
                has_alerts = True
    if not any(80 <= (spending_by_category.get(cat, 0) / budgets.get(cat, 1)) * 100 for cat, budget in budgets.items() if budget > 0):
        console.print("  No budget warnings or overspending detected.")

    console.print("\n[bold underline]Large Transaction Alerts:[/bold underline]")
    if total_income_this_month > 0:
        large_transaction_threshold = total_income_this_month * 0.20 # 20% of monthly income
        large_transactions_today = [
            t for t in transactions
            if t["Date"] == today_str and t["Type"] == "Expense" and int(t["Amount"]) > large_transaction_threshold
        ]
        if large_transactions_today:
            for t in large_transactions_today:
                console.print(f"  • [bold red]Large Expense:[/bold red] Rs {int(t['Amount']) / 100:.2f} on {t['Date']} for {t['Category']} ({t['Description']}).")
                has_alerts = True
        else:
            console.print("  No unusually large transactions today.")
    else:
        console.print("  Cannot check for large transactions without income data.")

    if not has_alerts:
        console.print("\n[bold green]No active spending alerts. Your finances are looking good![/bold green]")

def savings_opportunities():
    console.print(Panel("[bold green]💰 Savings Opportunities[/bold green]", expand=False))
    transactions = _load_transactions()
    current_month_transactions = _get_current_month_transactions(transactions)

    total_income, total_expenses = _calculate_total_income_expenses(current_month_transactions)
    spending_by_category = _calculate_monthly_spending_by_category(current_month_transactions)
    budgets = _get_budgets()

    console.print("[bold underline]Areas to Reduce Spending:[/bold underline]")
    if total_expenses > 0:
        sorted_spending = sorted(spending_by_category.items(), key=lambda item: item[1], reverse=True)

        for category, spent_amount in sorted_spending:
            if spent_amount > 0:
                budget_amount = budgets.get(category, 0)
                if budget_amount > 0 and spent_amount > budget_amount:
                    potential_savings = spent_amount - budget_amount
                    console.print(f"  • [bold]{category}[/bold]: You are [bold red]Rs {potential_savings / 100:.2f}[/bold red] over budget. Consider cutting back here.")
                elif spent_amount > (total_expenses * 0.15): # If a category is more than 15% of total expenses
                    console.print(f"  • [bold]{category}[/bold]: This category accounts for a significant portion of your expenses (Rs {spent_amount / 100:.2f}). Small reductions can lead to big savings.")
        if not sorted_spending:
            console.print("  No expenses recorded this month to identify reduction areas.")
    else:
        console.print("  No expenses recorded this month to identify reduction areas.")

    console.print("\n[bold underline]Estimated Monthly Savings Potential:[/bold underline]")
    if total_income > 0:
        current_savings = total_income - total_expenses
        console.print(f"  Current estimated monthly savings: [bold green]Rs {current_savings / 100:.2f}[/bold green]")

        # Simple estimation: if over budget in any category, potential savings is the amount over budget
        total_over_budget = sum((spent_amount - budgets.get(category, 0)) for category, spent_amount in spending_by_category.items() if budgets.get(category, 0) > 0 and spent_amount > budgets.get(category, 0))

        if total_over_budget > 0:
            console.print(f"  By adhering to your budgets, you could save an additional [bold green]Rs {total_over_budget / 100:.2f}[/bold green] this month.")
            console.print(f"  Total potential savings: [bold green]Rs {(current_savings + total_over_budget) / 100:.2f}[/bold green]")
        else:
            console.print("  You are currently within all your budgets. To save more, consider increasing your income or reducing spending in non-essential categories.")
    else:
        console.print("  Cannot estimate savings potential without income data.")

    console.print("\n[bold underline]Financial Goals Progress (Placeholder):[/bold underline]")
    console.print("  • [bold]Emergency Fund:[/bold] [yellow]Not set[/yellow] - [italic]Recommendation: Aim for 3-6 months of living expenses.[/italic]")
    console.print("  • [bold]Vacation Savings:[/bold] [yellow]Not set[/yellow] - [italic]Recommendation: Set a target and automate transfers.[/italic]")
    console.print("  [italic]You can set and track specific financial goals here in future updates.[/italic]")
