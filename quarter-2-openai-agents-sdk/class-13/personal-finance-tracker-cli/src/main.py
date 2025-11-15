import questionary
from features.transactions.transactions import add_expense, add_income, list_transactions, get_balance
from features.budgets.budgets import set_budget, view_budgets
from features.analytics.analytics import spending_analysis, income_analysis, savings_analysis, financial_health_score, monthly_report
from features.data_management.data_management import export_data, import_data, clear_data, backup_data, restore_data
from features.smart_assistant.smart_assistant import daily_financial_check, smart_recommendations, spending_alerts_system, savings_opportunities

def main():
    while True:
        choice = questionary.select(
            "What do you want to do?",
            choices=[
                "Add Expense",
                "Add Income",
                "List Transactions",
                "View Balance",
                "Set Budget",
                "View Budgets",
                "Spending Analysis",
                "Income Analysis",
                "Savings Analysis",
                "Financial Health Score",
                "Monthly Report",
                "Export Data",
                "Import Data",
                "Clear Data",
                "Backup Data",
                "Restore Data",
                "Smart Financial Assistant",
                "Exit"
            ]
        ).ask()

        if choice == "Add Expense":
            add_expense()
        elif choice == "Add Income":
            add_income()
        elif choice == "List Transactions":
            list_transactions()
        elif choice == "View Balance":
            get_balance()
        elif choice == "Set Budget":
            set_budget()
        elif choice == "View Budgets":
            view_budgets()
        elif choice == "Spending Analysis":
            spending_analysis()
        elif choice == "Income Analysis":
            income_analysis()
        elif choice == "Savings Analysis":
            savings_analysis()
        elif choice == "Financial Health Score":
            financial_health_score()
        elif choice == "Monthly Report":
            monthly_report()
        elif choice == "Export Data":
            export_data()
        elif choice == "Import Data":
            import_data()
        elif choice == "Clear Data":
            clear_data()
        elif choice == "Backup Data":
            backup_data()
        elif choice == "Restore Data":
            restore_data()
        elif choice == "Smart Financial Assistant":
            while True:
                smart_choice = questionary.select(
                    "Smart Financial Assistant - What would you like to see?",
                    choices=[
                        "Daily Financial Check",
                        "Smart Recommendations",
                        "Spending Alerts System",
                        "Savings Opportunities",
                        "Back to Main Menu"
                    ]
                ).ask()
                if smart_choice == "Daily Financial Check":
                    daily_financial_check()
                elif smart_choice == "Smart Recommendations":
                    smart_recommendations()
                elif smart_choice == "Spending Alerts System":
                    spending_alerts_system()
                elif smart_choice == "Savings Opportunities":
                    savings_opportunities()
                elif smart_choice == "Back to Main Menu":
                    break
        elif choice == "Exit":
            break

if __name__ == "__main__":
    main()
