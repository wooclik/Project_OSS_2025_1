import datetime
import random
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        self.printRandomTip()

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


    def printRandomTip(self):
        tips = [ #팁 목록은 GPT에서 가져왔습니다...
            "배달 대신 장보기를 이용해보세요!",
            "가계부를 매일 작성하는 습관을 들이세요.",
            "불필요한 구독 서비스를 해지해보세요.",
            "할인이 아닐 땐 꼭 필요한 것만 사세요.",
            "외식보다 직접 요리해보세요.",
            "현금보단 예산 한도 내 카드 사용을 고려해보세요.",
            "대중교통을 이용하면 교통비를 줄일 수 있어요.",
            "비싼 커피 대신 텀블러+홈브루 추천!",
        ]
        tip = random.choice(tips)
        print(f"💡 절약 팁: {tip}\n")