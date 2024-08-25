from app6 import BankAccount
from decimal import Decimal
import pytest


def test_bank_account_creation():
    bank_account = BankAccount(Decimal('123.45'))
    assert bank_account.current_balance == Decimal('123.45')


def test_bank_account_deposit():
    bank_account = BankAccount(Decimal('100'))
    bank_account.deposit(Decimal('123.45'))

    assert bank_account.current_balance == Decimal('223.45')

    with pytest.raises(ValueError):
        bank_account.deposit(Decimal('-123.45'))


def test_bank_account_withdraw():
    bank_account = BankAccount(Decimal('100'))
    bank_account.withdraw(Decimal('50'))

    assert bank_account.current_balance == Decimal('50')

    with pytest.raises(ValueError):
        bank_account.withdraw(Decimal('-123.45'))

    with pytest.raises(ValueError):
        bank_account.withdraw(Decimal('51'))


