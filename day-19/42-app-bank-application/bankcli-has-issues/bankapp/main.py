import typer
from . import db
from rich import print   # Installation -> python -m pip install rich Reference -> https://github.com/Textualize/rich
                         # Test -> python -m rich
app = typer.Typer()

@app.command()
def create(name: str):
    acc = db.create_account(name)
    print(f"[green]Account created[/green]: ID={acc.account_id}, Name={acc.name}, Balance=${acc.balance:.2f}")

@app.command()
def deposit(account_id: str, amount: float):
    acc = db.get_account(account_id)
    acc.deposit(amount)
    print(f"[blue]Deposited ${amount:.2f}[/blue] to {acc.name}'s account. New balance: ${acc.balance:.2f}")

@app.command()
def withdraw(account_id: str, amount: float):
    acc = db.get_account(account_id)
    acc.withdraw(amount)
    print(f"[red]Withdrew ${amount:.2f}[/red] from {acc.name}'s account. New balance: ${acc.balance:.2f}")

@app.command()
def update(account_id: str, name: str):
    acc = db.update_account(account_id, name)
    print(f"[yellow]Updated account[/yellow]: ID={acc.account_id}, New name={acc.name}")

@app.command()
def show(account_id: str):
    acc = db.get_account(account_id)
    print(f"[cyan]Account Info[/cyan]: ID={acc.account_id}, Name={acc.name}, Balance=${acc.balance:.2f}")

@app.command()
def list_all():
    accs = db.all_accounts()
    print(accs)
    for acc in accs:
        print(f"- ID={acc.account_id}, Name={acc.name}, Balance=${acc.balance:.2f}")

if __name__ == "__main__":
    app()
