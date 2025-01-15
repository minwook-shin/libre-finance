from libre_finance import LibreFinance
from libre_finance.database import MariaDBTable

# you need to install sql subpackage
# pip install pip install libre-finance[sql]

t = MariaDBTable(db_name='db', user='user', passwd='passwd', host='127.0.0.1', port=3306)

# deposit example
lf = LibreFinance(amount=12000000, currency='KRW')
print(lf.calculate_deposit(month=6, annual_interest_rate=3.5))
print(f"amount: {lf.amount}")

t.insert_data(lf.history)

# deposit example with non-taxable interest
lf = LibreFinance(amount=12000000, currency='KRW')
print(lf.calculate_deposit(month=6, annual_interest_rate=3.5, is_tax=False))
print(f"amount: {lf.amount}")

t.insert_data(lf.history)

# savings example
lf = LibreFinance(amount=0, currency='KRW')
print(lf.calculate_savings(month=6, monthly_deposit=1000000, annual_interest_rate=3.5))
print(f"amount: {lf.amount}")

t.insert_data(lf.history)

# savings example with non-taxable interest
lf = LibreFinance(amount=0, currency='KRW')
print(lf.calculate_savings(month=6, monthly_deposit=1000000, is_tax=False, annual_interest_rate=3.5))
print(f"amount: {lf.amount}")

t.insert_data(lf.history)
