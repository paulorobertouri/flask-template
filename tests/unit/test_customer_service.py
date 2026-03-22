from app.repositories.customer_repository import InMemoryCustomerRepository
from app.services.customer_service import CustomerService


def test_list_customers_returns_data() -> None:
    service = CustomerService(repository=InMemoryCustomerRepository())

    customers = service.list_customers()

    assert len(customers) >= 2
    assert customers[0].email.endswith("@example.com")
