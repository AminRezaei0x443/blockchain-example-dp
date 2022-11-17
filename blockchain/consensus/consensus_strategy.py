from abc import ABC, abstractmethod

from blockchain.entity.block import Block


class ConsensusStrategy(ABC):
    @abstractmethod
    def next_leader(self) -> int:
        pass

    @abstractmethod
    def validate_block(self, block: Block) -> bool:
        pass
