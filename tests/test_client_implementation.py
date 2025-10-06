#!/usr/bin/env python3
"""
Simple test to verify the Ollama Client implementation works correctly.
"""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ollama",
#     "pydantic",
# ]
# ///

import sys
from pathlib import Path

# Add the parent directory to the Python path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))
from main import AIAgent

def test_client_initialization():
    """Test that the AIAgent initializes correctly with and without server"""
    print("Testing AIAgent initialization...")
    
    # Test local client
    print("✓ Testing local client initialization...")
    agent_local = AIAgent()
    print(f"  Local client type: {type(agent_local.client)}")
    
    # Test remote client
    print("✓ Testing remote client initialization...")
    agent_remote = AIAgent(server="http://localhost:11434")
    print(f"  Remote client type: {type(agent_remote.client)}")
    print(f"  Remote client host: {getattr(agent_remote.client, '_host', 'unknown')}")
    
    print("✓ Client initialization tests passed!")

if __name__ == "__main__":
    test_client_initialization()