import os
import sys
import django
import random
from datetime import datetime, timedelta

# 添加專案目錄到 Python 路徑
sys.path.append('/Users/chrissylam/Desktop/assignment/financial_tracker')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financial_tracker.settings')
django.setup()

from income_expense.models import Income, Expense, Investment

# 清理數據函數
def clean_data():
    # 刪除所有現有數據
    Income.objects.all().delete()
    Expense.objects.all().delete()
    Investment.objects.all().delete()
    print("所有數據已清除")

# 生成樣本數據函數
def generate_sample_data():
    # 生成收入數據
    income_sources = ['工資', '獎金', '投資收益', '兼職', '租金']
    for i in range(20):
        Income.objects.create(
            date=datetime.now() - timedelta(days=random.randint(1, 365)),
            source=random.choice(income_sources),
            amount=random.uniform(1000, 20000),
            description=f"收入記錄 #{i+1}"
        )

    # 生成支出數據
    expense_categories = ['飲食', '交通', '娛樂', '住房', '醫療']
    for i in range(20):
        Expense.objects.create(
            date=datetime.now() - timedelta(days=random.randint(1, 365)),
            category=random.choice(expense_categories),
            amount=random.uniform(100, 5000),
            description=f"支出記錄 #{i+1}"
        )

    # 生成投資數據
    investment_types = ['股票', '基金', '債券', '房地產', '加密貨幣']
    for i in range(20):
        Investment.objects.create(
            date=datetime.now() - timedelta(days=random.randint(1, 365)),
            type=random.choice(investment_types),
            amount=random.uniform(5000, 50000),
            return_rate=random.uniform(-10, 20)
        )

    print("已生成60筆樣本數據(每種20筆)")

if __name__ == "__main__":
    clean_data()
    generate_sample_data()