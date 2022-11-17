from blockchain.consensus.consensus_strategy import ConsensusStrategy
from blockchain.db.block_db import BlockDB
from blockchain.db.ledger import Ledger
from blockchain.entity.block import Block
from blockchain.entity.transaction import Transaction
from blockchain.events.publisher import Publisher
from blockchain.network.network import Network


class Blockchain:
    consensus_strategy: ConsensusStrategy
    block_db: BlockDB
    ledger: Ledger
    unconfirmed_block: Block = None

    def __init__(
        self,
        consensus: ConsensusStrategy,
        db: BlockDB,
        ledger: Ledger,
        network: Network,
    ) -> None:
        self.consensus_strategy = consensus
        self.block_db = db
        self.ledger = ledger
        self.network = network
        self.init_events()

    def init_events(self):
        Publisher.subscribe("new_tx", self.observe_new_tx)
        Publisher.subscribe("rcv_blk", self.observer_rcv_blk)
        Publisher.subscribe("sgn_blk", self.observe_sgn_blk)
        Publisher.subscribe("finalize_blk", self.observe_finalize_blk)

    def observe_new_tx(self, tx: Transaction):
        if self.ledger.is_valid(tx):
            if self.unconfirmed_block is None:
                self.unconfirmed_block = Block()
            self.unconfirmed_block.transactions.append(tx)
        if len(self.unconfirmed_block.transactions) >= 10:
            leader = self.consensus_strategy.next_leader()
            if leader == self._id:
                self.network.broadcast(
                    {
                        "type": "propose_block",
                        "block": self.unconfirmed_block,  # TODO: Serialize better
                    }
                )

    def observer_rcv_blk(self, block: Block):
        vote = self.consensus_strategy.receive_block(block)
        if vote:
            self.network.broadcast(
                {
                    "type": "vote_block",
                    "block": self.unconfirmed_block,  # TODO: Serialize better
                }
            )

    def observe_sgn_blk(self, signer: int, signature: str):
        # TOOD: is sig valid?
        self.unconfirmed_block.signatures[signer] = signature
        if len(self.unconfirmed_block.signatures) >= int(
            2 / 3 * self.network.participants()
        ):
            self.network.broadcast(
                {
                    "type": "finalize_blk",
                    "block": self.unconfirmed_block,  # TODO: Serialize better
                }
            )

    def observe_finalize_blk(self, block: Block):
        self.block_db.append(block)

    def run(self):
        self.network.start()
