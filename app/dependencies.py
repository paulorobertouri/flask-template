from functools import lru_cache

from app.repositories.customer_repository import InMemoryCustomerRepository
from app.services.auth_service import AuthService
from app.services.customer_service import CustomerService


@lru_cache
def get_customer_service() -> CustomerService:
    return CustomerService(repository=InMemoryCustomerRepository())


@lru_cache
def get_auth_service() -> AuthService:
    return AuthService()
