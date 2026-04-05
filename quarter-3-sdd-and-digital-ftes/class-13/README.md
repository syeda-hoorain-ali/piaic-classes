# 🤖 Spec-Driven Development – Class 13 (4 April 2026)

## 📖 What we covered
- **System of Record for Agents**: Why canonical knowledge bases matter in the AI era
- **The Data Collection Journey**: From predictive AI to agentic AI (the Japanese mouse maze analogy)
- **Skills as Intellectual Property**: Progressive disclosure, token efficiency, and domain expertise encoding
- **Subagents vs Skills**: When to use isolated context vs shared context
- **MCP Integration**: Connecting Claude to external systems (databases, APIs, web)
- **MCP Tool Search**: Automatic lazy loading for 85% token reduction
- **Certification Path**: L1 Certified Agentic AI Engineer exam structure

---

## 🗄️ System of Record for the Agent Era

### AI Needs Ground Truth

**Jensen Huang (NVIDIA CEO) insight**: AI agents don't eliminate systems of record—they reinforce it.

**The Problem**: 
- Agents without authoritative data sources → hallucination
- Scattered tutorials, outdated blogs, unverified content → inconsistent learning
- Data poisoning at scale → unreliable model outputs

**The Solution**: Canonical knowledge bases
- **Book = System of record** (authoritative source of truth)
- **TutorClaw = Agent** (reads from verified knowledge, not open internet)
- **Human judgment = Verification layer** (confirms accuracy)

### The Japanese Mouse Maze Analogy

**Why wasn't AI built 20-30 years ago?**

Think of the mechanical mouse maze competition:
1. **First run**: Mouse explores maze, tries left path (blocked), backtracks, tries right path (success)
   - Takes time, collects data, learns the layout
2. **Second run**: Mouse solves maze 100x faster
   - Why? It already has the data

**The same happened with AI:**
- **Past 20-30 years**: Companies collected massive training data through search engines, user interactions
- **Challenge**: As data grows, so does noise—wrong information, misinformation, poisoned data
- **Result**: No standard for legitimate data = inconsistent/hallucinated outputs

**Key insight**: We now have data at scale, but quality is the bottleneck. Canonical sources (like this book) become critical.

📕 **Learning Resource:** [A System of Record for the Agent Era - Agent Factory](https://agentfactory.panaversity.org/docs/about#a-system-of-record-for-the-agent-era)

---

## 🎯 Skills: Your Intellectual Property

### Why Skills Are More Than Shortcuts

**Domain expertise examples:**
- Accountant who structures audits perfectly → **That's a skill**
- Recruiter who evaluates candidates effectively → **That's a skill**  
- Legal team's contract review workflow → **That's a skill**

**You don't need programming skills to create them—you need domain expertise and clear documentation.**

### The Three-Level Architecture

**Challenge**: Claude has limited context window (200K tokens). Loading all skills at startup = no space for actual work.

**Solution**: Progressive disclosure

**Level 1 - Brief Metadata (Always Loaded)**
- Short description: what the skill does, when it's relevant
- ~100 tokens per skill
- Just enough for Claude to know it exists

**Level 2 - Full Instructions (On-Demand)**
- Complete SKILL.md with procedures, workflows, examples
- Loaded only when Claude determines skill is relevant
- <5K tokens

**Level 3 - Supporting Files (If Needed)**
- Scripts, reference docs, templates in skill directory
- Accessed only during skill execution
- Variable size

**Result**: You can have 100+ skills without overwhelming context. Claude activates only what's needed.

### Skills + Scripts = Token Efficiency

**Bad approach** (wastes tokens):
```
"First add 3 + 3, then add x to it, then multiply by y, 
then apply formula z, then check if result > 100..."
```
Every time you run this task → fills context window with instructions.

**Good approach** (save tokens):
1. Create a script/code that does the calculation
2. Add script to your skill's directory
3. Skill instructions: "Run calculation.py with input values"
4. Agent executes script, gets output, minimal tokens used

**Example skill with script:**
```
.claude/skills/financial-analysis/
├── SKILL.md                 # Instructions
├── scripts/
│   ├── roi_calculator.py    # Predefined calculation
│   └── risk_assessment.py   # Another calculation
└── templates/
    └── report_template.md
```

**Benefits:**
- Consistent calculations (same formula every time)
- Token-efficient (just references script, doesn't explain logic)
- Reusable (script can be called from multiple skills)
- Verifiable (code can be reviewed, tested)

**Skills are strategic assets**, not disposable prompts:
- Share with teams (everyone benefits from expertise)
- Version in Git (track improvements)
- Integrate into Custom Agents
- Monetize as vertical AI solutions

📕 **Learning Resource**: [The Concept Behind Skills - Agent Factory](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/concept-behind-skills)

---

## 🤖 Subagents vs Skills: Decision Framework

### Why Subagents Work: Clean Context

**Without subagents** (one AI doing everything):
1. You: "Research competitors"
2. Context fills with research notes
3. You: "Draft a pitch"  
4. Problem: Context cluttered, Claude confuses research with pitch

**With subagents**:
1. Research subagent → does research → returns clean summary
2. Main Claude → receives summary → context stays clean
3. Planning subagent → drafts pitch → fresh context
4. Each specialist focuses on one job

**Analogy**: Team meeting where researcher presents findings, then leaves. Strategist creates plan with fresh focus. Nobody juggles everything at once.

### Decision Criteria: Skills vs Subagents

| Factor | Choose Skill | Choose Subagent |
|--------|--------------|-----------------|
| **Invocation** | Automatic OR explicit by name | Explicit only (you invoke) |
| **Context** | Shared with main conversation | Isolated context window |
| **Complexity** | Lightweight, single-focus | Multi-step, complex workflows |
| **Guarantee** | Flexible (auto-triggers or invoke) | Hard invocation (always runs) |
| **Best for** | Repeated patterns, formatting | Audits, refactoring, analysis |

### Examples

**Skill appropriate:**
- Meeting notes formatting (happens often, simple procedure)
- Blog post planning (repeated task, consistent structure)
- Code comment style (automatic enforcement)

**Subagent appropriate:**
- Comprehensive security audit (complex, needs isolation)
- Multi-file refactoring (guaranteed execution required)
- Full codebase analysis (too large for skill context)

**Use skill when**: "I want Claude to automatically do this whenever relevant."

**Use subagent when**: "I need guaranteed execution with isolated context for this complex task."

📕 **Learning Resource:** [Subagents & Orchestration - Agent Factory](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/subagents-and-orchestration)

---

## 🔌 MCP: Connecting to External Systems

### The Problem

Right now, Claude Code can only see files on your computer.

**What if you need Claude to:**
- Browse a website for information?
- Check latest library documentation?
- Query a database?
- Access an API?

All that data lives **outside your computer**. Claude Code can't reach it... yet.

### MCP Solution: Safe Access to the Outside World

**Think of MCP like this:**

**Without MCP**: Claude is a brilliant assistant who works in your office (your computer).
- Can only use what's in the office: files on your desk, folders in your cabinet

**With MCP**: You give Claude a phone directory with approved contacts:
- Web browser expert
- Documentation specialist
- Database consultant
- Now Claude can call the right expert and get answers safely

**MCP is that phone directory**—it connects Claude Code to external tools and data sources in a standardized, safe way.

### The Tool Definition Challenge

Each MCP server comes with tool definitions (descriptions, parameters, outputs).

**Token costs:**
- Playwright MCP: ~5,000-8,000 tokens
- Context7 MCP: ~3,000-5,000 tokens
- GitHub MCP: ~8,000-12,000 tokens
- **5 servers installed**: 25,000-40,000 tokens before you ask a question!

### MCP Tool Search: Built-In Solution

**Automatic lazy loading** that defers tool definitions until needed.

**How it works:**
1. Claude Code monitors installed MCP servers
2. When tool definitions exceed 10% of context → Tool Search activates
3. Instead of loading all tools upfront → searches for relevant tools on-demand
4. Only tools you actually use get loaded

**Result**: ~85% automatic reduction in MCP overhead

### Control and Configuration

**Command line:**
```bash
# Default: activates at 10% context
ENABLE_TOOL_SEARCH=auto claude

# Custom threshold (activate at 5%)
ENABLE_TOOL_SEARCH=auto:5 claude

# Always on
ENABLE_TOOL_SEARCH=true claude

# Always off (legacy: loads all tools upfront)
ENABLE_TOOL_SEARCH=false claude
```

**Or in settings.json:**
```json
{
  "env": {
    "ENABLE_TOOL_SEARCH": "auto:5"
  }
}
```

**For most users**: You don't need to do anything. Tool Search works automatically.

📕 **Learning Resource:** [MCP Integration - Agent Factory](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/mcp-integration)

---

## 🎓 Certification Path: L1 Certified Agentic AI Engineer

### Four Exam Components

**1. Agent Factory Intro Exam (L1:P1-AFI)**

Exam content:
- [About This Book](https://agentfactory.panaversity.org/docs/thesis)
- [The Agent Factory Thesis](https://agentfactory.panaversity.org/docs/about)
- [Which AI Employees Should You Use in 2026?](https://agentfactory.panaversity.org/docs/which-agents-2026)
- [Why AI Is Non-Negotiable?](https://agentfactory.panaversity.org/docs/why-ai-is-non-negotiable)
- [PREFACE: The AI Agent Factory](https://agentfactory.panaversity.org/docs/preface-agent-native)

**2. Claude Code Foundation Exam (L1:P2-CCF)**

Exam content:
- [Chapter 12: The AI Agent Factory Paradigm](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/agent-factory-paradigm)
- [Chapter 13: Markdown - Writing Instructions](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/markdown-writing-instructions)
- [Chapter 14: Working with General Agents](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents)

**3. Advanced Claude Code Exam (L1:P3-ACC)**

Exam content:
- [Chapter 15: Effective Context Engineering](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/context-engineering)
- [Chapter 16: Spec-Driven Development](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/spec-driven-development)
- [Chapter 17: Seven Principles of Problem Solving](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/seven-principles)
- [Chapter 18: Claude Code for Teams & CI/CD](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/claude-code-teams-cicd)

**4. Agent Workflow Primitives Exam (L1:P4-AWP)**

Exam content:
- [Chapter 19: File Processing Workflows](https://agentfactory.panaversity.org/docs/Agent-Workflow-Primitives/file-processing)
- [Chapter 21: Structured Data & Persistent Storage](https://agentfactory.panaversity.org/docs/Agent-Workflow-Primitives/structured-data-persistent-storage)
- [Chapter 23: Version Control & Safe Experimentation](https://agentfactory.panaversity.org/docs/Agent-Workflow-Primitives/version-control)


📕 **Latest Syllabus:** [Certified Agentic AI Architect](https://docs.google.com/document/d/1-T1lmz01jpxffGPJ0nQ0m2cmdXlMLPojrCLnwrQ1HPc/edit?tab=t.0)

---

💡 **Key Takeaway**: In the agent era, canonical knowledge bases aren't optional—they're the foundation that prevents hallucination and ensures verified execution. Your skills are intellectual property that compounds in value across the entire agentic ecosystem.
