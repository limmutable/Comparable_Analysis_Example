# Getting Started Guide

This guide walks you through setting up your development environment for the Comparable Analysis project.

## Prerequisites

- macOS or Windows with WSL (Windows Subsystem for Linux)
- [Homebrew](https://brew.sh/) (for macOS/Linux users)
- Terminal/command line access (see [instructions below](#step-0-environment-setup))
- A [GitHub](https://github.com/) account
- An Anthropic API key (for Claude)
  > **Note**: The $20/month Claude Pro subscription does **not** cover API usage. You need to set up a separate API account with credits.
- A Google AI API key (for Gemini)
  > **Note**: Google offers a generous **free tier** for the Gemini API that is sufficient for most student projects. You do not need a paid subscription.

---

## Step 0: Environment & API Setup

Before installing tools, ensure you have the correct environment and API keys.

### Getting a Gemini API Key (Free for Students)

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on **"Get API key"** in the sidebar.
4. Click **"Create API key"**.
5. Copy the key string. **Keep this secret.**

**Cost Note:**
- The **Free of Charge** tier allows for 15 requests per minute (RPM) and 1,500 requests per day (RPD) for Gemini 1.5 Flash, which is more than enough for this course.
- You do **not** need to enable billing or pay for the "Pay-as-you-go" tier unless you exceed these limits.

### For Windows Users (WSL)

**What is WSL?**
WSL (Windows Subsystem for Linux) lets you run a Linux environment directly on Windows, unmodified, without the overhead of a traditional virtual machine or dual-boot setup. This project requires a Linux-like environment for optimal compatibility with the tools.

**How to Install/Enable:**
1. Open PowerShell as Administrator.
2. Run the command: `wsl --install`
3. Restart your computer if prompted.
4. Additional instructions can be found [here](https://learn.microsoft.com/en-us/windows/wsl/install).

**How to Launch:**
- Press `Windows Key` and type **"Ubuntu"** (or your installed Linux distribution).
- Click to open the terminal window. This is where you will run all commands for this project.

### For macOS Users

**How to Launch:**
- Press `Command + Space` to open Spotlight Search.
- Type **"Terminal"**.
- Press `Enter` to open the Terminal application.


## Step 0.1: Install Homebrew (macOS/Linux)

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


## Step 1: Install Gemini CLI (Primary)

Gemini CLI provides access to Google's Gemini models from the terminal. This is the primary tool we will use.

### 1.1 Install Gemini CLI

You can install it using Homebrew (recommended) or npm:

**Option 1: Homebrew (macOS/Linux)**
```bash
brew install gemini-cli
```

**Option 2: npm (All Platforms)**
```bash
npm install -g gemini-chat-cli
```

### 1.2 Authenticate Gemini CLI

```bash
gemini auth login
```

Follow the prompts to authenticate with your Google account or API key.

### 1.3 Verify Installation

```bash
gemini --version
```

---

## Step 2: Install Claude CLI (Advanced/Optional)

Claude Code is an advanced command-line tool. It is optional but recommended for complex financial modeling tasks.

### 2.1 Install Node.js (if not already installed)

Claude CLI requires Node.js 18 or higher (which includes `npm`).

```bash
# Check if Node.js and npm are installed
node --version
npm --version

# If not installed, use Homebrew (macOS)
brew install node

# Or download from https://nodejs.org/
```

### 2.2 Install Claude CLI

```bash
npm install -g @anthropic-ai/claude-code
```

### 2.3 Authenticate Claude CLI

```bash
claude
```

On first run, you'll be prompted to authenticate. You can either:
- Log in with your Anthropic Console account, or
- Enter your API key directly

### 2.4 Verify Installation

```bash
claude --version
```

---

## Step 3: Download Project from GitHub

### 3.1 Clone the Repository

```bash
# Navigate to your projects directory
cd ~/Projects

# Clone the repository
git clone https://github.com/limmutable/Comparable_Analysis_Example.git

# Enter the project directory
cd Comparable_Analysis_Example
```

### 3.2 Verify Project Structure

```bash
ls -la
```

You should see:
```
.claude/          # Claude Code configuration and skills
dataroom/         # Source documents (SEC filings, etc.)
instructions/     # Educational guides (you are here)
output/           # Generated analysis outputs
prompts/          # LLM prompts for analysis tasks
scripts/          # Educational Python scripts
src/              # Internal source code
```

---



## Step 4: Verify Your Setup

Run the following commands to verify everything is working:

```bash
# 1. Check Gemini CLI
gemini --version

# 2. Check Claude CLI
claude --version

# 3. Navigate to project
cd ~/Projects/Comparable_Analysis_Example

# 4. Start Gemini and test
gemini
> "Hello, are you ready for financial analysis?"
```

---

## Next Steps

Now that your environment is set up, you can:

1. **Explore the dataroom** - Review the SEC filings and source documents
2. **Run your first analysis** - Ask Claude to analyze a document
3. **Generate outputs** - Create comparable analysis reports in the `/output` directory

See the other guides in this `/instructions` directory for specific tutorials on financial analysis tasks.

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
