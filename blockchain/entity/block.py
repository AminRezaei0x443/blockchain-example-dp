from blockchain.entity.hashable import Hashable
from blockchain.entity.transaction import Transaction
from blockchain.entity.util import dict_hash


class Block(Hashable):
    previous_hash: str
    seq_no: int
    transactions: list[Transaction]
    signatures: dict[int, str]

    def compute_hash(self) -> str:
        data = {
            "previous_hash": self.previous_hash,
            "seq_no": self.seq_no,
            "transactions_hash": [t.compute_hash() for t in self.transactions],
            "sigs": self.signatures,
        }
        return dict_hash(data)
