from abc import ABC, abstractmethod

from blockchain.entity.block import Block


class BlockDB(ABC):
    @abstractmethod
    def append(self, block: Block):
        pass

    @abstractmethod
    def last_block(self) -> Block:
        pass
