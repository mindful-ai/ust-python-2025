from typing import Dict, Optional          # Reference -> https://docs.python.org/3/library/typing.html
from .models import Account      
import uuid

accounts: Dict[str, Account] = {}

def create_account(name: str) -> Account:
    account_id = str(uuid.uuid4())[:8]
    acc = Account(account_id=account_id, name=name)
    accounts[account_id] = acc
    return acc

def get_account(account_id: str) -> Account:
    if account_id not in accounts:
        raise ValueError("Account not found.")
    return accounts[account_id]

def update_account(account_id: str, name: Optional[str] = None):
    acc = get_account(account_id)
    if name:
        acc.name = name
    return acc

def all_accounts():
    return list(accounts.values())
