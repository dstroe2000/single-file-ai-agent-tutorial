#!/usr/bin/env python3
"""
Verification script to check that all runbook files have been successfully migrated from Anthropic to Ollama.
"""

import os
import re
from pathlib import Path

def check_file_migration(filepath):
    """Check if a file has been properly migrated from Anthropic to Ollama"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check for Anthropic imports
    if 'from anthropic import' in content or 'import anthropic' in content:
        issues.append("❌ Still has Anthropic imports")
    
    # Check for ollama import
    if 'import ollama' not in content and 'anthropic' not in os.path.basename(filepath).lower():
        # Some basic files might not need ollama import
        if any(keyword in content for keyword in ['AIAgent', 'chat', 'tools']):
            issues.append("❌ Missing ollama import")
    
    # Check for Anthropic API key references
    if 'ANTHROPIC_API_KEY' in content:
        issues.append("❌ Still references ANTHROPIC_API_KEY")
    
    # Check for Claude model references
    if 'claude-sonnet' in content:
        issues.append("❌ Still references Claude model")
    
    # Check for Anthropic client usage
    if 'self.client = Anthropic' in content:
        issues.append("❌ Still initializes Anthropic client")
    
    # Check for old tool schema format
    if '"input_schema"' in content and '"type": "function"' not in content and 'Tool(' in content:
        issues.append("⚠️  Might be using old tool schema format")
    
    # Check for proper model usage
    if 'def __init__' in content and 'model:' in content:
        if 'qwen3:4b' not in content:
            issues.append("⚠️  Might not be using qwen3:4b as default")
    
    return issues

def main():
    print("🔍 Checking Ollama migration status for all runbook files...\n")
    
    # Get the project root directory (parent of tests folder)
    project_root = Path(__file__).parent.parent
    runbook_dir = project_root / "runbook"
    
    all_good = True
    
    for py_file in sorted(runbook_dir.glob("*.py")):
        print(f"📁 Checking {py_file.name}...")
        issues = check_file_migration(py_file)
        
        if not issues:
            print("   ✅ Migration looks good!")
        else:
            all_good = False
            for issue in issues:
                print(f"   {issue}")
        print()
    
    print("="*50)
    if all_good:
        print("🎉 All runbook files have been successfully migrated to Ollama!")
        print("\n💡 To test the migration:")
        print("   1. Make sure Ollama is running: ollama serve")
        print("   2. Pull the model: ollama pull qwen3:4b")
        print("   3. Test any runbook file: uv run runbook/07_add_personality.py")
    else:
        print("⚠️  Some files still need attention. Please review the issues above.")
    
    print("\n🔧 Files ready to use:")
    for py_file in sorted(runbook_dir.glob("*.py")):
        issues = check_file_migration(py_file)
        if not issues:
            print(f"   ✅ {py_file.name}")

if __name__ == "__main__":
    main()