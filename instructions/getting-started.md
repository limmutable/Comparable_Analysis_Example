# Getting Started Guide

This guide walks you through setting up your development environment for the Comparable Analysis project.

## Prerequisites

- macOS or Windows with WSL (Windows Subsystem for Linux)
- Terminal/command line access (see [instructions below](#step-2-environment-setup-wslterminal))
- **Python 3.10+** (see [Python Setup](#python-setup) below)
- Antigravity (IDE)
- A [GitHub](https://github.com/) account
- A Google AI API key (for Gemini)
- An Anthropic API key (for Claude)

## Step 1: Install Antigravity (IDE)

Antigravity is an AI-powered IDE designed to streamline financial analysis workflows.

1.  **Download**: Navigate to [antigravity.google](https://antigravity.google).
2.  **Install**: Run the installer for your operating system and follow the prompts.
3.  **Initial Setup**:
    - Choose **"Start fresh"** when prompted.
    - Select your preferred theme.
    - Ensure **"Agent assisted development"** is enabled.
    - Install the recommended extensions for Python and Markdown.
4.  **Sign In**: Sign in with your personal Google account to enable Gemini features.

## Step 2: Environment Setup (WSL/Terminal)

Before installing tools, ensure you have a working terminal environment.

### 2.1 For Windows Users (WSL)

**What is WSL?**
WSL (Windows Subsystem for Linux) lets you run a Linux environment directly on Windows. This project requires a Linux-like environment for optimal compatibility.

**How to Install/Enable:**

1. Open PowerShell as Administrator.
2. Run the command: `wsl --install`
3. Restart your computer if prompted.
4. Additional instructions can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install).

**How to Launch:**

- Press `Windows Key` and type **"Ubuntu"**.
- Click to open the terminal window.

### 2.2 For macOS Users

**How to Launch:**

- Press `Command + Space` to open Spotlight Search.
- Type **"Terminal"**.
- Press `Enter` to open the Terminal application.

## Step 3: Install Homebrew (macOS/Linux)

Homebrew is a package manager that simplifies installing software like Node.js and the Gemini CLI.

1. **Check if you have it installed**:

   ```bash
   brew --version
   ```

2. **If not installed, paste this into your terminal**:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   Follow the on-screen instructions (you may need to enter your password).

## Step 4: Install Python & uv

### 4.1 Python Setup

Check your Python version:

```bash
python3 --version
# Should be 3.10 or higher
```

**If Python is not installed or version is too old:**

```bash
# macOS (using Homebrew)
brew install python@3.12

# Ubuntu/Debian
sudo apt update && sudo apt install python3.12

# Windows WSL
sudo apt update && sudo apt install python3.12
```

### 4.2 uv Package Manager (Optional Pre-install)

`make setup` will install `uv` automatically, but you can install it manually:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation (restart terminal first)
uv --version
```

## Step 5: Download Project from GitHub

### 5.1 Clone the Repository

```bash
# Create and navigate to your projects directory
mkdir -p ~/Projects
cd ~/Projects

# Clone the repository
git clone https://github.com/limmutable/Comparable_Analysis_Example.git

# Enter the project directory
cd Comparable_Analysis_Example
```

### 5.2 Verify Project Structure

```bash
ls -la
```

You should see directories like `dataroom/`, `instructions/`, `output/`, `prompts/`, and `src/`.

---

## Step 6: Setup Python Environment

The project includes Python scripts for document processing. We use `uv` for fast, reliable package management.

### 6.1 Run Setup

```bash
cd ~/Projects/Comparable_Analysis_Example

# Full setup: installs uv (if needed), creates venv, installs dependencies
make setup
```

### 6.2 Verify Python Setup

```bash
# Run tests to verify setup
make test

# Check document sizes in dataroom
uv run python scripts/check_document_size.py dataroom/
```

> **Crucial Note:** Always use `uv run python` instead of `python` directly. This ensures the correct virtual environment and dependencies are used.

---

## Step 7: API Setup (Gemini & Claude)

Now that the project is set up, you need API keys to power the AI models.

### 7.1 Getting a Gemini API Key (Free)

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your **personal Google account** (@gmail.com).
3. Click on **"Get API key"** and then **"Create API key"**.
4. Copy and save your key securely.

### 7.2 Getting an Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/).
2. Create an account and add a small amount of credit (e.g., $5-$10).
3. Navigate to **"Get API Keys"** and create a new key.

---

## Step 8: Install & Authenticate CLIs

### 8.1 Install Gemini CLI

```bash
# macOS/Linux (Homebrew)
brew install gemini-cli

# All platforms (npm)
npm install -g gemini-chat-cli
```

### 8.2 Authenticate Gemini CLI

```bash
gemini auth login
```

### 8.3 Install Node.js (Requirement for Claude)

Claude CLI requires Node.js 18 or higher.

```bash
# Check if Node.js is installed
node --version

# If not installed, use Homebrew (macOS)
brew install node
```

### 8.4 Install & Authenticate Claude CLI

```bash
# Install Claude CLI
npm install -g @anthropic-ai/claude-code

# Start Claude to authenticate
claude
```

---

## Step 9: Verify Your Setup

### 9.1 Verify Gemini (Primary)

Start the Gemini REPL to test the connection:

```bash
gemini
```

**Try these commands inside the session:**

```text
> Hello, are you ready for financial analysis?
> /help          # Show available commands
> /clear         # Clear conversation history
> /exit          # Exit the session
```

### 9.2 Verify Claude (Optional)

Start the Claude CLI to test the connection:

```bash
claude
```

**Try these commands inside the session:**

```text
> Hello, what is 2+2?
> /help          # Show available commands
> /cost          # Show token usage and cost
> /clear         # Clear context
> /exit          # Exit the session
```

### 9.3 Verify Project Environment

```bash
# Check Python environment
make test
```

---

## Next Steps

Now that your environment is set up, you are ready to start the project:

1. **Understand the Workflow**: Read the [Analysis Workflow Guide](analysis-workflow.md) to understand the end-to-end process.
2. **Setup Your Data**: Go to [Step 0: Dataroom Setup](00-dataroom-setup.md) to add your target company's documents to the `/dataroom` directory.

---

## Troubleshooting

### Claude CLI not found

```bash
# Ensure npm global bin is in your PATH
export PATH="$PATH:$(npm config get prefix)/bin"
```

### Permission denied during install

```bash
# Use sudo (not recommended) or fix npm permissions
npm config set prefix ~/.npm-global
export PATH="$PATH:$HOME/.npm-global/bin"
```

### Skills not loading

- Ensure you're running Claude from the project root directory
- Check that `.claude/skills/` exists and contains valid `SKILL.md` files
- Restart Claude CLI after adding new skills
