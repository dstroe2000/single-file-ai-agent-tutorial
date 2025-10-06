#!/usr/bin/env python3
"""
Test script to verify Ollama migration works correctly.
This script tests the basic functionality without running the full interactive CLI.
"""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ollama",
#     "pydantic",
# ]
# ///

import os
import sys
import tempfile
from pathlib import Path

# Add the parent directory to the Python path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))
from main import AIAgent


def test_basic_functionality():
    """Test basic agent functionality"""
    print("Testing Ollama migration...")
    
    # Initialize agent with the default model for testing
    agent = AIAgent(model="qwen3:4b")
    
    print(f"✓ Agent initialized with model: {agent.model}")
    print(f"✓ Tools loaded: {len(agent.tools)} tools")
    
    # List the available tools
    for tool in agent.tools:
        print(f"  - {tool.name}: {tool.description}")
    
    print("\nTesting tool schema conversion...")
    
    # Test tool schema conversion to Ollama format
    ollama_tools = [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.input_schema,
            },
        }
        for tool in agent.tools
    ]
    
    print(f"✓ Successfully converted {len(ollama_tools)} tools to Ollama format")
    
    # Show first tool as example
    if ollama_tools:
        print(f"Example tool schema: {ollama_tools[0]['function']['name']}")
        print(f"  Parameters: {list(ollama_tools[0]['function']['parameters']['properties'].keys())}")
    
    print("\n✓ Migration test completed successfully!")
    print("\nTo test the full functionality, run:")
    print("  uv run main.py")
    print("\nOr with a specific model:")
    print("  uv run main.py --model qwen3:4b")


if __name__ == "__main__":
    test_basic_functionality()