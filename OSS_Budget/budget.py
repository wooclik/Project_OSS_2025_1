import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def saveToTxt(self, filename="지출목록록.txt"):
        if not self.expenses:
            print("지출 내역이 없으므로 저장하지 않습니다.\n")
            return

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("지출 목록록\n")
                f.write("=" * 30 + "\n")
                for idx, e in enumerate(self.expenses, 1):
                    f.write(f"{idx}. {e}\n")
                f.write("=" * 30 + "\n")
                total = sum(e.amount for e in self.expenses)
                f.write(f"총 지출 : {total}원\n")
            print(f"TXT로 저장 완료 : {filename}\n")
        except Exception as e:
            print(f"[오류] TXT 저장 실패 : {e}\n")

