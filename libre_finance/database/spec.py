from dataclasses import dataclass


# Define the finance data structure
@dataclass
class FinanceData:
    origin_amount: int
    product: str
    month: int
    amount: int
    total_interest: int
    interest_rate: float
    interest_tax: float
    is_tax: bool
    # monthly_deposit is optional
    monthly_deposit: int = None
    currency: str = "KRW"
