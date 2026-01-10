# 🤖 Spec-Driven Development & Digital FTEs – Class 2 (27 Dec 2025)

## 📖 What we covered

- Slides **19 to 29** — **General Agents vs Custom Agents** strategic decision framework.
- Deep dive into **Claude Code as a General Agent** (not just a coding tool).
- Installing **Claude Code Router** to use free AI models (Gemini).
- Connecting **GitHub MCP Server** to Claude Code for repository access.
- Live demo: Running Claude Code with Gemini via router.

📕 **Slides:** [Agent Factory: Building Digital Full-Time Equivalents (FTEs)](https://docs.google.com/presentation/d/1UGvCUk1-O8m5i-aTWQNxzg8EXoKzPa8fgcwfNh8vRjQ/edit)

---

## 🧠 Key Concepts

### Two Paths to AI Agentic Automation

| **Option A: "Smart Consultant"** | **Option B: "Assembly Line"** |
|:----------------------------------|:------------------------------|
| **Examples:** Claude Code, Goose | **Examples:** OpenAI Agents SDK, Claude Agent SDK |
| **Focus:** High-level reasoning, autonomy, flexibility | **Focus:** Reliability, process control, specific workflows |
| **Analogy:** Senior employee who figures out solutions | **Analogy:** Factory machine performing specific tasks perfectly |

### Decision Matrix: When to Choose?

| Requirement | General Agent (Claude Code) | Custom Agent (OpenAI SDK) |
|:------------|:----------------------------|:--------------------------|
| **Task Type** | Novel, Problem-Solving | Repetitive, Standardized |
| **End User** | Developers / Technical Staff | Non-Technical / Customers |
| **Error Tolerance** | High (Human in the loop) | Low (Must be reliable) |
| **Cost Sensitivity** | Low (High value per task) | High (Volume optimization) |
| **Implementation** | Instant (Install & Run) | Weeks (Design & Build) |

### Why Claude Code is a General Agent

**The Misconception:** It's just for coding/syntax assistance.

**The Reality:** It's an **Autonomous Problem Solver** that uses code as its interface.

| Feature | Coding Agent (Copilot) | General Agent (Claude Code) |
|:--------|:-----------------------|:----------------------------|
| **Habitat** | Text Editor (VS Code) | Terminal / CLI |
| **Visibility** | Only current file | Entire Operating System |
| **Capabilities** | Writes text | Executes Commands |
| **Scope** | "Complete this function" | "Check network, query DB, fix bug" |

> 💡 **Key Insight:** Code is the **Universal Interface** — General Agents use code to interrogate reality, analyze data, and solve business problems, not just write software.

---

## 🧰 Installation & Setup

### 1️⃣ Install Claude Code
```bash
npm i -g @anthropic-ai/claude-code
```

### 2️⃣ Install Claude Code Router
```bash
npm i -g claude-code-router
```

### 3️⃣ Start Router UI
```bash
ccr ui
```

This opens `http://localhost:3456/ui/`

---

## 🔑 Connect Gemini Model

### Step 1: Get Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click **"Create API Key"**
3. Select your project
4. **Copy** the generated API key

### Step 2: Configure Router

In the Router UI (`http://localhost:3456/ui/`):

1. Click **"Add provider"** button
2. Select **"gemini"** from "Import from templates"
3. **Paste** your Gemini API key
4. Click **"Save & Restart"** button

### Step 3: Run Claude Code with Router
```bash
ccr restart
ccr code
```

You'll enter the **Interactive Claude Code Interface**.

Try saying: `hello` or ask it to create a simple project!

---

## 🔗 Connect GitHub MCP Server

### Step 1: Generate GitHub Personal Access Token

1. Go to [GitHub Personal Access Tokens](https://github.com/settings/personal-access-tokens/new)
2. Create a new token with appropriate permissions
3. **Copy** the token

### Step 2: Add GitHub MCP to Claude Code
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp -H "Authorization: Bearer YOUR_GITHUB_PAT"
```

Replace `YOUR_GITHUB_PAT` with your actual token.

### Step 3: Verify Installation
```bash
# Restart Claude Code
ccr restart

# List configured MCP servers
claude mcp list
```

You should see the GitHub server in the list.

### 📌 Scope Flag (Optional)

Use `--scope` to control where the configuration is stored:

| Scope | Description |
|:------|:------------|
| `local` (default) | Available only in current project |
| `project` | Shared via `.mcp.json` file with team |
| `user` | Available across all your projects |

**Example:**
```bash
claude mcp add --scope user --transport http github https://api.githubcopilot.com/mcp -H "Authorization: Bearer YOUR_GITHUB_PAT"
```

---

## 🎯 Skills & MCP Explained

### Agent Skills = "How-To"
- Modular folders with `SKILL.md`
- Teach Claude specific workflows
- Example: "Analyze financial statements according to Q4 risk framework"
- **Purpose:** Standardizing expertise

### MCP = "With-What"
- Protocol connecting skills to live data
- Examples: SQL databases, Jira, Slack, GitHub
- **Purpose:** Data connectivity

> 🏭 **Agent Factory Concept:** General Agents + MCP + Skills = Transform knowledge into deployed Custom Agents

---

## 📚 Quick Commands Reference
```bash
# Install tools
npm i -g @anthropic-ai/claude-code
npm i -g claude-code-router

# Start router UI
ccr ui

# Run Claude Code with router
ccr restart
ccr code

# MCP management
claude mcp add [options]
claude mcp list
claude mcp remove <name>
```

---

## 🏆 Key Takeaways

✅ **Claude Code** is a General Agent that uses code as a universal interface
✅ **Choose General Agents** for novel problem-solving; **Custom Agents** for standardized workflows
✅ **Claude Code Router** enables using free models (Gemini) with Claude Code
✅ **MCP servers** connect Claude Code to external systems (GitHub, databases, etc.)
✅ **Code is not the goal** — it's the mechanism for AI to interact with reality

---

> 🧩 *"Code is the glue that holds the Agent Factory together."*
