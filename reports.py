def generate_report(expenses):
    print("Генерація звіту для ПФУ...")
    print("-" * 30)
    for expense in expenses:
        print(expense)
    print("-" * 30)
    print(f"Всього витрат: {len(expenses)}")