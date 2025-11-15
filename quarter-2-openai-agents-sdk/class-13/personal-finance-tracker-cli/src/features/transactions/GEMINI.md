# Day 2: Transaction Management

## Goal
Build the core feature - tracking expenses and income transactions.

## Learning Focus
- Working with money in code (avoid float errors!)
- Date handling
- File operations
- Input validation
- Transaction categories

## Fintech Concepts
- **Transaction**: Any money movement (in or out)
- **Debit**: Money going out (expense)
- **Credit**: Money coming in (income)
- **Categories**: Grouping transactions (Food, Transport, Salary, etc.)

## Features to Build

### 1. Add Expense
Flow:
1. Ask amount (validate: must be positive number)
2. Ask category (Food, Transport, Shopping, Bills, Entertainment, Health, Other)
3. Ask description (e.g., "Lunch at restaurant")
4. Ask date (default: today, or allow custom date)
5. Save to transactions.txt

### 2. Add Income
Flow:
1. Ask amount
2. Ask source (Salary, Freelance, Business, Investment, Gift, Other)
3. Ask description
4. Ask date
5. Save to transactions.txt

### 3. List Transactions
Display:
- Show transactions in Rich table
- Columns: Date, Type, Category, Description, Amount
- Color: Red for expenses, Green for income
- Sort by date (newest first)
- Optional filters: last 7 days, only expenses, only income

### 4. Balance Command
Display:
- Total Income (green)
- Total Expenses (red)
- Current Balance (green if positive, red if negative)
- Show for current month

## Success Criteria

✅ Can add expenses with validation
✅ Can add income with validation
✅ Can list all transactions
✅ Can filter transactions by days
✅ Can see current balance
✅ Money calculations are accurate (no float errors)
✅ Beautiful colored output
