from app.domain.customer import Customer
from app.repositories.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def list_customers(self) -> list[Customer]:
        return self._repository.list_customers()
