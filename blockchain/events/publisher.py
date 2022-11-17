from typing import Callable, TypeVar

from blockchain.events.observer import Observer

T = TypeVar("T")


class Publisher:
    observers: dict[str, list[Observer, Callable]] = {}

    @classmethod
    def subscribe(cls, event: str, observer: Observer[T] | Callable):
        o_list = cls.observers.get(event, [])
        o_list.append(observer)
        cls.observers[event] = o_list

    @classmethod
    def send(cls, event: str, data):
        for observer in cls.observers.get(event, []):
            observer(event, data)
