# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ollama", # type: ignore
#     "pydantic",
# ]
# ///

import os
import sys
from typing import List, Dict, Any
import ollama
from pydantic import BaseModel


class Tool(BaseModel):
    name: str
    description: str
    input_schema: Dict[str, Any]


class AIAgent:
    def __init__(self, model: str = "qwen3:4b"):
        self.model = model
        self.messages: List[Dict[str, Any]] = []
        self.tools: List[Tool] = []
        print(f"Agent initialized with model: {model}")


if __name__ == "__main__":
    agent = AIAgent()

# ```bash
# ollama serve  # Make sure Ollama is running
# ollama pull qwen3:4b  # Pull the model if not already available
# uv run runbook/02_agent_class.py
# ```
# Should print: Agent initialized
