from crud_bot.resource import Resource


class TestResource(Resource[str]):
    name: str
    description: str

    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    def update_from(self, other: "TestResource"):
        self.name = other.name
        self.description = other.description

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "description": self.description}

    @classmethod
    def from_dict(cls, data: dict) -> "TestResource":
        return cls(id=data["id"], name=data["name"], description=data["description"])
