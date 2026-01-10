# 🤖 Spec-Driven Development & Digital FTEs – Class 1 (20 Dec 2025)

## 📖 What we covered

- Slides up to **Slide 18** (Claude Code timeline) — see PDF in this folder.
- Intro to **Claude Code** setup across OSs.
- Installing **Spec-Kit Plus (SpecifyPlus)** for spec-driven workflows.
- Kicked off **Hackathon 1** assignment for next week.

📕 **Slides:** [Agent Factory: Building Digital Full-Time Equivalents (FTEs)](https://docs.google.com/presentation/d/1UGvCUk1-O8m5i-aTWQNxzg8EXoKzPa8fgcwfNh8vRjQ/edit)

---

## 🧰 Prerequisites & installs

- Enable **WSL** (Windows users): [WSL setup](https://github.com/syeda-hoorain-ali/piaic-classes/blob/main/quarter-2-openai-agents-sdk/class-09/WSL_(windows_subsystem_for_Linux).md)

### Install Claude Code
- macOS / Linux / WSL
  `curl -fsSL https://claude.ai/install.sh | bash`
- Windows PowerShell
  `irm https://claude.ai/install.ps1 | iex`
- Windows CMD
  `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`
- Any OS (npm)
  `npm install -g @anthropic-ai/claude-code`

### Install Spec-Kit Plus (SpecifyPlus)

- Repo: [Spec-Kit Plus](https://github.com/panaversity/spec-kit-plus)
- Hands-on guide: [Spec-Kit Plus hands-on](https://ai-native.panaversity.org/docs/SDD-RI-Fundamentals/spec-kit-plus-hands-on)
- From PyPI (recommended): `pip install specifyplus`
- With uv tools: `uv tool install specifyplus`

---

## 🚀 Quickstart workflow

1) Start Claude Code: run `claude` (login with subscription, send first prompt).
2) Initialize a SpecifyPlus project:
   - `specifyplus init <PROJECT_NAME>`
   - or `sp init <PROJECT_NAME>`

---

## 📚 Homework Assignment

- **Hackathon 1** (due next week): [Assignment doc](https://docs.google.com/document/d/1nw6D37JmTfhPLHo0IfTeCcKajX3Lw9PidDmBjMG1G5o/)
- Install & set up Claude Code with **Gemini CLI** or **Qwen**:
  - [Gemini CLI setup](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows/free-claude-setup)
  - [Qwen setup](https://danielhashmi.medium.com/how-to-use-claude-code-with-qwen-models-for-free-on-powershell-windows-74061f59b8e4?postPublishedType=initial)

---
