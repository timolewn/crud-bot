from typing import List, Generic, Optional

from crud_bot.resource import T, Identifier
from crud_bot.data_source import DataSource


class CrudManager(Generic[T]):
    """CRUD manager that operates on a data source."""

    def __init__(self, data_source: DataSource[T]):
        self.data_source = data_source

    def create(self, resource: T) -> T:
        return self.data_source.create(resource)

    def read(self, resource_id: Identifier) -> Optional[T]:
        return self.data_source.read(resource_id)

    def update(self, resource_id: Identifier, resource: T) -> Optional[T]:
        return self.data_source.update(resource_id, resource)

    def delete(self, resource_id: Identifier) -> bool:
        return self.data_source.delete(resource_id)

    def list_all(self) -> List[T]:
        return self.data_source.list_all()
