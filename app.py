from models import Expense
import reports

def main():
    my_expenses = [
        Expense(150, "Їжа", "2026-06-07"),
        Expense(500, "Транспорт", "2026-06-07")
    ]
    reports.generate_report(my_expenses)

if __name__ == "__main__":
    main()
  
