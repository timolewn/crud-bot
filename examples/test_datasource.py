from typing import Optional, List
from examples.test_resource import TestResource
from crud_bot.data_source import DataSource


class TestDataSource(DataSource[TestResource]):
    def __init__(self, name: str):
        self.data: List[TestResource] = []
        self.name = name

    def create(self, resource: TestResource) -> TestResource:
        self.data.append(resource)
        return resource

    def read(self, resource_id: str) -> Optional[TestResource]:
        return next((x for x in self.data if x.id == resource_id), None)

    def update(
        self, resource_id: str, resource: TestResource
    ) -> Optional[TestResource]:
        test = next((x for x in self.data if x.id == resource_id), None)
        if test is None:
            return None
        test.update_from(resource)
        return test

    def delete(self, resource_id: str) -> bool:
        test = next((x for x in self.data if x.id == resource_id), None)
        if test is None:
            return False
        self.data.remove(test)
        return True

    def list_all(self) -> List[TestResource]:
        return self.data
