# Single-File AI Agent Tutorial

Build a complete AI agent in ~220 lines of Python. No frameworks, no complexity. Just clean code that shows exactly how agents work.

This tutorial demonstrates a working agent that can read, write, and edit files through natural conversation with Ollama. Everything runs from a single Python file using `uv`'s inline dependencies: no virtual environments, no pip installs, no dependency conflicts.

You'll understand how AI agents parse responses, execute tools, and maintain conversation context. The mechanics laid bare, without abstractions.

## Credits

This repository is forked from Dave Ebbelaar's implementation: [Single-File AI Agent Tutorial](https://github.com/daveebbelaar/single-file-ai-agent-tutorial).

Dave Ebbelaar's implementation is also based on the following sources:
- It is forked from Francis Beeson's implementation: [Single-File AI Agent Tutorial](https://github.com/leobeeson/single-file-ai-agent-tutorial)
- Which code is based on the tutorial by Thorsten Ball in ["How to Build an Agent"](https://ampcode.com/how-to-build-an-agent) from ampcode.com

Thank you, all: Dave, Francis, and Thorsten!

## 📋 Migration Note
 
This repository has been migrated from Anthropic's Claude API to Ollama for local execution. See [docs/MIGRATION_SUMMARY.md](docs/MIGRATION_SUMMARY.md) for detailed migration information.

## Features

- Single-file execution.
- No virtual environment or manual dependency installation required (except for `uv`).
- The AI agent can:
  - Read file contents.
  - List directory contents.
  - Edit existing files or create new ones.
- Interactive chat interface.
- Error handling and feedback.
- Logging of agent tool usage.

## Requirements

- `uv` package manager (see installation instructions below)
- Python 3.12 or higher (though `uv` will [handle this automatically](https://docs.astral.sh/uv/concepts/python-versions/))
- Ollama installed and running locally (see installation instructions below)

## Installing uv

`uv` is an extremely fast Python package manager that simplifies running Python scripts with inline dependencies.

It allows you to run Python scripts [without needing to create a virtual environment or manually install dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

To [install](https://docs.astral.sh/uv/getting-started/installation/) `uv`::

### Linux/macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, verify it's working:

```bash
uv --version
```

## Installing Ollama

Ollama allows you to run large language models locally on your machine.

### Linux/macOS

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Windows

Download and install from [ollama.com](https://ollama.com/download)

After installation, start Ollama and pull the default model:

```bash
ollama serve  # Start the Ollama server (runs in background)
ollama pull qwen3:4b  # Pull the default model (or any other model you prefer)
```

## Running the Agent

1. Make sure Ollama is running:

```bash
ollama serve
```

2. Run the agent:

```bash
uv run main.py
```

You can specify a different model with the `--model` argument:

```bash
uv run main.py --model qwen3:4b
```

The agent leverages uv's inline dependencies handling from the script headers, so no manual dependency installation is needed.

## Project Structure

```
├── main.py                    # Main AI agent application
├── runbook/                   # Tutorial progression files
│   ├── 01_basic_script.py    # Basic script setup
│   ├── 02_agent_class.py     # Agent class definition
│   ├── 03_define_tools.py    # Tool definitions
│   ├── 04_implement_tool_execution.py  # Tool execution
│   ├── 05_add_chat_method.py # Chat functionality
│   ├── 06_create_interactive_cli.py    # Interactive CLI
│   └── 07_add_personality.py # Full implementation with logging
├── tools/                     # Individual tool implementations
├── tests/                     # Test and verification scripts
│   ├── test_ollama_migration.py       # Basic migration test
│   └── verify_runbook_migration.py    # Comprehensive verification
└── docs/                      # Documentation
    └── MIGRATION_SUMMARY.md   # Detailed migration information
```

## Testing

Verify the migration and functionality:

```bash
# Test basic functionality
uv run tests/test_ollama_migration.py

# Verify all runbook files
python tests/verify_runbook_migration.py

# Test individual runbook files
uv run runbook/07_add_personality.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
