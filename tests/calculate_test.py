from libre_finance.app import LibreFinance


def test_calculates_correct_deposit_with_tax():
    finance = LibreFinance(1000000, 'KRW')
    result = finance.calculate_deposit(12, 3.0, is_tax=True, is_pretty=False)
    assert result == 25380


def test_calculates_correct_deposit_without_tax():
    finance = LibreFinance(1000000, 'KRW')
    result = finance.calculate_deposit(12, 3.0, is_tax=False, is_pretty=False)
    assert result == 30000


def test_calculates_correct_savings_with_tax():
    finance = LibreFinance(0, 'KRW')
    result = finance.calculate_savings(12, 3.0, 100000, is_tax=True, is_pretty=False)
    assert result == 16494


def test_calculates_correct_savings_without_tax():
    finance = LibreFinance(0, 'KRW')
    result = finance.calculate_savings(12, 3.0, 100000, is_tax=False, is_pretty=False)
    assert result == 19500


def test_calculates_correct_deposit_with_pretty_format():
    finance = LibreFinance(1000000, 'KRW')
    result = finance.calculate_deposit(12, 3.0, is_tax=True, is_pretty=True)
    assert result == '25,380'


def test_calculates_correct_savings_with_pretty_format():
    finance = LibreFinance(0, 'KRW')
    result = finance.calculate_savings(12, 3.0, 100000, is_tax=True, is_pretty=True)
    assert result == '16,494'
