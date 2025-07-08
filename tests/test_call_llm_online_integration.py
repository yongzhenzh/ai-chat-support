import os
from unittest.mock import patch
from app.services.generator import call_llm

@patch("app.services.generator.requests.post")
@patch.dict(os.environ, {"USE_ONLINE_LLM": "false"})
def test_call_llm_online_integration(mock_post):
    """
    Integration-style test for call_llm using the online DeepSeek API path.
    """
    # Set env to trigger online LLM path
    os.environ["USE_ONLINE_LLM"] = "true"
    os.environ["LLM_API_KEY"] = "dummy-key"

    # Mocked DeepSeek-like API response
    mock_post.return_value.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": "This is a simulated DeepSeek response."
                }
            }
        ]
    }
    mock_post.return_value.raise_for_status = lambda: None

    messages = [
        {"role": "system", "content": "System message"},
        {"role": "user", "content": "Hello!"}
    ]

    # Act
    result = call_llm(messages)

    # Assert
    assert isinstance(result, str)
    assert "simulated DeepSeek" in result
