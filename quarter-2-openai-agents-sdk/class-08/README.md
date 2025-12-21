# 🤖 OpenAI Agents SDK – Class 8 (11 October 2025)

---

## 🤝 **Handoffs** — Basic

**📘 Definition:**
A *handoff* is when your current agent **transfers control** to another, more specialized agent to finish the task.
In the SDK, a handoff is treated as a **tool** (e.g. `transfer_to_refund_agent`).

**💡 Why we need it:**
Used when different specialists handle different parts of a workflow — like **triage ➜ billing ➜ refund**.
Think customer support routing!

**🧠 Analogy:**

* *Agents-as-tools* → ask a colleague a quick question.
* *Handoff* → transfer the whole call to that colleague.

**🧩 Core SDK Concepts:**

* `Agent.handoffs`: list of agents or `handoff(...)` objects it can transfer to.
* `handoff(...)`: customize name, description, `on_handoff`, and filters.
* Handoff appears to the LLM as a **tool** (e.g. `transfer_to_agentname`).

**📜 Example:**
A “Triage Agent” routes user queries to **Billing** or **Refund** specialists.

```python
triage_agent = Agent(
    name="Triage agent",
    instructions="If billing ➜ Billing agent. If refund ➜ Refund agent.",
    handoffs=[billing_agent, handoff(refund_agent)],
)
```

**🧪 Lab:**
Change user input and inspect `result.new_items` to spot
`HandoffCallItem` and `HandoffOutputItem` — proof that handoff occurred.

---

## 🧠 **Advanced Handoffs**

**💬 Big Idea:**
Advanced handoffs = **VIP transfers** — next agent gets a *briefing*, clean history, and structured data.
It’s not just routing; it’s orchestration.

**🧰 What you can control:**

1. 🏷 **Customize** tool name, description, or add callbacks (`on_handoff`).
2. 📦 **Pass structured data** (Pydantic models like `EscalationData`).
3. 🧹 **Filter history** so the new agent only sees relevant context.
4. 🔁 **Continue conversation** seamlessly with the right specialist.

**🧩 Example:**

```python
custom_handoff = handoff(
    agent=specialist,
    tool_name_override="escalate_to_specialist",
    on_handoff=log_handoff_event,
)
```

**🧠 Structured Handoff Example:**

```python
class EscalationData(BaseModel):
    reason: str
    order_id: str
```

This forces the LLM to pass `reason` and `order_id` during the transfer.

**🧹 Clean History:**
Use `handoff_filters.remove_all_tools` to give the next agent a clean slate.

**🆚 Handoffs vs Agents-as-tools:**

* 🤝 Handoff → long, multi-turn dialogs; next agent *owns* conversation.
* 🛠 Agent-as-tool → quick subtask; main agent *keeps* control.

**⚠ Tips:**

* Make handoff prompts explicit.
* Sanitize history.
* Use `result.last_agent` to continue conversation with same specialist.

---

## 🧰 **Agents as a Tool**

**📘 Meaning:**
Let one agent **call another like a function** — without losing control.
The *main agent* stays in charge while *specialist agents* do small jobs.

**💡 Why we need it:**

* 🕹 Main agent keeps control.
* 🧩 Modular, reusable sub-agents.
* 🎯 Deterministic orchestration.
* ✍ Clean, focused prompts for each specialist.

**🧠 Analogy:**

* *Handoff* → transfer the call.
* *Agent as a tool* → put call on hold, ask a colleague, then you answer.

**⚙ SDK Support:**
Use `agent.as_tool()` to wrap one agent as a callable tool.
Or use a `@function_tool` that runs another agent via `Runner.run()` for full control.

**📜 Example:**

```python
orchestrator = Agent(
    name="Translator Orchestrator",
    tools=[
        spanish_agent.as_tool("translate_to_spanish", "Translate to Spanish"),
        french_agent.as_tool("translate_to_french", "Translate to French"),
    ],
)
```

**🧠 Advanced Pattern:**
Run a sub-agent *inside* a tool:

```python
@function_tool
async def proofread_text(text: str) -> str:
    result = await Runner.run(proofreader, text, max_turns=3)
    return result.final_output
```

**🧭 Choosing Between:**

| Scenario               | Use              |
| ---------------------- | ---------------- |
| Short, scoped subtasks | 🧰 Agent as Tool |
| Long, focused sessions | 🤝 Handoff       |

**🕵 Gotchas:**

* `model_settings.tool_choice`: `"auto"`, `"required"`, `"none"`, or a specific tool.
* `tool_use_behavior="stop_on_first_tool"` to control loops.
* Use traces to debug tool calls.

---

## 🎛 **Model Settings**

**🎯 What:**
Model settings are like **knobs and dials** controlling your agent’s brain.
Tune creativity, response length, and tool usage.

**🧑‍🍳 Analogy:**

* *Temperature* → creativity
* *Tool Choice* → allow / disallow tools
* *Max Tokens* → response length
* *Parallel Tools* → use multiple tools at once

**⚙ Key Controls:**

1. **Temperature**

   * Low (0.1) = Focused
   * High (0.9) = Creative

   ```python
   ModelSettings(temperature=0.3)
   ```

2. **Tool Choice**

   * `"auto"` – decide automatically
   * `"required"` – must use a tool
   * `"none"` – no tools

3. **Max Tokens**
   Limit response length.

4. **Parallel Tool Calls**
   Run multiple tools together or one-by-one.

**🧪 Examples:**

* 🧮 Math Tutor → `temperature=0.1`
* ✍ Story Writer → `temperature=0.8`
* 🧰 Tool User → `tool_choice="required"`

**🧠 Advanced:**
Adjust `top_p`, `frequency_penalty`, `presence_penalty` for word variety.

**💡 Tips:**

* Start with defaults.
* Change one setting at a time.
* Match settings to task type.

---

## 🏠 Homework

🧩 Explore complete **handoff** module — every detail matters for your quiz!
🖥 Enable **WSL:** [how to enable WSL](https://www.google.com/search?q=how+to+enable+wsl+in+windows+10)
💻 Install [Git Bash](https://git-scm.com/downloads)
🧠 Install [Gemini CLI](https://github.com/google-gemini/gemini-cli)
🤖 Install [Qwen CLI](https://github.com/QwenLM/qwen-code)
🧩 Explore [OpenAI Codex](https://github.com/openai/codex)
🧱 Explore [Spec-Kit-Plus](https://github.com/panaversity/spec-kit-plus)
📖 Read [AgentKit overview](https://openai.com/index/introducing-agentkit/)
