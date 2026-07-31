import pytest


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API."""
    return "https://reqres.in/api"


@pytest.fixture(scope="function")
def user_data():
    """Тестовые данные для создания пользователя."""
    return {
        "name": "morpheus",
        "job": "leader"
    }
