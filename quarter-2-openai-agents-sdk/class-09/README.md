# 🤖 OpenAI Agents SDK – Class 9 (19 October 2025)

---

## **🧭 The Seven Pillars of AI-Driven Development**

The **Seven Pillars Framework** defines how modern AI-native systems are built — shifting focus from *writing code* to *designing specifications*.

| 🏛️ Pillar                          | 🧩 Concept                                                             | 💬 Essence                                                         |
| :---------------------------------: | :--------------------------------------------------------------------- | :------------------------------------------------------------------ |
| **1 Markdown as Language**          | Specs written in `spec.md` and `plan.md` act as executable blueprints. | Markdown → universal interface between human intent & AI execution. |
| **2 Linux Environment**             | Unified Bash/WSL workflow with Git & GitHub Actions.                   | Reproducible, automated development pipelines.                      |
| **3 AI CLI Agents**                 | Gemini CLI / Codex / Claude Code.                                      | Terminal-based AI assistants for coding and testing.                |
| **4 Model Context Protocol (MCP)**  | “USB-C for AI” connecting agents to data and tools.                    | Enables plugins and real-world actions by AI agents.                |
| **5 Test-Driven Development (TDD)** | Tests written before code.                                             | “No green, no merge.” Quality through automation.                   |
| **6 Spec-Driven Development (SDD)** | Specifications drive planning → tasks → implementation.                | Code always aligned with specifications.                            |
| **7 Cloud-Native Deployment**       | Docker, Kubernetes, Dapr, Ray                                          | Scalable distributed AI systems.                                    |

---

## **🐧 Setting up WSL (Windows Subsystem for Linux)**

> Required for Linux-based AI CLI tools and Spec-Kit Plus.

1. **Turn Windows features on/off →** enable

   * ✅ *Virtual Machine Platform*
   * ✅ *Windows Subsystem for Linux*
2. Restart your system.
3. In **CMD** run:

   ```bash
   wsl --status
   wsl --update
   wsl --install -d Ubuntu
   ```
4. Create username + password.
5. Confirm virtualization in **Task Manager → Performance → Virtualization = Enabled**
   (enable in BIOS if disabled).

---

## **🤖 Gemini CLI Setup**

> AI coding agent for spec-driven development.

```bash
node -v           # ensure v20+
npm install -g @google/gemini-cli
gemini -v
# or on WSL
sudo snap install gemini
```

📘 Docs: [Panaversity Gemini CLI Guide](https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus/01a_ai_cli/01_big_free_tiers)
📰 Tutorial: [Gemini CLI Series (Medium)](https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718)

---

## **🏗️ Microsoft Spec-Kit**

Microsoft’s **Spec-Kit** introduced the foundation of **Spec-Driven Development**, where
developers define software through **specifications instead of manual coding**.

* Structured workflow using slash commands:
  `/sp.constitution → /sp.specify → /sp.plan → /sp.tasks → /sp.implement`
* Integrates with AI CLIs (Gemini, Claude, Codex).
* Focus on architecture and governance rather than syntax.

---

## **🚀 Panaversity Spec-Kit Plus (SpecifyPlus)**

> Panaversity’s enhanced fork of Microsoft Spec-Kit — combining **vibe coding speed** with **spec-driven structure** for building multi-agent AI systems.

### **🧰 Installation**

```bash
# inside WSL
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install specifyplus
```

### **✨ Initialize a Project**

```bash
specifyplus init speckit_hello_world
# or
sp init .
```

Choose:

* AI assistant → `gemini`, `qwen`, or `claude`
* Script → `sh` (for Bash) or `ps` (for PowerShell)

---

### **⚙️ Slash Commands Workflow**

| Slash Command      | Purpose                                                |
| :----------------- | :----------------------------------------------------- |
| `/sp.constitution` | Define project rules (quality, UX, testing standards). |
| `/sp.specify`      | Describe what to build and why.                        |
| `/sp.plan`         | Outline tech stack and architecture.                   |
| `/sp.tasks`        | Break plan into actionable tasks.                      |
| `/sp.implement`    | Execute tasks and build project.                       |
| `/sp.clarify`      | Resolve ambiguous requirements.                        |
| `/sp.analyze`      | Check consistency across specs and plans.              |


---

## **🛡️ Guardrails in OpenAI Agents SDK**

**Guardrails** are like the safety barriers on a mountain highway. Just as physical guardrails prevent cars from going off dangerous cliffs, AI guardrails prevent your agents from doing things they shouldn't do or producing outputs that could be harmful, inappropriate, or costly.
They validate inputs and outputs — ensuring agents behave predictably and securely.

📂 Repo: [Panaversity – OpenAI Agents Guardrails](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/18_guardrails)
🧪 Colab Example: [Guardrails Notebook](https://colab.research.google.com/drive/1pQCYRMO922Vo2jXin_Q3io8sbugNtKM8?usp=sharing)

---

## **📚 Resources**

* 🧠 **Spec-Kit Plus Docs:** [https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus](https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus)
* 🧩 **Gemini CLI Guide:** [https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus/01a_ai_cli/01_big_free_tiers](https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus/01a_ai_cli/01_big_free_tiers)
* 🔐 **Guardrails Repo:** [https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/18_guardrails](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/18_guardrails)
* 📘 **Gemini CLI Tutorial:** [https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718](https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718)

---

## **🪄 Summary**

* **Seven Pillars** → foundation of AI-driven software engineering.
* **WSL** → Linux environment on Windows for AI development.
* **Gemini CLI** → AI assistant for code generation via terminal.
* **Spec-Kit Plus** → Panaversity’s complete spec-driven toolchain.
* **Guardrails** → safety layer for OpenAI Agents SDK.

> 🧩 *Build the future with specifications — not just code.*

---
