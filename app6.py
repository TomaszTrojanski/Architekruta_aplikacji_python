from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=False)
class BankAccount:
    balance: Decimal = Decimal('0')

    def deposit(self, amount: Decimal):
        if amount <= Decimal('0'):
            raise ValueError('Kwota nie może być ujemna')
        self.balance += amount

    def withdraw(self, amount: Decimal):
        if amount <= Decimal('0'):
            raise ValueError('Saldo musi być dodatnie')

        if amount > self.balance:
            raise ValueError('Kwota musi być maksymalnie o wartości salda')

        self.balance -= amount

    @property
    def current_balance(self):
        return self.balance
