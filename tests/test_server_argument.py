#!/usr/bin/env python3
"""
Test script to verify --server argument functionality works correctly
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import AIAgent
import argparse

def test_server_argument():
    """Test that --server argument properly configures the Ollama client"""
    
    print("Testing --server argument functionality...")
    print("=" * 50)
    
    # Test 1: Default client (no server specified)
    print("\n1. Testing default client (no server):")
    agent_default = AIAgent()
    default_url = str(agent_default.client._client.base_url)
    print(f"   Default client base_url: {default_url}")
    assert "127.0.0.1:11434" in default_url or "localhost:11434" in default_url
    print("   ✅ Default client configured correctly")
    
    # Test 2: Custom server
    print("\n2. Testing custom server:")
    custom_server = "http://remote-host:11434"
    agent_custom = AIAgent(server=custom_server)
    custom_url = str(agent_custom.client._client.base_url)
    print(f"   Custom client base_url: {custom_url}")
    assert custom_server in custom_url
    print("   ✅ Custom server client configured correctly")
    
    # Test 3: Different port
    print("\n3. Testing different port:")
    different_port = "http://localhost:8080"
    agent_port = AIAgent(server=different_port)
    port_url = str(agent_port.client._client.base_url)
    print(f"   Different port client base_url: {port_url}")
    assert "8080" in port_url
    print("   ✅ Different port client configured correctly")
    
    # Test 4: Command line argument parsing
    print("\n4. Testing command line argument parsing:")
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="qwen3:4b")
    parser.add_argument("--server", default=None)
    
    # Simulate command line args
    test_args = ["--server", "http://test-server:11434"]
    args = parser.parse_args(test_args)
    
    agent_cli = AIAgent(model=args.model, server=args.server)
    cli_url = str(agent_cli.client._client.base_url)
    print(f"   CLI args client base_url: {cli_url}")
    assert "test-server:11434" in cli_url
    print("   ✅ Command line argument parsing works correctly")
    
    print("\n" + "=" * 50)
    print("🎉 All server argument tests passed!")
    return True

if __name__ == "__main__":
    test_server_argument()