from abc import ABC, abstractmethod
from typing import Optional, AsyncIterator, Dict


class User(ABC):
    @property
    @abstractmethod
    def id(self) -> int:  # pylint: disable=invalid-name
        pass

    @property
    def name(self) -> str:
        pass


class Message(ABC):
    @abstractmethod
    async def delete(self) -> None:
        pass

    @property
    @abstractmethod
    def author(self) -> User:
        pass

    @property
    @abstractmethod
    def content(self) -> str:
        pass


class Channel(ABC):
    @abstractmethod
    async def history(self, limit: Optional[int] = None) -> AsyncIterator[Message]:
        if False: #pylint: disable=using-constant-test
            yield None


class Emoji(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Counter(ABC):
    @abstractmethod
    async def increment(self, counter_set: str, key: str) -> None:
        pass

    @abstractmethod
    async def decrement(self, counter_set: str, key: str) -> None:
        pass

    @abstractmethod
    async def top(self, counter_set: str, start: int, stop: int) -> Dict[str, int]:
        pass
