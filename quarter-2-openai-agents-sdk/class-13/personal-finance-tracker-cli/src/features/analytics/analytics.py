import csv
from datetime import datetime, timedelta
from collections import defaultdict
import os
from rich.console import Console
from rich.table import Table
from rich.bar import Bar
from rich.text import Text
import questionary

# Assuming transactions.csv is in the same relative path as transactions.py
TRANSACTIONS_FILE = "finance_tracker/database/transactions.csv"
console = Console()

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

def spending_analysis():
    console.print("[bold blue]Spending Analysis[/bold blue]")
    transactions = _load_transactions()

    if not transactions:
        console.print("No transactions recorded yet for analysis.")
        return

    current_month_expenses = defaultdict(int)
    last_month_expenses = defaultdict(int)
    total_current_month_expense = 0
    total_last_month_expense = 0

    today = datetime.now()
    current_month_start = today.replace(day=1)
    last_month_end = current_month_start - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)

    for t in transactions:
        if t["Type"] == "Expense":
            transaction_date = datetime.strptime(t["Date"], "%Y-%m-%d")
            amount = int(t["Amount"])

            if transaction_date >= current_month_start:
                current_month_expenses[t["Category"]] += amount
                total_current_month_expense += amount
            elif transaction_date >= last_month_start and transaction_date <= last_month_end:
                last_month_expenses[t["Category"]] += amount
                total_last_month_expense += amount

    if total_current_month_expense == 0:
        console.print("No expenses recorded for the current month.")
        return

    # Spending Breakdown by Category (Pie Chart in ASCII)
    console.print("\n[bold underline]Spending by Category (Current Month):[/bold underline]")
    category_percentages = {}
    for category, amount in current_month_expenses.items():
        percentage = (amount / total_current_month_expense) * 100
        category_percentages[category] = percentage

    # Sort categories by percentage for display
    sorted_categories = sorted(category_percentages.items(), key=lambda item: item[1], reverse=True)

    for category, percentage in sorted_categories:
        bar_length = int(percentage / 100 * 20)  # Scale to 20 characters
        bar = "█" * bar_length
        console.print(f"{category:<12} {bar:<20} {percentage:.1f}%")

    # Top 3 Spending Categories
    console.print("\n[bold underline]Top 3 Spending Categories (Current Month):[/bold underline]")
    for i, (category, percentage) in enumerate(sorted_categories[:3]):
        console.print(f"{i+1}. {category} ({percentage:.1f}%)")

    # Average Daily Expense
    days_in_current_month = (today - current_month_start).days + 1
    average_daily_expense = total_current_month_expense / days_in_current_month / 100
    console.print(f"\n[bold underline]Average Daily Expense (Current Month):[/bold underline] Rs {average_daily_expense:.2f}")

    # Comparison with Last Month
    console.print("\n[bold underline]Comparison with Last Month:[/bold underline]")
    console.print(f"Current Month Total Expenses: Rs {total_current_month_expense / 100:.2f}")
    console.print(f"Last Month Total Expenses: Rs {total_last_month_expense / 100:.2f}")

    if total_last_month_expense > 0:
        change = ((total_current_month_expense - total_last_month_expense) / total_last_month_expense) * 100
        if change > 0:
            console.print(f"Spending Change: [bold red]+{change:.1f}%[/bold red] compared to last month.")
        elif change < 0:
            console.print(f"Spending Change: [bold green]{change:.1f}%[/bold green] compared to last month.")
        else:
            console.print("Spending Change: No change compared to last month.")
    else:
        console.print("No expenses recorded last month for comparison.")

    # Spending Trends (up/down) - simple comparison for now
    console.print("\n[bold underline]Spending Trends:[/bold underline]")
    if total_current_month_expense > total_last_month_expense:
        console.print("[bold red]Overall spending is trending UP.[/bold red]")
    elif total_current_month_expense < total_last_month_expense:
        console.print("[bold green]Overall spending is trending DOWN.[/bold green]")
    else:
        console.print("Overall spending is stable.")

    console.print("Overall spending is stable.")

def income_analysis():
    console.print("[bold green]Income Analysis[/bold green]")
    transactions = _load_transactions()

    if not transactions:
        console.print("No transactions recorded yet for analysis.")
        return

    current_month_income = defaultdict(int)
    last_month_income = defaultdict(int)
    total_current_month_income = 0
    total_last_month_income = 0

    today = datetime.now()
    current_month_start = today.replace(day=1)
    last_month_end = current_month_start - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)

    for t in transactions:
        if t["Type"] == "Income":
            transaction_date = datetime.strptime(t["Date"], "%Y-%m-%d")
            amount = int(t["Amount"])

            if transaction_date >= current_month_start:
                current_month_income[t["Category"]] += amount
                total_current_month_income += amount
            elif transaction_date >= last_month_start and transaction_date <= last_month_end:
                last_month_income[t["Category"]] += amount
                total_last_month_income += amount

    if total_current_month_income == 0:
        console.print("No income recorded for the current month.")
        return

    # Income by Source
    console.print("\n[bold underline]Income by Source (Current Month):[/bold underline]")
    for source, amount in current_month_income.items():
        console.print(f"{source:<12} Rs {amount / 100:.2f}")

    # Total Income this month
    console.print(f"\n[bold underline]Total Income (Current Month):[/bold underline] [bold green]Rs {total_current_month_income / 100:.2f}[/bold green]")

    # Comparison with Last Month
    console.print("\n[bold underline]Comparison with Last Month:[/bold underline]")
    console.print(f"Current Month Total Income: Rs {total_current_month_income / 100:.2f}")
    console.print(f"Last Month Total Income: Rs {total_last_month_income / 100:.2f}")

    if total_last_month_income > 0:
        change = ((total_current_month_income - total_last_month_income) / total_last_month_income) * 100
        if change > 0:
            console.print(f"Income Change: [bold green]+{change:.1f}%[/bold green] compared to last month.")
        elif change < 0:
            console.print(f"Income Change: [bold red]{change:.1f}%[/bold red] compared to last month.")
        else:
            console.print("Income Change: No change compared to last month.")
    else:
        console.print("No income recorded last month for comparison.")

    # Income Stability
    console.print("\n[bold underline]Income Stability:[/bold underline]")
    if total_current_month_income >= total_last_month_income:
        console.print("[bold green]Income is stable or increasing.[/bold green]")


def savings_analysis():
    console.print("[bold purple]Savings Analysis[/bold purple]")
    transactions = _load_transactions()

    if not transactions:
        console.print("No transactions recorded yet for analysis.")
        return

    today = datetime.now()

    # Calculate savings for the last 3 months
    monthly_savings = defaultdict(lambda: {"income": 0, "expense": 0})

    for i in range(3):
        month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1) if i > 0 else today.replace(day=1)
        if i == 1:
            month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        elif i == 2:
            month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
            month_start = (month_start - timedelta(days=1)).replace(day=1)

        month_key = month_start.strftime("%Y-%m")

        for t in transactions:
            transaction_date = datetime.strptime(t["Date"], "%Y-%m-%d")
            if transaction_date.strftime("%Y-%m") == month_key:
                amount = int(t["Amount"])
                if t["Type"] == "Income":
                    monthly_savings[month_key]["income"] += amount
                else:
                    monthly_savings[month_key]["expense"] += amount

    # Calculate current month's savings
    current_month_key = today.strftime("%Y-%m")
    current_month_income = monthly_savings[current_month_key]["income"]
    current_month_expense = monthly_savings[current_month_key]["expense"]
    current_month_net_savings = current_month_income - current_month_expense

    console.print(f"\n[bold underline]Monthly Savings (Current Month - {current_month_key}):[/bold underline]")
    console.print(f"Total Income: [bold green]Rs {current_month_income / 100:.2f}[/bold green]")
    console.print(f"Total Expenses: [bold red]Rs {current_month_expense / 100:.2f}[/bold red]")
    if current_month_net_savings >= 0:
        console.print(f"Net Savings: [bold purple]Rs {current_month_net_savings / 100:.2f}[/bold purple]")
    else:
        console.print(f"Net Savings: [bold red]Rs {current_month_net_savings / 100:.2f}[/bold red]")

    # Savings Rate
    if current_month_income > 0:
        savings_rate = (current_month_net_savings / current_month_income) * 100
        console.print(f"Savings Rate: [bold purple]{savings_rate:.2f}%[/bold purple]")
    else:
        console.print("Savings Rate: N/A (No income recorded for the current month)")

    # Savings Trend (last 3 months)
    console.print("\n[bold underline]Savings Trend (Last 3 Months):[/bold underline]")

    trend_data = []
    for i in range(3):
        month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1) if i > 0 else today.replace(day=1)
        if i == 1:
            month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        elif i == 2:
            month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
            month_start = (month_start - timedelta(days=1)).replace(day=1)

        month_key = month_start.strftime("%Y-%m")
        income = monthly_savings[month_key]["income"]
        expense = monthly_savings[month_key]["expense"]
        net_savings = income - expense
        trend_data.append((month_key, net_savings))

    trend_data.sort(key=lambda x: x[0]) # Sort by month

    for month, savings in trend_data:
        if savings >= 0:
            console.print(f"{month}: [bold purple]Rs {savings / 100:.2f}[/bold purple]")
        else:
            console.print(f"{month}: [bold red]Rs {savings / 100:.2f}[/bold red]")

    # Simple trend interpretation
    if len(trend_data) >= 2:
        if trend_data[-1][1] > trend_data[-2][1]:
            console.print("[bold green]Savings are trending UP.[/bold green]")
        elif trend_data[-1][1] < trend_data[-2][1]:
            console.print("[bold red]Savings are trending DOWN.[/bold red]")
        else:
            console.print("Savings are stable.")

    if len(trend_data) >= 2:
        if trend_data[-1][1] > trend_data[-2][1]:
            console.print("[bold green]Savings are trending UP.[/bold green]")
        elif trend_data[-1][1] < trend_data[-2][1]:
            console.print("[bold red]Savings are trending DOWN.[/bold red]")
        else:
            console.print("Savings are stable.")

# Budget Categories (from GEMINI.md)
BUDGET_CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]
BUDGET_FILE = 'finance_tracker/database/budgets.txt'

def _get_budgets():
    """Reads budgets from budgets.txt."""
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

def financial_health_score():
    console.print("[bold yellow]Financial Health Score[/bold yellow]")
    transactions = _load_transactions()
    budgets = _get_budgets()

    if not transactions:
        console.print("No transactions recorded yet for analysis. Financial health score cannot be calculated.")
        return

    today = datetime.now()
    current_month_key = today.strftime("%Y-%m")

    total_income_current_month = 0
    total_expense_current_month = 0

    spent_this_month_by_category = defaultdict(int)

    for t in transactions:
        transaction_date = datetime.strptime(t["Date"], "%Y-%m-%d")
        if transaction_date.strftime("%Y-%m") == current_month_key:
            amount = int(t["Amount"])
            if t["Type"] == "Income":
                total_income_current_month += amount
            else:
                total_expense_current_month += amount
                spent_this_month_by_category[t["Category"]] += amount

    # 1. Savings Rate (30 points)
    savings_rate_score = 0
    net_savings = total_income_current_month - total_expense_current_month
    if total_income_current_month > 0:
        savings_rate = (net_savings / total_income_current_month) * 100
        if savings_rate >= 20: # Excellent savings rate
            savings_rate_score = 30
        elif savings_rate >= 10: # Good savings rate
            savings_rate_score = 20
        elif savings_rate > 0: # Some savings
            savings_rate_score = 10
        else: # No savings or negative savings
            savings_rate_score = 0

    # 2. Budget Adherence (25 points)
    budget_adherence_score = 0
    if budgets:
        in_budget_categories = 0
        for category, budget_amount in budgets.items():
            spent_amount = spent_this_month_by_category.get(category, 0)
            if spent_amount <= budget_amount:
                in_budget_categories += 1

        if len(budgets) > 0:
            adherence_percentage = (in_budget_categories / len(budgets)) * 100
            if adherence_percentage >= 90:
                budget_adherence_score = 25
            elif adherence_percentage >= 70:
                budget_adherence_score = 15
            elif adherence_percentage >= 50:
                budget_adherence_score = 5
            else:
                budget_adherence_score = 0

    # 3. Income vs Expenses (25 points)
    income_vs_expense_score = 0
    if total_income_current_month > total_expense_current_month:
        income_vs_expense_score = 25
    elif total_income_current_month == total_expense_current_month and total_income_current_month > 0:
        income_vs_expense_score = 10
    else:
        income_vs_expense_score = 0

    # 4. Debt Management (20 points) - Placeholder as debt is not tracked
    debt_management_score = 15 # Assuming reasonable debt management for now

    overall_score = savings_rate_score + budget_adherence_score + income_vs_expense_score + debt_management_score

    console.print(f"\n[bold underline]Your Financial Health Score: {overall_score}/100[/bold underline]")

    console.print("\n[bold]Score Breakdown:[/bold]")
    console.print(f"  Savings Rate: {savings_rate_score}/30")
    console.print(f"  Budget Adherence: {budget_adherence_score}/25")
    console.print(f"  Income vs Expenses: {income_vs_expense_score}/25")
    console.print(f"  Debt Management: {debt_management_score}/20 (Assumed, as debt tracking is not implemented)")

    console.print("\n[bold underline]Interpretation and Recommendations:[/bold underline]")
    if overall_score >= 80:
        console.print("[bold green]Excellent! Your financial health is strong. Keep up the great work![/bold green]")
        console.print("  - Consider increasing investments or setting more ambitious savings goals.")
    elif overall_score >= 60:
        console.print("[bold yellow]Good. Your finances are in a healthy state, but there's room for improvement.[/bold yellow]")
        console.print("  - Review your budget for areas to optimize spending.")
        console.print("  - Look for opportunities to increase your savings rate.")
    elif overall_score >= 40:
        console.print("[bold orange3]Fair. Your financial health needs attention.[/bold orange3]")
        console.print("  - Focus on creating and sticking to a strict budget.")
        console.print("  - Identify and reduce unnecessary expenses.")
        console.print("  - Explore ways to increase your income.")
    else:
        console.print("[bold red]Poor. Your financial health is at risk. Immediate action is required.[/bold red]")
        console.print("  - Develop a detailed plan to reduce expenses and increase income.")
        console.print("  - Seek financial advice if needed.")
        console.print("  - Prioritize building an emergency fund.")

        console.print("  - Prioritize building an emergency fund.")

def monthly_report():
    console.print("[bold cyan]Comprehensive Monthly Report[/bold cyan]")
    transactions = _load_transactions()
    budgets = _get_budgets()

    if not transactions:
        console.print("No transactions recorded yet for report generation.")
        return

    today = datetime.now()
    current_month_key = today.strftime("%Y-%m")
    current_month_name = today.strftime("%B %Y")

    console.print(f"\n[bold underline]Report for {current_month_name}[/bold underline]")

    # --- Data Aggregation ---
    total_income_current_month = 0
    total_expense_current_month = 0
    income_by_source_current_month = defaultdict(int)
    expense_by_category_current_month = defaultdict(int)
    current_month_transactions = []

    last_month_end = today.replace(day=1) - timedelta(days=1)
    last_month_start = last_month_end.replace(day=1)
    last_month_key = last_month_start.strftime("%Y-%m")
    total_income_last_month = 0
    total_expense_last_month = 0

    for t in transactions:
        transaction_date = datetime.strptime(t["Date"], "%Y-%m-%d")
        amount = int(t["Amount"])

        if transaction_date.strftime("%Y-%m") == current_month_key:
            current_month_transactions.append(t)
            if t["Type"] == "Income":
                total_income_current_month += amount
                income_by_source_current_month[t["Category"]] += amount
            else:
                total_expense_current_month += amount
                expense_by_category_current_month[t["Category"]] += amount
        elif transaction_date.strftime("%Y-%m") == last_month_key:
            if t["Type"] == "Income":
                total_income_last_month += amount
            else:
                total_expense_last_month += amount

    # --- Income Summary ---
    console.print("\n[bold underline]Income Summary:[/bold underline]")
    console.print(f"  Total Income this month: [bold green]Rs {total_income_current_month / 100:.2f}[/bold green]")
    if total_income_last_month > 0:
        income_change = ((total_income_current_month - total_income_last_month) / total_income_last_month) * 100
        if income_change >= 0:
            console.print(f"  Vs Last Month: [bold green]+{income_change:.1f}%[/bold green]")
        else:
            console.print(f"  Vs Last Month: [bold red]{income_change:.1f}%[/bold red]")
    else:
        console.print("  Vs Last Month: No income recorded last month.")

    console.print("  Income by Source:")
    for source, amount in income_by_source_current_month.items():
        console.print(f"    - {source}: Rs {amount / 100:.2f}")

    # --- Expense Summary ---
    console.print("\n[bold underline]Expense Summary:[/bold underline]")
    console.print(f"  Total Expenses this month: [bold red]Rs {total_expense_current_month / 100:.2f}[/bold red]")
    if total_expense_last_month > 0:
        expense_change = ((total_expense_current_month - total_expense_last_month) / total_expense_last_month) * 100
        if expense_change >= 0:
            console.print(f"  Vs Last Month: [bold red]+{expense_change:.1f}%[/bold red]")
        else:
            console.print(f"  Vs Last Month: [bold green]{expense_change:.1f}%[/bold green]")
    else:
        console.print("  Vs Last Month: No expenses recorded last month.")

    console.print("  Top Spending Categories:")
    sorted_expenses = sorted(expense_by_category_current_month.items(), key=lambda item: item[1], reverse=True)
    for i, (category, amount) in enumerate(sorted_expenses[:3]):
        console.print(f"    {i+1}. {category}: Rs {amount / 100:.2f}")

    # --- Budget Performance ---
    console.print("\n[bold underline]Budget Performance:[/bold underline]")
    if budgets:
        budget_table = Table(title="Budget vs. Actual")
        budget_table.add_column("Category", style="cyan")
        budget_table.add_column("Budget", style="magenta", justify="right")
        budget_table.add_column("Spent", style="red", justify="right")
        budget_table.add_column("Remaining", style="green", justify="right")
        budget_table.add_column("Status", justify="center")

        total_budget_amount = 0
        total_spent_amount = 0

        for category in BUDGET_CATEGORIES:
            budget_amount = budgets.get(category, 0)
            spent_amount = expense_by_category_current_month.get(category, 0)

            total_budget_amount += budget_amount
            total_spent_amount += spent_amount

            remaining = budget_amount - spent_amount
            status_color = "green"
            status_text = "OK"
            if budget_amount > 0 and spent_amount > budget_amount:
                status_color = "red"
                status_text = "OVER"
            elif budget_amount > 0 and (spent_amount / budget_amount) >= 0.7:
                status_color = "yellow"
                status_text = "Warning"

            budget_table.add_row(
                category,
                f"Rs {budget_amount / 100:.2f}",
                f"Rs {spent_amount / 100:.2f}",
                f"Rs {remaining / 100:.2f}",
                f"[{status_color}]{status_text}[/{status_color}]"
            )
        console.print(budget_table)
        console.print(f"  Total Budget: Rs {total_budget_amount / 100:.2f}, Total Spent: Rs {total_spent_amount / 100:.2f}")
    else:
        console.print("  No budgets set for the current month.")

    # --- Savings Achieved ---
    console.print("\n[bold underline]Savings Achieved:[/bold underline]")
    net_savings_current_month = total_income_current_month - total_expense_current_month
    if net_savings_current_month >= 0:
        console.print(f"  Net Savings: [bold purple]Rs {net_savings_current_month / 100:.2f}[/bold purple]")
    else:
        console.print(f"  Net Savings: [bold red]Rs {net_savings_current_month / 100:.2f}[/bold red]")

    if total_income_current_month > 0:
        savings_rate = (net_savings_current_month / total_income_current_month) * 100
        console.print(f"  Savings Rate: [bold purple]{savings_rate:.2f}%[/bold purple]")
    else:
        console.print("  Savings Rate: N/A (No income recorded)")

    # --- Top Transactions ---
    console.print("\n[bold underline]Top Transactions (Current Month):[/bold underline]")
    if current_month_transactions:
        # Sort by absolute amount for top transactions
        sorted_transactions = sorted(current_month_transactions, key=lambda x: abs(int(x["Amount"])), reverse=True)

        top_transactions_table = Table(show_header=True, header_style="bold blue")
        top_transactions_table.add_column("Date", style="dim")
        top_transactions_table.add_column("Type")
        top_transactions_table.add_column("Category")
        top_transactions_table.add_column("Description")
        top_transactions_table.add_column("Amount", justify="right")

        for i, t in enumerate(sorted_transactions[:5]): # Top 5 transactions
            amount_display = f"Rs {int(t['Amount']) / 100:.2f}"
            if t["Type"] == "Expense":
                top_transactions_table.add_row(
                    t["Date"],
                    f"[bold red]{t['Type']}[/bold red]",
                    t["Category"],
                    t["Description"],
                    f"[bold red]{amount_display}[/bold red]"
                )
            else:
                top_transactions_table.add_row(
                    t["Date"],
                    f"[bold green]{t['Type']}[/bold green]",
                    t["Category"],
                    t["Description"],
                    f"[bold green]{amount_display}[/bold green]"
                )
        console.print(top_transactions_table)
    else:
        console.print("  No transactions to display for the current month.")

    # --- Trends (simplified) ---
    console.print("\n[bold underline]Overall Trends:[/bold underline]")
    if total_expense_current_month > total_expense_last_month:
        console.print("[bold red]  Spending is trending UP.[/bold red]")
    elif total_expense_current_month < total_expense_last_month:
        console.print("[bold green]  Spending is trending DOWN.[/bold green]")
    else:
        console.print("  Spending is stable.")

    if total_income_current_month > total_income_last_month:
        console.print("[bold green]  Income is trending UP.[/bold green]")
    elif total_income_current_month < total_income_last_month:
        console.print("[bold red]  Income is trending DOWN.[/bold red]")
    else:
        console.print("  Income is stable.")

    # --- Recommendations (based on a simplified score) ---
    console.print("\n[bold underline]Recommendations:[/bold underline]")
    # Re-calculate a simplified score for recommendations
    simplified_score = 0
    if total_income_current_month > total_expense_current_month:
        simplified_score += 1
    if net_savings_current_month > 0:
        simplified_score += 1
    if total_expense_current_month < total_expense_last_month:
        simplified_score += 1

    if simplified_score >= 2:
        console.print("[bold green]  Your finances are looking good! Keep monitoring and consider setting new financial goals.[/bold green]")
    elif simplified_score == 1:
        console.print("[bold yellow]  You're on the right track, but there's room for improvement. Review your spending habits.[/bold yellow]")
    else:
        console.print("[bold red]  It seems your finances need attention. Focus on increasing income and reducing unnecessary expenses.[/bold red]")
