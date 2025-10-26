# 🤖 OpenAI Agents SDK — Class 10 (25 Oct 2025)

## 🧩 OpenAI Agents SDK

### **Local Context**

Local Context allows you to pass additional runtime data to an agent that is **not shared with the LLM**, but is available to tools, hooks, and backend logic during execution. It’s useful for dependency injection (e.g., database clients, user info, logs) and scoped configuration per run.

**📕 References:**

* [Panaversity: Local Context](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/08_local_context)
* [OpenAI Docs: Local Context](https://openai.github.io/openai-agents-python/context/#local-context)

---

### **Session Memory**

Session Memory enables agents to maintain continuity across multiple interactions. It stores and retrieves past conversation turns, allowing the agent to “remember” prior context during a session.

**📕 References:**

* [Panaversity: Session Memory](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/21_sesssion_memory)
* [OpenAI Docs: Session Memory](https://openai.github.io/openai-agents-python/sessions/)

---

## ⚙️ Gemini CLI Tutorial

We explored the **Gemini CLI** tool, covering configuration, setup, and usage.
Configurations can be applied at three levels:

1. **Global level**
2. **Project level**
3. **Sub-folder level**

**Example structure:**

```
your-project/.gemini/settings.json
your-project/GEMINI.md
```

**Configuration Reference:**
[Gemini settings.json schema](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md)

---

### 📕 **Gemini CLI Tutorial Series**

For detailed reading and practice, refer to the full tutorial series on Medium:

* Part 1: [Installation and Getting Started](https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718)
* Part 2: [Gemini CLI Command Line Options](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-2-gemini-cli-command-line-parameters-e64e21b157be)
* Part 3: [Configuration Settings via settings.json and .env Files](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-3-configuration-settings-via-settings-json-and-env-files-669c6ab6fd44)
* Part 4: [Built-in Tools](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-4-built-in-tools-c591befa59ba)
* Part 5: [Using GitHub MCP Server](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-5-github-mcp-server-b557ae449e6e)

---
