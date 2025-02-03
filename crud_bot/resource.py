from abc import ABC, abstractmethod
from typing import TypeVar, Generic


Identifier = TypeVar("Identifier", contravariant=True, bound=int | str)
T = TypeVar("T", bound="Resource")


class Resource(ABC, Generic[Identifier]):
    """Base class for all resources."""

    id: Identifier

    def __init__(self, id):
        self.id = id

    @abstractmethod
    def to_dict(self) -> dict:
        """Convert the resource to a dictionary."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_dict(cls: type[T], data: dict) -> T:
        """Create a resource from a dictionary."""
        raise NotImplementedError
