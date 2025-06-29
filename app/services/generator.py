"""
This module provides a function to call a local LLM (Large Language Model) API.
It sends a prompt to the LLM and returns the generated response."""

import os
import requests
from typing import List, Dict


def call_local_llm(messages: List[Dict[str, str]]) -> str:
    """
    Call the local LLM API with the given message history (multi-turn).

    Args:
        messages (List[Dict[str, str]]): List of messages with role and content.

    Returns:
        str: The LLM response.
    """

    print(">>> LLM received messages:", messages)
    LLM_API_URL = os.getenv("LLM_URL", "http://localhost:11434/api/chat")

    payload = {
        "model": "llama3",
        "messages": messages,
        "stream": False,
    }

    response = requests.post(LLM_API_URL, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]
