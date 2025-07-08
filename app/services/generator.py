"""
This module provides a function to call a local LLM (Large Language Model) API.
It sends a prompt to the LLM and returns the generated response."""

import os
import requests
from typing import List, Dict
from dotenv import load_dotenv
load_dotenv()




def call_llm(messages: List[Dict[str, str]]) -> str:
    """
    Call either the local Ollama LLM or the online DeepSeek API based on env config.

    Args:
        messages (List[Dict[str, str]]): List of messages with role and content.

    Returns:
        str: The LLM response.
    """

    print(">>> LLM received messages:", messages)

    use_online = os.getenv("USE_ONLINE_LLM", "true").lower() == "true"

    if use_online:
        # Call the online API (by default, DeepSeek)
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError("Missing LLM_API_KEY in environment variables.")
        

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": messages,
            "stream": False
        }

        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    else:
        # Call the local Ollama LLM
        llm_url = os.getenv("LLM_URL", "http://localhost:11434/api/chat")
        payload = {
            "model": "llama3",
            "messages": messages,
            "stream": False,
        }

        response = requests.post(llm_url, json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"]
