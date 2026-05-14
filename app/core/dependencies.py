from functools import lru_cache

from app.application.use_cases.list_customers import ListCustomersUseCase
from app.infrastructure.repositories.sqlite_customer_repository import (
    SQLiteCustomerRepository,
)
from app.services.auth_service import AuthService


@lru_cache
def get_auth_service() -> AuthService:
    return AuthService()


@lru_cache
def get_customer_repository() -> SQLiteCustomerRepository:
    return SQLiteCustomerRepository()


def get_list_customers_use_case() -> ListCustomersUseCase:
    return ListCustomersUseCase(repository=get_customer_repository())
