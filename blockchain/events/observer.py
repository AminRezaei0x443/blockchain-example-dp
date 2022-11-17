from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Observer(Generic[T], ABC):
    @abstractmethod
    def observe(self, data: T):
        pass

    def __call__(self, *args):
        return self.observe(*args)
