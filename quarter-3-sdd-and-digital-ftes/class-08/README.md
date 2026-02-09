# 🤖 Spec-Driven Development & Digital FTEs – Class 8 (7 Feb 2026)

## 📖 What we covered
- **From Coder to Orchestrator**: Role evolution in the AI era
- **The OODA Loop**: How autonomous agents think (Observe, Orient, Decide, Act)
- **Teaching Claude your workflow** using skills and project context
- **Active vs Passive components** in system architecture
- Setting up **CLAUDE.md** for project-specific context

---

## 🎯 The Orchestrator Mindset

**Old role (Typist)**: Write every line of code manually
**New role (Orchestrator)**: Direct AI to implement while you focus on judgment

### What Changes
- **Planning**: AI helps generate specs from vague descriptions
- **Coding**: AI writes 80-90% of code; you validate quality
- **Testing**: AI generates test cases; you validate coverage
- **Deployment**: AI orchestrates pipelines; you validate strategy
- **Operations**: AI monitors 24/7; you validate incident response

### Your Focus Shifts To
✅ Problem decomposition
✅ Writing clear specifications
✅ Architecture decisions
✅ Quality validation
✅ Security assessment

---

## 🔄 The OODA Loop Explained

**OODA** = Observe → Orient → Decide → Act (repeat)

**Example - Debugging:**
```
OBSERVE: Read error message
   ↓
ORIENT: Identify root cause (null reference? timeout?)
   ↓
DECIDE: Choose where to investigate
   ↓
ACT: Read files, run tests
   ↓
OBSERVE: Did it fix? (repeat until solved)
```

**Key difference:**
- Passive AI (ChatGPT): Predicts one response
- Agentic AI (Claude Code): Loops until goal achieved

---

## 🗂️ Project Context: CLAUDE.md

**Why it matters:** Claude forgets your project between sessions

**Create CLAUDE.md in project root:**
```markdown
# Project: Finance Management System

## Tech Stack
- Backend: Python, FastAPI
- Database: PostgreSQL
- Frontend: React

## Architecture Decisions
- Use ADR (Architectural Decision Records)
- RESTful API design
- JWT authentication

## Coding Standards
- PEP 8 for Python
- Async/await for FastAPI routes
- Comprehensive error handling
```

**Benefits:**
- Claude remembers your stack
- Consistent architecture
- Follows your coding style

---

## 🎨 Active vs Passive Components

**RAM (Active)**: Always running, processing data
**ROM/BIOS (Passive)**: Runs only when triggered

**In development:**
- **Active**: Main application logic, running services
- **Passive**: Skills, configuration files, templates (loaded when needed)

**WSL Mounting analogy:**
- Like Google Drive in Colab: External storage mounted when needed
- Docker containers: Isolated environments with mounted volumes

---

## 📚 Hands-On Assignment

### Task 1: Create Initial Project
```bash
# Create project folder
mkdir finance-management
cd finance-management

# Start Claude Code
claude
```

**Prompt for Claude:**
> "I'm building a finance management system for customers, invoices, and payments. Tech stack: Python, FastAPI, PostgreSQL. Create initial project structure with ADR documentation, basic setup, and CLAUDE.md file. Use SpecifyPlus for spec-driven development."

### Task 2: Create CLAUDE.md
Ask Claude to:
- Document tech stack decisions
- Add coding standards
- Include project structure
- Set up guardrails

### Task 3: Practice OODA Loop
Give Claude a bug scenario and observe:
1. How it observes (reads files)
2. How it orients (analyzes context)
3. How it decides (chooses approach)
4. How it acts (implements fix)
5. How it loops (validates solution)

---

## 💡 Key Concepts from Class

**Gates in Programming:**
- AND gate: Both conditions must be true
- OR gate: At least one condition true
- XOR gate: Exactly one condition true
- Used in: Validation logic, access control, workflow decisions

**Jira/Ticketing Systems:**
- Track feature requests and bugs
- Manage development workflow
- Integrate with CLAUDE.md for context

**Mounting (WSL/Docker):**
- External resources accessed when needed
- Like skills: Available but not always active
- Preserves isolation while enabling access

---

## 📕 Resources
- [Chapter 1: From Coder to Orchestrator and the OODA Loop](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/agent-factory-paradigm/from-coder-to-orchestrator)
- [Chapter 3: Teach Claude Your Way](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/teach-claude-your-way)
- [Panaversity repo: Skills Lab](https://github.com/panaversity/claude-code-skills-lab)

---

> 💡 **Remember**: You're not coding - you're orchestrating intelligence. Focus on judgment, not implementation!
