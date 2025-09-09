class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }


class UserRequest:
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            email=data.get("email"),
        )
