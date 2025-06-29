from unittest.mock import patch
from app.services.generator import call_local_llm


@patch("app.services.generator.requests.post")
def test_call_local_llm(mock_post):
    """
    Test the call_local_llm function with message history.
    """
    # Arrange
    mock_response = {
        "message": {
            "role": "assistant",
            "content": "This is a mocked response from the LLM.",
        },
        "done": True,
    }

    mock_post.return_value.json.return_value = mock_response
    mock_post.return_value.raise_for_status = lambda: None

    messages = [
        {"role": "system", "content": "System prompt here."},
        {"role": "user", "content": "Hello!"},
    ]

    # Act
    response = call_local_llm(messages)

    # Assert
    assert response == "This is a mocked response from the LLM."
    mock_post.assert_called_once()
    sent_payload = mock_post.call_args[1]["json"]
    assert sent_payload["messages"] == messages
