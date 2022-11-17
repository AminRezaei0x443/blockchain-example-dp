from blockchain.entity.transaction import Transaction


class Ledger:
    balances: dict[str, int]

    def __init__(self) -> None:
        self.balances = {}

    def can_spend(self, user, amount) -> bool:
        return self.balances[user] >= amount

    def is_valid(self, tx: Transaction) -> bool:
        return self.can_spend(tx.origin, tx.value)
