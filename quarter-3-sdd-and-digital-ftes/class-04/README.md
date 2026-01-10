# 🤖 Spec-Driven Development & Digital FTEs – Class 4 (10 Jan 2026)
## 📖 What we covered

- Slides **37 to 47** — Manual Prompting vs Agent Skills evolution
- **Chapter 5** of the book — Agent Factory
- Browser vs Terminal agents comparison
- Deep dive: **Skills, Sub-agents, Hooks, Plugins, Skills + MCP**
- Hands-on: Installing and using **Claude Code Marketplace** skills
- Building **Digital FTEs** with full system access

📕 **Slides:** [Agent Factory: Building Digital Full-Time Equivalents (FTEs)](https://docs.google.com/presentation/d/1UGvCUk1-O8m5i-aTWQNxzg8EXoKzPa8fgcwfNh8vRjQ/edit)

---

## 🧠 Core Concepts

### Manual Prompting vs Agent Skills

**Manual Prompting (Old Way):**
- ❌ Ad-hoc, best-effort results
- ❌ Pay for "rules" in every conversation turn
- ❌ Disposable — knowledge lost after chat
- ❌ Requires human to copy-paste context

**Agent Skills (New Way):**
- ✅ Deterministic, script-backed execution
- ✅ Load rules only when triggered (token savings)
- ✅ Reusable IP — knowledge as scalable asset
- ✅ API-ready via Agent SDKs

> 🎬 **Matrix Analogy:** Trinity downloads helicopter flying skills instantly when needed — Agent Skills work the same way: load expertise on-demand into agent context.

### Browser vs Terminal Agents

**Browser Agents (claude.ai):**
- Limited sandbox environment
- Can't access your file system
- Safe but restricted
- Good for conversations and web tasks

**Terminal Agents (Claude Code):**
- Full access to your operating system
- Can read/write files, run commands, install packages
- "God Mode" over your machine
- Real power for automation

---

## 🏗️ Digital FTE Architecture

### What is a Digital FTE?

**Digital Full-Time Equivalent** = AI agent that works like a human employee

**Components:**
1. **General Agent** (Claude Code) — the brain
2. **MCP Servers** — connectivity to external systems
3. **Skills** — expertise packages (SKILL.md)
4. **Sub-agents** — specialized workers
5. **Hooks** — event triggers for automation

### How They Work Together
```
Human → Digital FTE (General Agent)
         ↓
    Skills (expertise) + MCP (data access)
         ↓
    Sub-agents (specialized tasks)
         ↓
    Enterprise Systems & Data
```

---

## 📦 Agent Skills Deep Dive

### What are Skills?

**Skills** = Organized folders containing:
- `SKILL.md` — instructions and metadata
- Scripts — executable code
- Templates — reusable files
- Resources — reference materials

### How Skills Work

**Progressive Disclosure:**
- Claude loads skill metadata (name + description) at startup
- Full skill content loaded only when triggered
- Saves massive amounts of tokens
- Enables unlimited expertise packages

**Example Structure:**
```
.claude/skills/pdf-extractor/
├── SKILL.md                    # Main instructions
├── scripts/
│   └── extract_tables.py       # Python extraction tool
└── references/
    └── pdf-standards.md        # Format specifications
```

### Installing Skills

**From Official Marketplace:**
```bash
# In Claude Code
/plugin marketplace add anthropic/skills

# Install specific skill
/plugin install document-skills@anthropic-agent-skills
```

**From Community Marketplaces:**
```bash
# Engineering workflows
/plugin marketplace add mhattingpete/claude-skills-marketplace

# Enterprise skills
/plugin marketplace add netresearch/claude-code-marketplace
```

**Manual Installation:**
```bash
# Personal skills
~/.claude/skills/

# Project skills (shared via git)
.claude/skills/
```

### Creating Custom Skills

**Basic SKILL.md Template:**
```markdown
---
name: my-skill-name
description: Clear description of what this does and when to use it
---

# My Skill Name

[Instructions Claude will follow when skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

**Key Tips:**
- Write specific descriptions with trigger conditions
- Include concrete examples, not vague advice
- Document failed attempts to prevent repetition
- Use exact parameters and configurations

---

## 🤖 Sub-agents

### What are Sub-agents?

Specialized Claude instances that handle specific types of work independently.

**Built-in Sub-agents:**
- `Explore` — codebase navigation
- `Plan` — project planning
- `general-purpose` — default assistant

**Custom Sub-agents:**

Create in `.claude/agents/code-reviewer.md`:
```markdown
---
name: code-reviewer
description: Review code for quality and best practices
skills: pr-review, security-check
---

[Specific instructions for this agent]
```

**Key Features:**
- Run with their own context (isolated from main conversation)
- Can use different AI models optimized for their task
- Load specific skills via the `skills` field
- Execute tasks independently

---

## 🪝 Hooks

### What are Hooks?

**Hooks** = Event triggers that run automation at specific points in your workflow

**Available Hook Events:**
- `UserPromptSubmit` — before user message is sent
- `PostToolUse` — after Claude uses a tool
- `Stop` — when conversation ends

**Example Use Case — Auto Git Commit:**
```markdown
# .claude/hooks/auto-commit.md
---
event: Stop
---

When session ends:
1. Stage all changes
2. Generate commit message
3. Commit with conventional format
4. Push to remote
```

**Coach Plugin Example:**
- Detects friction signals (errors, repeated instructions)
- Learns from user corrections
- Auto-generates skills from successful patterns
- Cross-repo learning with deduplication

---

## 🔌 Plugins

### What are Plugins?

**Plugins** = Shareable packages containing skills, agents, and hooks

**Plugin Structure:**
```
my-plugin/
├── skills/           # Reusable skills
├── agents/           # Custom sub-agents
├── hooks/            # Event automation
└── marketplace.json  # Installation metadata
```

**Installing Plugins:**
```bash
# Add marketplace
/plugin marketplace add <owner>/<repo>

# List available
/plugin marketplace list

# Install specific plugin
/plugin install <plugin-name>
```

**marketplace.json:**
```json
{
  "name": "my-plugin",
  "description": "Plugin description",
  "version": "1.0.0",
  "skills": [
    {
      "name": "skill-name",
      "description": "What it does",
      "path": "skills/skill-name"
    }
  ]
}
```

---

## 🔗 Skills + MCP Integration

### The Power Combination

**Skills** = "How to do the task" (expertise)
**MCP** = "What data to use" (connectivity)

**Example — Financial Analysis Skill + QuickBooks MCP:**
```
1. Skill provides: How to analyze vendor spending
2. MCP provides: Live connection to QuickBooks data
3. Result: Automated financial audits
```

**Example — Code Review Skill + GitHub MCP:**
```
1. Skill provides: Review checklist and standards
2. MCP provides: Access to pull requests
3. Result: Automated code quality checks
```

### Combined Workflow
.claude/skills/vendor-analysis/SKILL.md
```markdown
---
name: vendor-analysis
description: Analyze vendor spend using Ramp data
---

When user asks for vendor analysis:
1. Use Ramp MCP to fetch transactions
2. Group by vendor using lodash
3. Calculate spend patterns
4. Export to Excel using QuickBooks MCP
5. Generate summary report
```

---

## 🛠️ Hands-on Exercise

### Task: Install and Use a Skill

**Step 1: Add Official Marketplace**
```bash
claude
/plugin marketplace add anthropic/skills
```

**Step 2: Browse Available Skills**
```bash
/plugin marketplace list
```

**Step 3: Install Document Skill**
```bash
/plugin install document-skills@anthropic-agent-skills
```

**Step 4: Verify Installation**
```bash
/skills list
```

**Step 5: Use the Skill**
```
"Use the PDF skill to extract form fields from invoice.pdf"
```

### Task: Create Custom Skill

**Step 1: Create Skill Directory**
```bash
mkdir -p .claude/skills/commit-message
cd .claude/skills/commit-message
```

**Step 2: Create SKILL.md**
```markdown
---
name: commit-message
description: Generate conventional commit messages from git diff
---

# Commit Message Generator

When user asks to commit changes:
1. Run `git diff --staged`
2. Analyze changes
3. Generate message format: `type(scope): description`
4. Suggest message to user

## Types
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Adding tests
- chore: Maintenance

## Examples
- `feat(auth): add OAuth2 login`
- `fix(api): handle null user response`
```

**Step 3: Test**
```bash
# Make some changes
echo "test" > test.txt
git add test.txt

# In Claude Code
"Generate a commit message for these changes"
```

---

## 🌐 Popular Skill Marketplaces

### 1. Official Anthropic Skills
- **URL:** https://github.com/anthropics/skills
- **Focus:** Official examples and templates
- **Categories:** Creative, Development, Enterprise, Documents

---

## 💡 Best Practices

### Writing Effective Skills

**1. Specific Descriptions:**
```markdown
❌ "Helps with testing"
✅ "Fixes failing tests using smart error grouping. Activates when: user reports test failures, asks to fix tests, or wants test suite passing."
```

**2. Include Trigger Conditions:**
- List exact phrases that should activate skill
- Mention specific error messages
- State verified environments/versions

**3. Progressive Disclosure:**
- Put common info in SKILL.md
- Split detailed docs into separate files
- Reference files only when needed
- Keep mutually exclusive contexts separate

**4. Code as Tools:**
- Include scripts for deterministic operations
- Mark if code should be executed vs read as reference
- Prefer code execution over token generation for sorting, filtering, math

### Managing Skills at Scale

**Personal Skills:** `~/.claude/skills/` — your private expertise
**Project Skills:** `.claude/skills/` — committed to git, shared with team
**Plugin Skills:** Distributed via marketplaces

**Token Optimization:**
- Only name + description loaded at startup
- Full content loaded when triggered
- Split large skills into separate files
- Use code execution instead of generating output

---

## 🎯 Key Takeaways

✅ **Agent Skills** = reusable IP vs disposable prompts
✅ **Progressive Disclosure** = unlimited expertise without token bloat
✅ **Sub-agents** = specialized workers with isolated contexts
✅ **Hooks** = event-driven automation
✅ **Plugins** = shareable packages of skills + agents + hooks
✅ **Skills + MCP** = expertise + data = powerful automation
✅ **Terminal agents** = full system access vs browser limitations
✅ **Marketplaces** = discover 25,000+ community skills

---

## 📚 Resources

- [Claude Marketplaces Hub](https://claudemarketplaces.com/)
- [Claude Code Skills Guide](https://code.claude.com/docs/en/skills)
- [Anthropic Official Skills](https://github.com/anthropics/skills)
- [Agent Factory Book (Chapter 5)](https://agentfactory.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows/concept-behind-skills)
- [Slides: Agent Factory: Building Digital Full-Time Equivalents (FTEs)](https://docs.google.com/presentation/d/1UGvCUk1-O8m5i-aTWQNxzg8EXoKzPa8fgcwfNh8vRjQ/edit)

---

## 🏆 Homework

**Task 1:** Install 3 skills from claude code marketplaces and test them

**Task 2:** Create a custom skill for your own workflow (e.g., "project setup", "code formatting", "documentation generator")

**Task 3:** Combine a skill with an MCP server (e.g., GitHub skill + GitHub MCP)

**Task 4:** Document one failed attempt and turn it into a skill for your team

---

> 🧩 *"Skills turn general agents into specialized teammates."*
