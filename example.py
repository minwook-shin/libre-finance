from libre_finance import LibreFinance

# deposit example
lf = LibreFinance(amount=12000000, currency='KRW')
print(lf.calculate_deposit(month=6, annual_interest_rate=3.5))
print(f"amount: {lf.amount}")

# deposit example with non-taxable interest
lf = LibreFinance(amount=12000000, currency='KRW')
print(lf.calculate_deposit(month=6, annual_interest_rate=3.5, is_tax=False))
print(f"amount: {lf.amount}")

# savings example
lf = LibreFinance(amount=0, currency='KRW')
print(lf.calculate_savings(month=6, monthly_deposit=1000000, annual_interest_rate=3.5))
print(f"amount: {lf.amount}")

# savings example with non-taxable interest
lf = LibreFinance(amount=0, currency='KRW')
print(lf.calculate_savings(month=6, monthly_deposit=1000000, is_tax=False, annual_interest_rate=3.5))
print(f"amount: {lf.amount}")
