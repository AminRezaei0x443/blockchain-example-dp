from blockchain.entity.hashable import Hashable
from blockchain.entity.util import dict_hash


class Transaction(Hashable):
    origin: str
    destination: str
    value: int
    timestamp: int

    def compute_hash(self) -> str:
        data = {
            "origin": self.origin,
            "destination": self.destination,
            "value": self.value,
            "timestamp": self.timestamp,
        }
        return dict_hash(data)
