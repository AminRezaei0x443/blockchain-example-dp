import random

from blockchain.consensus.consensus_strategy import ConsensusStrategy
from blockchain.entity.block import Block


class PoS(ConsensusStrategy):
    def __init__(self, peers: dict[int, int]) -> None:
        self.peers = peers

    def next_leader(self) -> int:
        pop = list(self.peers.keys())
        weights_sum = sum(self.peers.values())
        weights = [k / weights_sum for k in self.peers.values()]
        chosen_one = random.choices(pop, weights=weights, k=1)
        return chosen_one

    def validate_block(self, block: Block):
        # block.validate()
        return True
