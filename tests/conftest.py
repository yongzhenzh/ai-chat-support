import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """
    Fixture to create a TestClient for the FastAPI application.

    Returns:
        TestClient: A client for testing the FastAPI application.
    """
    return TestClient(app)
