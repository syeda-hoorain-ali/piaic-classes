import streamlit as st
import pandas as pd
from datetime import datetime

TRANSACTIONS_FILE = "finance_tracker/database/transactions.txt"
BUDGETS_FILE = "finance_tracker/database/budgets.txt"

def load_transactions():
    try:
        df = pd.read_csv(TRANSACTIONS_FILE, header=None, names=['Date', 'Type', 'Category', 'Description', 'Amount'])
        df['Date'] = pd.to_datetime(df['Date'])
        df['Amount'] = df['Amount'].astype(int) # Store as paisa/cents
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Date', 'Type', 'Category', 'Description', 'Amount'])

def load_budgets():
    try:
        df = pd.read_csv(BUDGETS_FILE, header=None, names=['Category', 'Budget'])
        df['Budget'] = df['Budget'].astype(int) # Store as paisa/cents
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Category', 'Budget'])

def main():
    st.set_page_config(layout="wide")
    st.title("Personal Finance Dashboard")

    transactions_df = load_transactions()
    budgets_df = load_budgets()

    # Get current month's data
    current_month = datetime.now().month
    current_year = datetime.now().year
    monthly_transactions = transactions_df[
        (transactions_df['Date'].dt.month == current_month) &
        (transactions_df['Date'].dt.year == current_year)
    ]

    # Calculate balance
    total_income = monthly_transactions[monthly_transactions['Type'] == 'income']['Amount'].sum()
    total_expenses = monthly_transactions[monthly_transactions['Type'] == 'expense']['Amount'].sum()
    current_balance = total_income - total_expenses

    st.header("Current Balance")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Income", f"Rs {total_income / 100:,.2f}")
    with col2:
        st.metric("Total Expenses", f"Rs {total_expenses / 100:,.2f}")
    with col3:
        st.metric("Current Balance", f"Rs {current_balance / 100:,.2f}")

    st.header("Budget Status")
    if not budgets_df.empty:
        # Calculate spending per category
        expense_by_category = monthly_transactions[monthly_transactions['Type'] == 'expense'].groupby('Category')['Amount'].sum().reset_index()
        
        # Merge with budgets to get budget vs actual
        budget_status_df = pd.merge(budgets_df, expense_by_category, on='Category', how='left').fillna(0)
        budget_status_df.rename(columns={'Amount': 'Spent'}, inplace=True)
        
        budget_status_df['Remaining'] = budget_status_df['Budget'] - budget_status_df['Spent']
        budget_status_df['Utilization'] = (budget_status_df['Spent'] / budget_status_df['Budget']) * 100

        # Format for display
        budget_status_display_df = budget_status_df.copy()
        budget_status_display_df['Budget'] = budget_status_display_df['Budget'].apply(lambda x: f"Rs {x / 100:,.2f}")
        budget_status_display_df['Spent'] = budget_status_display_df['Spent'].apply(lambda x: f"Rs {x / 100:,.2f}")
        budget_status_display_df['Remaining'] = budget_status_display_df['Remaining'].apply(lambda x: f"Rs {x / 100:,.2f}")
        budget_status_display_df['Utilization'] = budget_status_display_df['Utilization'].apply(lambda x: f"{x:,.2f}%")
        
        st.dataframe(budget_status_display_df[['Category', 'Budget', 'Spent', 'Remaining', 'Utilization']], use_container_width=True)

        st.subheader("Budget Progress")
        for index, row in budget_status_df.iterrows():
            category = row['Category']
            spent = row['Spent'] / 100
            budget = row['Budget'] / 100
            utilization_ratio = row['Utilization'] / 100 # For st.progress, it expects a value between 0 and 1

            st.write(f"**{category}** (Rs {spent:,.2f} / Rs {budget:,.2f})")
            st.progress(min(utilization_ratio, 1.0), text=f"{row['Utilization']:.2f}%") # Cap progress at 100% visually

    else:
        st.info("No budgets set yet.")

    st.header("Recent Transactions")
    if not monthly_transactions.empty:
        display_transactions = monthly_transactions.copy()
        display_transactions['Amount'] = display_transactions['Amount'] / 100 # Convert back to Rs for display
        
        # Streamlit's dataframe doesn't directly support cell-level color styling easily without custom CSS/HTML.
        # For simplicity, we'll just display the formatted amount.
        display_transactions['Amount'] = display_transactions['Amount'].apply(lambda x: f"Rs {x:,.2f}")
        
        st.dataframe(display_transactions[['Date', 'Type', 'Category', 'Description', 'Amount']], use_container_width=True)
    else:
        st.info("No transactions for the current month yet.")

if __name__ == "__main__":
    main()
