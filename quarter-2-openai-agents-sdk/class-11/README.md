# 🤖 OpenAI Agents SDK – Class 11 (1 Nov 2025)

This class was focused on advanced Agent SDK concepts.

---

## 🔁 TResponseInputItem & `result.to_input_list()`

Turning agent responses into reusable structured inputs for chaining and debugging.

---

## 📊 Tracing (OpenAI Tracing Dashboard)

We learned how to inspect each llm call, tool call, and agent step.

📕 **Resource:** [Basic Tracing](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/12_basic_tracing)

MLflow was briefly mentioned for tracking external models.

---

## ⚙️ Model Settings

Controls affecting agent behaviour:

* **tool_choice** – auto, required & none
* **max_tokens** – output length control
* **parallel tool calls** – run multiple tools at once

📕 **Resource:** [Model Settings](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/07_model_settings)

---

## 🔄 Streaming

There are two kinds of streaming:

* **LLM Output Streaming** – token-by-token
* **Agent Loop Streaming** – see each tool step in real time

📕 **Resource:** [Streaming](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/10_streaming)

⚠️ We also saw how streaming reveals errors inside the tool/agent loop.

---

## 🧬 `agent.clone()`

Duplicate an agent with same configuration and modify specific parts.

📕 **Resource:** [Agent Clone](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/11_agent_clone)

---

## 🛠️ Advanced Tool Controls

* **max_turns** – stop runaway loops
* **tool_use_behavior** – decide how freely tools are used

📕 **Resource:** [Advanced Tools](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/15_advanced_tools)

---

## 📦 Structured Output

Force the model to return clean, predictable JSON.

📕 **Resource:** [Structured Output](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/17_structured_output)

---

## 🔔 Hooks (Agent + Runner)

Hooks let you run custom logic before/after each step.

📕 **Resource:**
- [Agent Lifecycle](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/19_agent_lifecycle)
- [Run Lifecycle](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/20_run_lifecycle)

---
