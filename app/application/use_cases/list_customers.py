from app.domain.customer import Customer, CustomerRepository

class ListCustomersUseCase:
    def __init__(self, repository: CustomerRepository) -> None:
        self._repository = repository

    def execute(self) -> list[Customer]:
        return self._repository.list_customers()
