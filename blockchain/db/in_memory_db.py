from blockchain.db.block_db import BlockDB
from blockchain.entity.block import Block


class InMemoryDB(BlockDB):
    blocks: list[Block]

    def __init__(self) -> None:
        self.blocks = []

    def append(self, block: Block):
        self.blocks.append(block)

    def last_block(self) -> Block:
        return self.blocks[len(self.blocks) - 1]

    def checkpoint(self, path: str):
        pass

    def load_checkpoint(self, path: str):
        pass

    def __iter__(self):
        return iter(self.blocks)
