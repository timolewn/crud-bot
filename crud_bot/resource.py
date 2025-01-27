from abc import ABC, abstractmethod
from typing import TypeVar

Identifier = TypeVar("Identifier", int, str)
T = TypeVar("T", bound="Resource")


class Resource(ABC):
    """Base class for all resources."""

    id: Identifier

    @abstractmethod
    def to_dict(self) -> dict:
        """Convert the resource to a dictionary."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_dict(cls: type[T], data: dict) -> T:
        """Create a resource from a dictionary."""
        raise NotImplementedError
