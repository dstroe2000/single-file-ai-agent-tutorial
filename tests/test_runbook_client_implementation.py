#!/usr/bin/env python3
"""
Test script to verify all runbook files work with the new Client-based approach
"""

import sys
import os
import subprocess
import tempfile

def test_runbook_file(file_path, has_server_param=False):
    """Test that a runbook file can be imported and instantiated"""
    print(f"\nTesting {os.path.basename(file_path)}...")
    
    try:
        # Import the module
        sys.path.insert(0, os.path.dirname(file_path))
        module_name = os.path.basename(file_path)[:-3]  # Remove .py
        module = __import__(module_name)
        
        # Create an agent instance
        if has_server_param:
            # Test both default and custom server
            agent_default = module.AIAgent()
            agent_custom = module.AIAgent(server="http://test-server:11434")
            
            print(f"   ✅ Default client: {type(agent_default.client)}")
            print(f"   ✅ Custom server client: {type(agent_custom.client)}")
            
            # Check client configuration
            default_url = str(agent_default.client._client.base_url)
            custom_url = str(agent_custom.client._client.base_url)
            
            assert "127.0.0.1:11434" in default_url or "localhost:11434" in default_url
            assert "test-server:11434" in custom_url
            
            print(f"   ✅ Client URLs configured correctly")
        else:
            agent = module.AIAgent()
            print(f"   ✅ Agent created: {type(agent.client)}")
            
            # Check client configuration
            client_url = str(agent.client._client.base_url)
            assert "127.0.0.1:11434" in client_url or "localhost:11434" in client_url
            print(f"   ✅ Client URL configured correctly")
        
        print(f"   ✅ {os.path.basename(file_path)} passed all tests")
        return True
        
    except Exception as e:
        print(f"   ❌ {os.path.basename(file_path)} failed: {e}")
        return False
    finally:
        # Clean up
        if module_name in sys.modules:
            del sys.modules[module_name]
        if os.path.dirname(file_path) in sys.path:
            sys.path.remove(os.path.dirname(file_path))

def main():
    """Test all runbook files"""
    print("Testing Client-based implementation in runbook files...")
    print("=" * 60)
    
    base_dir = "/media/daniels/data/work/single-file-ai/single-file-ai-agent-tutorial"
    
    # Files to test and whether they have server parameters
    test_files = [
        ("runbook/05_add_chat_method.py", False),
        ("runbook/06_create_interactive_cli.py", True),
        ("runbook/07_add_personality.py", True),
    ]
    
    all_passed = True
    
    for file_path, has_server in test_files:
        full_path = os.path.join(base_dir, file_path)
        if not test_runbook_file(full_path, has_server):
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All runbook files passed Client implementation tests!")
    else:
        print("❌ Some runbook files failed tests")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)