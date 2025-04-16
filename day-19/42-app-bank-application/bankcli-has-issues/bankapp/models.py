from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass               # <- Automatically insert a constructor for Account class
class Account:           # Reference -> https://docs.python.org/3/library/dataclasses.html

    account_id: str
    name: str
    balance: float = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal amount.")
        self.balance -= amount
