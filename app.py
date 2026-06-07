from models import Expense
from reports import generate_report

def main():
    # Створюємо список витрат
    my_expenses = [
        Expense(150, "Їжа", "2026-06-07"),
        Expense(500, "Транспорт", "2026-06-07")
    ]
    
    # Викликаємо функцію з модуля reports
    generate_report(my_expenses)

if __name__ == "__main__":
    main()