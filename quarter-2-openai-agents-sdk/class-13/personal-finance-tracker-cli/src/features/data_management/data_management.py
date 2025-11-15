import csv
import json
import os
from datetime import datetime
import questionary
from rich.console import Console

console = Console()

TRANSACTIONS_FILE = "finance_tracker/database/transactions.csv"
BUDGET_FILE = "finance_tracker/database/budgets.txt"

# --- Helper functions to load data (copied from transactions.py and budgets.py) ---
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
# --- End Helper functions ---

def export_data():
    console.print("[bold blue]Export Data[/bold blue]")

    export_format = questionary.select(
        "Select export format:",
        choices=["CSV", "JSON"]
    ).ask()

    if not export_format:
        console.print("[red]Export cancelled.[/red]")
        return

    data_type = questionary.select(
        "Select data type to export:",
        choices=["Transactions", "Budgets"]
    ).ask()

    if not data_type:
        console.print("[red]Export cancelled.[/red]")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = ""
    data_to_export = []
    fieldnames = []

    if data_type == "Transactions":
        data_to_export = _load_transactions()
        fieldnames = ["Date", "Type", "Category", "Description", "Amount"]
        filename = f"transactions_export_{timestamp}"
    elif data_type == "Budgets":
        budgets_dict = _get_budgets()
        data_to_export = [{"Category": k, "Amount": v} for k, v in budgets_dict.items()]
        fieldnames = ["Category", "Amount"]
        filename = f"budgets_export_{timestamp}"

    if not data_to_export:
        console.print(f"[yellow]No {data_type.lower()} data to export.[/yellow]")
        return

    try:
        if export_format == "CSV":
            filename += ".csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_to_export)
        elif export_format == "JSON":
            filename += ".json"
            with open(filename, mode='w') as file:
                json.dump(data_to_export, file, indent=4)
        
        console.print(f"[bold green]Data exported successfully to {filename}[/bold green]")
    except IOError as e:
        console.print(f"[bold red]Error exporting data: {e}[/bold red]")

    except IOError as e:
        console.print(f"[bold red]Error exporting data: {e}[/bold red]")

# --- Helper functions to save data ---
def _save_transactions(transactions):
    with open(TRANSACTIONS_FILE, mode='w', newline='') as file:
        fieldnames = ["Date", "Type", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

def _save_budgets(budgets):
    with open(BUDGET_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for category, amount_paisa in budgets.items():
            writer.writerow([category, amount_paisa])
# --- End Helper functions ---

def import_data():
    console.print("[bold blue]Import Data[/bold blue]")

    file_path = questionary.text("Enter the path to the file to import:").ask()
    if not file_path:
        console.print("[red]Import cancelled.[/red]")
        return

    if not os.path.exists(file_path):
        console.print(f"[bold red]Error: File not found at {file_path}[/bold red]")
        return

    data_type = questionary.select(
        "Select data type to import:",
        choices=["Transactions", "Budgets"]
    ).ask()

    if not data_type:
        console.print("[red]Import cancelled.[/red]")
        return

    merge_option = questionary.select(
        "How to handle existing data?",
        choices=["Merge (add new data to existing)", "Overwrite (replace existing data)"]
    ).ask()

    if not merge_option:
        console.print("[red]Import cancelled.[/red]")
        return

    try:
        imported_data = []
        if file_path.endswith(".csv"):
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    imported_data.append(row)
        elif file_path.endswith(".json"):
            with open(file_path, mode='r') as file:
                imported_data = json.load(file)
        else:
            console.print("[bold red]Error: Unsupported file format. Only .csv and .json are supported.[/bold red]")
            return

        if data_type == "Transactions":
            # Validate transactions
            valid_transactions = []
            for t in imported_data:
                if not all(key in t for key in ["Date", "Type", "Category", "Description", "Amount"]):
                    console.print(f"[bold red]Skipping invalid transaction (missing fields): {t}[/bold red]")
                    continue
                try:
                    datetime.strptime(t["Date"], "%Y-%m-%d")
                    int(t["Amount"]) # Check if amount is convertible to int
                    valid_transactions.append(t)
                except ValueError:
                    console.print(f"[bold red]Skipping invalid transaction (date or amount format error): {t}[/bold red]")
                    continue
            
            if merge_option == "Merge (add new data to existing)":
                existing_transactions = _load_transactions()
                final_transactions = existing_transactions + valid_transactions
            else: # Overwrite
                final_transactions = valid_transactions
            
            _save_transactions(final_transactions)
            console.print(f"[bold green]Successfully imported {len(valid_transactions)} transactions.[/bold green]")

        elif data_type == "Budgets":
            # Validate budgets
            valid_budgets = {}
            for b in imported_data:
                if not all(key in b for key in ["Category", "Amount"]):
                    console.print(f"[bold red]Skipping invalid budget (missing fields): {b}[/bold red]")
                    continue
                try:
                    valid_budgets[b["Category"]] = int(b["Amount"])
                except ValueError:
                    console.print(f"[bold red]Skipping invalid budget (amount format error): {b}[/bold red]")
                    continue
            
            if merge_option == "Merge (add new data to existing)":
                existing_budgets = _get_budgets()
                existing_budgets.update(valid_budgets)
                final_budgets = existing_budgets
            else: # Overwrite
                final_budgets = valid_budgets
            
            _save_budgets(final_budgets)
            console.print(f"[bold green]Successfully imported {len(valid_budgets)} budgets.[/bold green]")

    except (IOError, json.JSONDecodeError) as e:
        console.print(f"[bold red]Error importing data: {e}[/bold red]")

    except (IOError, json.JSONDecodeError) as e:
        console.print(f"[bold red]Error importing data: {e}[/bold red]")

def clear_data():
    console.print("[bold red]Clear Data[/bold red]")

    data_type_to_clear = questionary.select(
        "What data do you want to clear?",
        choices=["All Transactions", "All Budgets", "Cancel"]
    ).ask()

    if data_type_to_clear == "Cancel":
        console.print("[yellow]Data clearing cancelled.[/yellow]")
        return

    confirmation = questionary.confirm(
        f"[bold red]Are you sure you want to clear {data_type_to_clear}? This action cannot be undone.[/bold red]"
    ).ask()

    if not confirmation:
        console.print("[yellow]Data clearing cancelled.[/yellow]")
        return

    try:
        if data_type_to_clear == "All Transactions":
            _save_transactions([]) # Overwrite with empty list
            console.print("[bold green]All transactions cleared successfully.[/bold green]")
        elif data_type_to_clear == "All Budgets":
            _save_budgets({}) # Overwrite with empty dictionary
            console.print("[bold green]All budgets cleared successfully.[/bold green]")
    except IOError as e:
        console.print(f"[bold red]Error clearing data: {e}[/bold red]")

    except IOError as e:
        console.print(f"[bold red]Error clearing data: {e}[/bold red]")

BACKUP_DIR = "finance_tracker/database/backups"

def backup_data():
    console.print("[bold blue]Backup Data[/bold blue]")
    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Backup transactions
    transactions_backup_file = os.path.join(BACKUP_DIR, f"transactions_{timestamp}.csv")
    try:
        with open(TRANSACTIONS_FILE, 'r', newline='') as src, \
             open(transactions_backup_file, 'w', newline='') as dst:
            dst.write(src.read())
        console.print(f"[green]Transactions backed up to {transactions_backup_file}[/green]")
    except FileNotFoundError:
        console.print("[yellow]No transactions file found to backup.[/yellow]")
    except IOError as e:
        console.print(f"[bold red]Error backing up transactions: {e}[/bold red]")

    # Backup budgets
    budgets_backup_file = os.path.join(BACKUP_DIR, f"budgets_{timestamp}.txt")
    try:
        with open(BUDGET_FILE, 'r', newline='') as src, \
             open(budgets_backup_file, 'w', newline='') as dst:
            dst.write(src.read())
        console.print(f"[green]Budgets backed up to {budgets_backup_file}[/green]")
    except FileNotFoundError:
        console.print("[yellow]No budgets file found to backup.[/yellow]")
    except IOError as e:
        console.print(f"[bold red]Error backing up budgets: {e}[/bold red]")

def restore_data():
    console.print("[bold blue]Restore Data[/bold blue]")

    if not os.path.exists(BACKUP_DIR) or not os.listdir(BACKUP_DIR):
        console.print("[yellow]No backups found.[/yellow]")
        return

    backup_files = sorted(os.listdir(BACKUP_DIR), reverse=True)
    
    # Group by timestamp
    backup_sets = defaultdict(lambda: {"transactions": None, "budgets": None})
    for f in backup_files:
        parts = f.split('_')
        if len(parts) >= 3:
            file_type = parts[0]
            timestamp = parts[1]
            if file_type == "transactions":
                backup_sets[timestamp]["transactions"] = f
            elif file_type == "budgets":
                backup_sets[timestamp]["budgets"] = f
    
    choices = []
    for ts in sorted(backup_sets.keys(), reverse=True):
        choices.append(f"Backup from {datetime.strptime(ts, '%Y%m%d_%H%M%S').strftime('%Y-%m-%d %H:%M:%S')} (T: {backup_sets[ts]['transactions'] or 'N/A'}, B: {backup_sets[ts]['budgets'] or 'N/A'})")
    
    if not choices:
        console.print("[yellow]No valid backup sets found.[/yellow]")
        return

    selected_backup_display = questionary.select(
        "Select a backup to restore:",
        choices=choices
    ).ask()

    if not selected_backup_display:
        console.print("[yellow]Restore cancelled.[/yellow]")
        return
    
    # Extract timestamp from selected display string
    selected_timestamp = selected_backup_display.split(' ')[2] # Assuming format "Backup from YYYY-MM-DD HH:MM:SS (T: ..., B: ...)"
    
    selected_backup = backup_sets[selected_timestamp]

    confirmation = questionary.confirm(
        "[bold red]Are you sure you want to restore this backup? Current data will be overwritten.[/bold red]"
    ).ask()

    if not confirmation:
        console.print("[yellow]Restore cancelled.[/yellow]")
        return

    try:
        if selected_backup["transactions"]:
            src_path = os.path.join(BACKUP_DIR, selected_backup["transactions"])
            with open(src_path, 'r', newline='') as src, \
                 open(TRANSACTIONS_FILE, 'w', newline='') as dst:
                dst.write(src.read())
            console.print(f"[green]Transactions restored from {selected_backup['transactions']}[/green]")
        else:
            console.print("[yellow]No transactions backup found in selected set.[/yellow]")

        if selected_backup["budgets"]:
            src_path = os.path.join(BACKUP_DIR, selected_backup["budgets"])
            with open(src_path, 'r', newline='') as src, \
                 open(BUDGET_FILE, 'w', newline='') as dst:
                dst.write(src.read())
            console.print(f"[green]Budgets restored from {selected_backup['budgets']}[/green]")
        else:
            console.print("[yellow]No budgets backup found in selected set.[/yellow]")

        console.print("[bold green]Data restore complete.[/bold green]")

    except IOError as e:
        console.print(f"[bold red]Error restoring data: {e}[/bold red]")
