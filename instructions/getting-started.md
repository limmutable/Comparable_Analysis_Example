# Getting Started Guide

This guide walks you through setting up your development environment for the Comparable Analysis project.

## Prerequisites

- macOS or Windows with WSL (Windows Subsystem for Linux)
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


## Step 1: Install Claude CLI

Claude Code is a command-line tool that brings Claude's AI capabilities to your terminal.

### 1.1 Install Node.js (if not already installed)

Claude CLI requires Node.js 18 or higher.

```bash
# Check if Node.js is installed
node --version

# If not installed, use Homebrew (macOS)
brew install node

# Or download from https://nodejs.org/
```

### 1.2 Install Claude CLI

```bash
npm install -g @anthropic-ai/claude-code
```

### 1.3 Authenticate Claude CLI

```bash
claude
```

On first run, you'll be prompted to authenticate. You can either:
- Log in with your Anthropic Console account, or
- Enter your API key directly

### 1.4 Verify Installation

```bash
claude --version
```

---

## Step 2: Install Gemini CLI

Gemini CLI provides access to Google's Gemini models from the terminal.

### 2.1 Install Gemini CLI

```bash
npm install -g @anthropic-ai/claude-code
```

Or using Homebrew:

```bash
brew install gemini-cli
```

### 2.2 Authenticate Gemini CLI

```bash
gemini auth login
```

Follow the prompts to authenticate with your Google account or API key.

### 2.3 Verify Installation

```bash
gemini --version
```

---

## Step 3: Download Project from GitHub

### 3.1 Clone the Repository

```bash
# Navigate to your projects directory
cd ~/Projects

# Clone the repository
git clone https://github.com/YOUR_USERNAME/Comparable_Analysis_Example.git

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

## Step 4: Setup Claude Skills

Claude Skills are automatically loaded when you run Claude CLI in this project directory. The project includes two pre-configured skills for financial analysis.

### 4.1 Verify Skills Are Installed

Navigate to the project directory and check the skills folder:

```bash
cd ~/Projects/Comparable_Analysis_Example
ls -la .claude/skills/
```

You should see:
```
financial-modeling/
financial-analysis/
```

### 4.2 Understanding the Skills

| Skill | Description |
|-------|-------------|
| `financial-modeling` | Build financial models, forecasts, and DCF valuations |
| `financial-analysis` | Comparable company analysis, financial statement analysis, trading multiples |

### 4.3 How Skills Work

Skills are automatically activated based on your request. When you ask Claude to perform a task related to financial modeling or analysis, it will use the appropriate skill.

**Example prompts that activate skills:**

```bash
# Start Claude in the project directory
cd ~/Projects/Comparable_Analysis_Example
claude

# These prompts will activate the financial-analysis skill:
> "Analyze the SEC filing in the dataroom"
> "Create a comparable company analysis for tech companies"
> "Calculate valuation multiples for these companies"

# These prompts will activate the financial-modeling skill:
> "Build a DCF model with these assumptions"
> "Create a 5-year revenue forecast"
> "Project cash flows for this company"
```

### 4.4 Viewing Skill Details

To see what a skill contains:

```bash
cat .claude/skills/financial-analysis/SKILL.md
cat .claude/skills/financial-modeling/SKILL.md
```

### 4.5 Creating Your Own Skills (Optional)

To create a custom skill:

1. Create a new directory in `.claude/skills/`:
   ```bash
   mkdir -p .claude/skills/my-custom-skill
   ```

2. Create a `SKILL.md` file with YAML frontmatter:
   ```bash
   cat > .claude/skills/my-custom-skill/SKILL.md << 'EOF'
   ---
   name: my-custom-skill
   description: Describe when this skill should be used.
   allowed-tools: Read, Write, Edit, Bash
   ---

   # My Custom Skill

   ## Instructions
   Add your instructions here...
   EOF
   ```

3. The skill will be automatically available next time you run Claude in this directory.

---

## Step 5: Verify Your Setup

Run the following commands to verify everything is working:

```bash
# 1. Check Claude CLI
claude --version

# 2. Check Gemini CLI
gemini --version

# 3. Navigate to project
cd ~/Projects/Comparable_Analysis_Example

# 4. Start Claude and test a skill
claude
> "What skills are available in this project?"
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
