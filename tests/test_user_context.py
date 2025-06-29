"""
ai-chat-support/tests/test_user_context.py
This module contains unit tests for the user context retrieval functionality.
It tests the get_user_context function to ensure it retrieves the correct user context based on user IDs
and handles cases where the user ID does not exist.
"""

from app.services.get_user_context import get_user_context


def test_get_user_context_valid_id():
    user_id = "u001"
    context = get_user_context(user_id)

    assert isinstance(context, str)
    assert "diabetes" in context.lower()


def test_get_user_context_invalid_id():
    user_id = "invalid_id"
    context = get_user_context(user_id)

    assert isinstance(context, str)
    assert "User context not found." in context
