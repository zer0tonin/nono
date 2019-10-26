from abc import ABC, abstractmethod
from typing import Optional, AsyncIterator


class User(ABC):
    @property
    @abstractmethod
    def id(self) -> int:  # pylint: disable=invalid-name
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
        if False:
            yield None
