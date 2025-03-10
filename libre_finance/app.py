import math
from typing import Type

from libre_finance.constants import KRW_INTEREST_TAX, USD_INTEREST_TAX
from libre_finance.database.spec import FinanceData


class LibreFinance:
    def __init__(self, amount: int, currency: str = 'KRW'):
        self.amount: int = amount
        self.original_amount: int = amount
        self.currency: str = currency
        self.total_interest: int = 0
        # set interest tax
        if currency == 'KRW':
            self.interest_tax: float = KRW_INTEREST_TAX
        else:
            self.interest_tax: float = USD_INTEREST_TAX
        self.history: Type[FinanceData] = FinanceData

    def calculate_deposit(self, month: int, annual_interest_rate: float = 0.0, is_tax: bool = True,
                          is_pretty: bool = True) -> str | int:
        # calculate monthly interest
        interest_rate = annual_interest_rate / 12
        for _ in range(month):
            # calculate interest for each month
            interest = math.floor(self.amount * interest_rate / 100)
            if is_tax:
                # calculate interest tax
                interest *= 1 - self.interest_tax / 100
            self.total_interest += interest
        return_interest = math.floor(self.total_interest)
        self.amount += return_interest
        # saving history
        self.history = FinanceData(
            product='deposit',
            origin_amount=self.original_amount,
            month=month,
            amount=self.amount,
            total_interest=self.total_interest,
            interest_rate=annual_interest_rate,
            interest_tax=self.interest_tax,
            is_tax=is_tax,
            currency=self.currency)
        if is_pretty:
            return f'{return_interest:,}'
        else:
            return return_interest

    def calculate_savings(self, month: int, annual_interest_rate: float = 0.0, monthly_deposit: int = 0,
                          is_tax: bool = True, is_pretty: bool = True) -> str | int:
        # calculate monthly interest
        interest_rate = annual_interest_rate / 12
        self.amount += monthly_deposit
        for _ in range(month):
            # calculate interest for each month
            interest = math.ceil(self.amount * interest_rate / 100)
            if is_tax:
                # calculate interest tax
                interest *= 1 - self.interest_tax / 100
            self.total_interest += math.floor(interest)
            self.amount += monthly_deposit
        return_interest = math.floor(self.total_interest)
        self.amount += return_interest - monthly_deposit
        # saving history
        self.history = FinanceData(
            product='savings',
            origin_amount=self.original_amount,
            month=month,
            amount=self.amount,
            total_interest=self.total_interest,
            interest_rate=annual_interest_rate,
            interest_tax=self.interest_tax,
            is_tax=is_tax,
            currency=self.currency,
            monthly_deposit=monthly_deposit)
        if is_pretty:
            return f'{return_interest:,}'
        else:
            return return_interest
