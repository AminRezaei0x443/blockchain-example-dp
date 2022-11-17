from blockchain.events.publisher import Publisher


class Network:
    nodes: dict[int, str]

    def __init__(self) -> None:
        self.nodes = {}

    def start(self):
        # ws.start()
        pass

    def send(self, target: int, msg: dict):
        pass

    def receive(self, event: str, data):
        Publisher.send(event, data)

    def broadcast(self, msg: dict):
        for n in self.nodes:
            self.send(n, msg)

    def participants(self) -> int:
        return len(self.nodes)
