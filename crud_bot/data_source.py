from abc import abstractmethod
from typing import List, Protocol, Optional

from crud_bot.resource import T, Identifier


class DataSource(Protocol[T, Identifier]):
    """Protocol defining data source operations."""

    @abstractmethod
    def create(self, resource: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def read(self, resource_id: Identifier) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def update(self, resource_id: Identifier, resource: T) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, resource_id: Identifier) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[T]:
        raise NotImplementedError
