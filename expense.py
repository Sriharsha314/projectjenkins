def expense_summary(name, expenses):
    if not expenses:
        total = 0
        summary = "No expenses recorded"
    else:
        total = sum(e["amount"] for e in expenses)
        category_totals = {}

        for e in expenses:
            category = e["category"]
            category_totals[category] = category_totals.get(category, 0) + e["amount"]

        summary_lines = []
        for cat, amt in category_totals.items():
            summary_lines.append(f"{cat}: ₹{amt}")

        summary = "\n".join(summary_lines)

    result = (
        f"User Name: {name}\n"
        f"Total Expense: ₹{total}\n"
        f"Category Summary:\n"
        f"{summary}\n"
    )
    return result


if __name__ == "__main__":
    expenses = [
        {"date": "01-01-2025", "category": "Food", "amount": 200, "note": "Lunch"},
        {"date": "02-01-2025", "category": "Travel", "amount": 150, "note": "Bus"},
        {"date": "03-01-2025", "category": "Food", "amount": 100, "note": "Snacks"}
    ]

    print(expense_summary("Nagaraj", expenses))
