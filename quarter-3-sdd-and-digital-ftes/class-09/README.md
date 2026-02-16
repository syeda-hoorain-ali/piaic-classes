# 🤖 Spec-Driven Development – Class 9 (14 Feb 2026)

## 📖 What we covered
- **Progressive Disclosure**: 3-level skill loading (Level 1: metadata ~100 tokens, Level 2: full instructions <5K, Level 3: resources)
- **Hands-on Skill Creation**: Building custom skills step-by-step
- **Agent Factory Thesis**: From SaaS subscriptions to outcome-based AI employees
- **Plugin Ecosystem**: Reuse community intelligence before building custom
- **Cross-Vendor Portability**: Your skills work across Claude Code, Codex, Gemini CLI

---

## 🛠️ Hands-On: Build Your First Skill (Step-by-Step)

### Step 1: Check Current Skills
```bash
claude
```
Ask: `How many skills do you have?`

### Step 2: Create Skill Folder
```bash
# Create folder structure
mkdir -p .claude/skills/ui-piaic
```

### Step 3: Create SKILL.md (YAML Only)
Create file: `.claude/skills/ui-piaic/SKILL.md`
```markdown
---
name: ui-piaic
description: Create web base ui using html, css and javascript.
---

### Step 4: Restart & Test Basic Skill
```bash
# Restart Claude Code
claude
```
Ask: `How many skills do you have?`
Run: `/context` (see token usage - Skills: 11 tokens)

Ask: `Create index.html page using ui-piaic`
- Claude will ask permission to use the Skill
- Creates basic HTML file

### Step 5: Add Style Guidelines
Update `SKILL.md` - add Style section:
```markdown
# Style
* Background: black
* Text color: white
```

### Step 6: Restart & Test Styled Output
```bash
# Restart Claude Code
claude
```
Ask: `Create index.html page, write heading "Pakistan Zindabad" using ui-piaic`
- Now Claude applies black background + white text!

### Step 7: Add References Folder
```bash
# Create references folder
mkdir .claude/skills/ui-piaic/references
```

Create: `references/piaic.md`
```markdown
# PIAIC
* Education institution
* Leading AI Technology on National level
* We have 100,000 students
* Cities: Karachi, Islamabad, Lahore, KPK, Faisalabad
```

Create: `references/panaversity.md`
```markdown
# Panaversity
* Online Education institution
* Leading AI Technology on National level
* We have 10,000 students
```

### Step 8: Add Reference Instructions
Update to `SKILL.md` - add Reference section:
```markdown
# About PIAIC
* Read piaic details from ./references/piaic.md

# About Panaversity
* Read panaversity details from ./references/panaversity.md
```

Restart Claude Code
Ask: `Share detail about panaversity`
> ⚠️ It gives response from own knowledge/web search, doesn't read skill!

### Step 9: Fix Description (Critical!)
Update description in `SKILL.md`:
```markdown
---
name: ui-piaic
description: Create web base ui using html, css and javascript. Provides information about piaic and panaversity
---
```

Restart Claude Code
Ask: `share detail about panaversity`
> ✅ Now it reads SKILL.md (Level 2) then panaversity.md from references!

**Key Learning**: Description determines when Claude loads Level 2. If "piaic and panaversity" aren't mentioned, Claude won't activate the skill!

---

## 🏭 Agent Factory Thesis

**SaaS Era → Agent Factory Era**

| Old World | New World |
|-----------|-----------|
| Software subscriptions | AI employees (outcomes) |
| Manual workflows | Industrialized execution |
| Human operates | Human supervises & verifies |

**What remains:** Intent → Execution → Verification

---

## 🎯 Choose Your Vertical Domain

Pick your specialization from **17 vertical expertise areas**:

1. **Manufacturing** — Domain Intelligence
2. **Personal Productivity** — Tasks, Calendars, Workflows
3. **Enterprise Knowledge** — Search & Synthesize Company Tools
4. **Sales** — Prospect Research, Pipeline Management
5. **Marketing** — Content, Campaigns, Multi-Channel Launches
6. **Customer Support** — Triage, Responses, Escalation
7. **Product Management** — Specs, Roadmaps, Delivery Tracking
8. **Finance** — Financial Analysis, Models, Key Metrics
9. **Accounting** — Bookkeeping, Reconciliation, Reporting
10. **Legal** — Document Review, Risk Flagging, Compliance
11. **Data Analysis** — Query, Visualize, Interpret at Scale
12. **Healthcare** — Clinical Documentation, Coding, Patient Workflows
13. **HR & Recruiting** — Screening, Interviews, Onboarding
14. **Architecture & Engineering** — Design, Drafting, BIM Workflows
15. **ERP & Operations** — Procurement, Inventory, Business Processes
16. **Education & Training** — Curricula, Assessments, Learning Paths
17. **Startup Consulting** — Business Plans, Forecasts, Growth Strategy

**📊 Example: Revit MCP for Architecture**
[Revit MCP Presentation](https://docs.google.com/presentation/d/1Uwjgx7OPEqkYkHpDomcDkEwpDN7vfW3kb1YdUPHni0o/edit?slide=id.p1#slide=id.p1) — See how MCP connects Claude to Revit for automated BIM workflows

---

## 🔌 Plugins & Cross-Vendor

**Plugins**: Bundles of skills + agents + MCP
**Key**: Reuse before rebuilding!

**Your skills are portable:**
- `.claude/skills/` → `.agents/skills/` → `.gemini/skills/`

**Top Tools (Feb 2026):**
- **Claude Code**: $1B ARR, accuracy-first
- **OpenAI Codex**: Open source, parallel tasks
- **Gemini CLI**: Free tier, 1M context

---

## 📚 Homework

1. Create domain-specific skill (finance, legal, education, etc.)
2. Test progressive disclosure (with/without description)
3. Explore plugin marketplace

---

## 📕 Resources
- [Agent Factory: Thesis](https://agentfactory.panaversity.org/docs/thesis)
- [Agent Factory: Chapter 3: Plugins](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/plugins-putting-it-all-together)
- [Anthropic: The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

💡 **Remember**: Description triggers activation. No mention in description = Claude won't load skill or refrences!
