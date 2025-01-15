# LibreFinance

LibreFinance is a combination of the words "libre" and "finance". 

This tool helps financial consumers freely utilize financial services by interest calculating.

##  Important Notice

> In South Korea, the general interest income tax rate is 15.4% (14% interest income tax + 1.4% local tax). Please be aware of this when using the tool.

## Usage

1. Install the library using `pip install libre-finance`.
2. Import the library with `from libre_finance import LibreFinance`.

## Example

```python
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
```

## Features

- Deposit interest (taxable/non-taxable)
- Savings interest (taxable/non-taxable)


- sql query

if you want to use sql feature, you can install the library with the following command.

```bash
pip install libre-finance[sql]
```

```python
from libre_finance.database import MariaDBTable

t = MariaDBTable(db_name='db', user='user', passwd='passwd', host='127.0.0.1', port=3306)
```

and you can use the sql command as follows.

```sql
SELECT *
FROM `finance`
where product = "deposit" and month = 6
order by total_interest desc
limit 5;
```

## ToDo List

- Bond interest
- RP interest

## License

MIT
