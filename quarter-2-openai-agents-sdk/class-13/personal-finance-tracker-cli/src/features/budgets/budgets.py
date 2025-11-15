import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime
import csv
import os

# Initialize Rich Console
console = Console()

BUDGET_FILE = 'finance_tracker/database/budgets.txt'
TRANSACTIONS_FILE = 'finance_tracker/database/transactions.csv' # Changed to .csv

# Ensure the database directory exists
os.makedirs(os.path.dirname(BUDGET_FILE), exist_ok=True)
os.makedirs(os.path.dirname(TRANSACTIONS_FILE), exist_ok=True)

# Budget Categories (from GEMINI.md)
BUDGET_CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]

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

def _save_budgets(budgets):
    """Saves budgets to budgets.txt."""
    with open(BUDGET_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for category, amount_paisa in budgets.items():
            writer.writerow([category, amount_paisa])

def _load_transactions():
    """Loads transactions from transactions.csv."""
    transactions = []
    try:
        with open(TRANSACTIONS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        pass
    return transactions

def set_budget():
    """Allows the user to set a monthly budget for a category."""
    console.print("[bold cyan]Set Monthly Budget[/bold cyan]")

    category = questionary.select(
        "Select a category for the budget:",
        choices=BUDGET_CATEGORIES
    ).ask()

    if not category:
        console.print("[red]Budget setting cancelled.[/red]")
        return

    while True:
        amount_str = questionary.text(f"Enter monthly budget amount for {category} (e.g., 500.00):").ask()
        if not amount_str:
            console.print("[red]Budget setting cancelled.[/red]")
            return
        try:
            amount_float = float(amount_str)
            if amount_float <= 0:
                console.print("[red]Amount must be a positive number. Please try again.[/red]")
                continue
            amount_paisa = int(amount_float * 100)
            break
        except ValueError:
            console.print("[red]Invalid amount. Please enter a number (e.g., 500.00).[/red]")

    budgets = _get_budgets()
    budgets[category] = amount_paisa
    _save_budgets(budgets)
    console.print(f"[green]Budget for {category} set to Rs {amount_paisa / 100:.2f}.[/green]")

def view_budgets():
    """Displays current budget allocations and spending against them."""
    console.print("[bold cyan]Monthly Budget Overview[/bold cyan]")

    budgets = _get_budgets()
    if not budgets:
        console.print("[yellow]No budgets set yet. Use 'Set Budget' to add some.[/yellow]")
        return

    transactions = _load_transactions()
    spent_this_month = {category: 0 for category in BUDGET_CATEGORIES}
    current_month = datetime.now().strftime("%Y-%m")

    for t in transactions:
        if t["Type"] == "Expense" and t["Date"].startswith(current_month):
            category = t["Category"]
            amount = int(t["Amount"])
            spent_this_month[category] += amount

    table = Table(title="Budget vs. Actual (Current Month)")
    table.add_column("Category", style="cyan", justify="left")
    table.add_column("Budget", style="magenta", justify="right")
    table.add_column("Spent", style="red", justify="right")
    table.add_column("Remaining", style="green", justify="right")
    table.add_column("Utilization", style="blue", justify="right")
    table.add_column("Status", justify="center")

    total_budget = 0
    total_spent = 0
    
    for category in BUDGET_CATEGORIES:
        budget_amount = budgets.get(category, 0)
        spent_amount = spent_this_month.get(category, 0)

        total_budget += budget_amount
        total_spent += spent_amount

        remaining = budget_amount - spent_amount
        
        if budget_amount > 0:
            utilization_percent = (spent_amount / budget_amount) * 100
        else:
            utilization_percent = 0

        status_color = "green"
        status_text = "OK"
        if utilization_percent >= 100:
            status_color = "red"
            status_text = "OVER"
        elif utilization_percent >= 70:
            status_color = "yellow"
            status_text = "Warning"

        table.add_row(
            category,
            f"Rs {budget_amount / 100:.2f}",
            f"Rs {spent_amount / 100:.2f}",
            f"Rs {remaining / 100:.2f}",
            f"{utilization_percent:.2f}%",
            f"[{status_color}]{status_text}[/{status_color}]"
        )
    
    console.print(table)

    overall_remaining = total_budget - total_spent
    overall_utilization = (total_spent / total_budget) * 100 if total_budget > 0 else 0

    console.print(f"\n[bold]Summary for Current Month:[/bold]")
    console.print(f"  [bold magenta]Total Budget:[/bold magenta] Rs {total_budget / 100:.2f}")
    console.print(f"  [bold red]Total Spent:[/bold red] Rs {total_spent / 100:.2f}")
    console.print(f"  [bold green]Total Remaining:[/bold green] Rs {overall_remaining / 100:.2f}")
    console.print(f"  [bold blue]Overall Utilization:[/bold blue] {overall_utilization:.2f}%")

    over_budget_categories = [cat for cat, budget in budgets.items() if spent_this_month.get(cat, 0) > budget]
    if over_budget_categories:
        console.print("\n[bold red]Categories Over Budget:[/bold red]")
        for cat in over_budget_categories:
            console.print(f"  - {cat}")
