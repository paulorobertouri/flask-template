from typing import Protocol
from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str
    email: str

class CustomerRepository(Protocol):
    def list_customers(self) -> list[Customer]:
        ...
