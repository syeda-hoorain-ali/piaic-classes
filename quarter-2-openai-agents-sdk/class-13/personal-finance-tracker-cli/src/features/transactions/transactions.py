import csv
from datetime import datetime
from rich.console import Console
from rich.table import Table
import questionary

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

def _save_transactions(transactions):
    with open(TRANSACTIONS_FILE, mode='w', newline='') as file:
        fieldnames = ["Date", "Type", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

def add_expense():
    console.print("[bold red]Add Expense[/bold red]")
    amount_str = questionary.text("Enter amount (e.g., 12.50):").ask()
    try:
        amount = int(float(amount_str) * 100)  # Store as paisa/cents
        if amount <= 0:
            console.print("[bold red]Amount must be a positive number.[/bold red]")
            return
    except ValueError:
        console.print("[bold red]Invalid amount. Please enter a number.[/bold red]")
        return

    category = questionary.select(
        "Select category:",
        choices=["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]
    ).ask()

    description = questionary.text("Enter description:").ask()

    date_str = questionary.text("Enter date (YYYY-MM-DD, leave blank for today):").ask()
    if not date_str:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            date = date_str
        except ValueError:
            console.print("[bold red]Invalid date format. Please use YYYY-MM-DD.[/bold red]")
            return

    transactions = _load_transactions()
    transactions.append({
        "Date": date,
        "Type": "Expense",
        "Category": category,
        "Description": description,
        "Amount": str(amount)
    })
    _save_transactions(transactions)
    console.print("[bold green]Expense added successfully![/bold green]")

def add_income():
    console.print("[bold green]Add Income[/bold green]")
    amount_str = questionary.text("Enter amount (e.g., 100.00):").ask()
    try:
        amount = int(float(amount_str) * 100)  # Store as paisa/cents
        if amount <= 0:
            console.print("[bold red]Amount must be a positive number.[/bold red]")
            return
    except ValueError:
        console.print("[bold red]Invalid amount. Please enter a number.[/bold red]")
        return

    category = questionary.select(
        "Select source:",
        choices=["Salary", "Freelance", "Business", "Investment", "Gift", "Other"]
    ).ask()

    description = questionary.text("Enter description:").ask()

    date_str = questionary.text("Enter date (YYYY-MM-DD, leave blank for today):").ask()
    if not date_str:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            date = date_str
        except ValueError:
            console.print("[bold red]Invalid date format. Please use YYYY-MM-DD.[/bold red]")
            return

    transactions = _load_transactions()
    transactions.append({
        "Date": date,
        "Type": "Income",
        "Category": category,
        "Description": description,
        "Amount": str(amount)
    })
    _save_transactions(transactions)
    console.print("[bold green]Income added successfully![/bold green]")

def list_transactions():
    console.print("[bold blue]List Transactions[/bold blue]")
    transactions = _load_transactions()

    if not transactions:
        console.print("No transactions recorded yet.")
        return

    # Apply filters
    filter_option = questionary.select(
        "Filter transactions:",
        choices=["All", "Last 7 days", "Only Expenses", "Only Income"]
    ).ask()

    filtered_transactions = []
    today = datetime.now().date()

    for t in transactions:
        include = True
        transaction_date = datetime.strptime(t["Date"], "%Y-%m-%d").date()

        if filter_option == "Last 7 days":
            if (today - transaction_date).days > 7:
                include = False
        elif filter_option == "Only Expenses":
            if t["Type"] != "Expense":
                include = False
        elif filter_option == "Only Income":
            if t["Type"] != "Income":
                include = False
        
        if include:
            filtered_transactions.append(t)

    if not filtered_transactions:
        console.print("No transactions found matching the filter criteria.")
        return

    # Sort by date (newest first)
    filtered_transactions.sort(key=lambda x: datetime.strptime(x["Date"], "%Y-%m-%d"), reverse=True)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim")
    table.add_column("Type")
    table.add_column("Category")
    table.add_column("Description")
    table.add_column("Amount", justify="right")

    for t in filtered_transactions:
        amount_display = f"Rs {int(t['Amount']) / 100:.2f}"
        if t["Type"] == "Expense":
            table.add_row(
                t["Date"],
                f"[bold red]{t['Type']}[/bold red]",
                t["Category"],
                t["Description"],
                f"[bold red]{amount_display}[/bold red]"
            )
        else:
            table.add_row(
                t["Date"],
                f"[bold green]{t['Type']}[/bold green]",
                t["Category"],
                t["Description"],
                f"[bold green]{amount_display}[/bold green]"
            )
    console.print(table)

def get_balance():
    console.print("[bold magenta]Current Balance[/bold magenta]")
    transactions = _load_transactions()

    total_income = 0
    total_expenses = 0
    current_month = datetime.now().strftime("%Y-%m")

    for t in transactions:
        if t["Date"].startswith(current_month):
            amount = int(t["Amount"])
            if t["Type"] == "Income":
                total_income += amount
            else:
                total_expenses += amount

    balance = total_income - total_expenses

    console.print(f"Total Income (this month): [bold green]Rs {total_income / 100:.2f}[/bold green]")
    console.print(f"Total Expenses (this month): [bold red]Rs {total_expenses / 100:.2f}[/bold red]")
    if balance >= 0:
        console.print(f"Current Balance: [bold green]Rs {balance / 100:.2f}[/bold green]")
    else:
        console.print(f"Current Balance: [bold red]Rs {balance / 100:.2f}[/bold red]")
