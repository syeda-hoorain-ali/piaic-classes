# Day 7: Web Dashboard & Final Polish

## Today's Objective
Create a simple web interface to view your finance data and polish the CLI application.

---

## Part A: Simple Web Dashboard

### What You'll Build
A single-page web dashboard that displays:
- Current balance with income and expenses
- Budget progress bars (color-coded)
- Recent transactions in a table
- Clean, professional design

### Tech Stack to Use
- **Streamlit** - Python web framework

**What to Display:**

#### Balance Section
- Large centered balance amount
- Income and expenses side by side
- Use green for income, red for expenses

#### Budget Status Section
- List each budget category
- Show: Budget amount, Spent amount, Percentage
- Progress bars with colors:
  - Green: under 70% used
  - Yellow: 70-99% used
  - Red: 100%+ used (over budget)

#### Recent Transactions Table
- Show last 10 transactions
- Columns: Date, Type, Category, Description, Amount
- Color-code by type (income=green, expense=red)

### Styling Guidelines
- Use card-based design (white boxes with shadows)
- Maximum width: 1200px, centered
- Clean fonts (Arial or similar)
- Plenty of white space
- Mobile-friendly (responsive)

