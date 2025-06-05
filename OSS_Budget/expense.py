class Expense:
    def __init__(self, datetime_str, category, description, amount):
        self.datetime_str = datetime_str  # 시간 추가
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.datetime_str}] {self.category} - {self.description}: {self.amount}원"