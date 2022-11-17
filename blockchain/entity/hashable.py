from abc import ABC, abstractmethod


class Hashable(ABC):
    @abstractmethod
    def compute_hash(self) -> str:
        pass
