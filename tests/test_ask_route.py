from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


@patch("app.services.rag_pipeline.call_llm")
def test_ask_question(mock_llm_call):
    """
    Test the /ask endpoint to ensure it correctly processes a question and returns an answer.
    """
    mock_llm_call.return_value = "Mocked answer based on the provided context."

    response = client.post(
        "/ask",
        json={"user_id": "u001", "query": "What are the risks of high blood pressure?"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["answer"] == "Mocked answer based on the provided context."
