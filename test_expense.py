import pytest
from expense import expense_summary


def test_expense_with_data():
    expenses = [
        {"date": "01-01-2025", "category": "Food", "amount": 200, "note": "Lunch"},
        {"date": "02-01-2025", "category": "Travel", "amount": 150, "note": "Bus"},
        {"date": "03-01-2025", "category": "Food", "amount": 100, "note": "Snacks"}
    ]

    expected_output = (
        "User Name: Nagaraj\n"
        "Total Expense: ₹450\n"
        "Category Summary:\n"
        "Food: ₹300\n"
        "Travel: ₹150\n"
    )

    assert expense_summary("Nagaraj", expenses) == expected_output


def test_no_expenses():
    expected_output = (
        "User Name: Ravi\n"
        "Total Expense: ₹0\n"
        "Category Summary:\n"
        "No expenses recorded\n"
    )

    assert expense_summary("Ravi", []) == expected_output
