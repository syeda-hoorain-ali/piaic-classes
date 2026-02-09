# 🤖 Spec-Driven Development & Digital FTEs – Class 7 (31 Jan 2026)

## 📖 What we covered
- **Markdown as the specification language** for AI-native development
- **Agent Skills architecture**: encoding expertise, not building agents
- Hands-on skill creation using YAML + Markdown
- Understanding the **Intent Layer** in AI-driven workflows

---

## 🎯 Key Concepts

### Markdown: Your AI Communication Language
Markdown is how you write **specifications** that AI agents understand. Think of it as programming the agent's understanding:
- **Headings** create document hierarchy
- **Lists** organize requirements and steps
- **Code blocks** show examples and expected outputs
- **Links & images** provide context and references

**The paradigm shift**: Stop explaining manually every time—write structured specs once, reuse forever.

### Agent Skills: Encoding Expertise
**The bottleneck isn't AI intelligence—it's access to YOUR expertise.**

Skills are folders containing `SKILL.md` files that teach Claude your procedures:
- Finance team → audit procedures, report formats
- Marketing team → brand voice, campaign templates
- Engineers → code review checklists, documentation standards

**Universal, not just for coding**: Through code, Claude manipulates documents, analyzes data, generates reports in ANY domain.

### The Three-Level Architecture
Protects context from overload:
1. **Metadata** (always loaded): Brief description
2. **Instructions** (on-demand): Full SKILL.md when relevant
3. **Supporting files** (if needed): Templates, scripts, references

You can have 100+ skills without overwhelming Claude's memory.

---

## 🛠️ Skill Creation Basics

### SKILL.md Structure
```markdown
---
name: "meeting-notes"
description: "Transform transcripts into structured summaries with action items. Use when user shares meeting content."
---

# Meeting Notes Skill

## When to Use
- User shares meeting transcript
- User asks for meeting summary

## Procedure
1. Extract action items with owners
2. Highlight decisions made
3. Summarize discussion points
4. Flag open questions

## Output Format
**Action Items**
- [ ] Task — Owner — Deadline
```

### Creating Your First Skill
```bash
# Create skill folder
mkdir -p .claude/skills/blog-planner

# Add SKILL.md with procedure
# Use skill-creator for guidance:
claude
> "Use skill-creator to build a skill for [your task]"
```

---

## 💡 The Real Value

**Skills are reusable IP**, not disposable prompts:
- Share with your team (everyone benefits)
- Version in Git (track improvements)
- Integrate into Custom Agents (Part 6 of course)
- Monetize as vertical AI solutions

When one person improves a skill, **everyone** using that skill gets better.

---

## 📚 Homework Assignment

### Practice Tasks
1. **Create 2 custom skills** for tasks you do repeatedly:
   - Use proper YAML frontmatter
   - Write clear activation descriptions
   - Include procedure steps and output format

2. **Test your skills** with Claude Code:
```bash
   claude
   > [trigger your skill and observe behavior]
```

3. **Refine through iteration**:
   - Use the skill 2-3 times
   - Note what works / doesn't work
   - Ask Claude to improve it

### Recommended Reading
- Review Markdown basics (headings, lists, code blocks)
- Study the `blog-planner` example from lesson materials
- Explore Skills Lab examples

---

## 📕 Resources
- [Chapter 2: Markdown - Writing Instructions](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/markdown-writing-instructions)
- [Chapter 3: The Concept Behind Skills](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/concept-behind-skills)
- [Chapter 3: Building Your Own Skills](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/general-agents/agent-skills)
- [Markdown Slides: The Specification Language of AI-Driven Development](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/part-1/chapter-02/chapter-02-slides.pdf)

---

> 💡 **Remember**: You're not just building agents - you're encoding expertise that makes general-purpose agents specifically useful for YOUR work.
