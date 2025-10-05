# 🤖 OpenAI Agents SDK – Class 7 (4 October 2025)

**Tools**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")](https://colab.research.google.com/drive/1sJt3aTk6Xnd-R0WgfzrzdAE8vFinEflS?usp=sharing)  
**Handoff**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")](https://colab.research.google.com/drive/1PB_k03WMAxpVykyknAMtXhpv1QFU8uoj?usp=sharing)

---

## 🚀 Topic: Tools in Agents SDK

Agents become powerful when they can **use tools** — to fetch data, perform actions, or call other agents.

### 🔧 3 Types of Tools

1. **🌐 Hosted Tools**  
   OpenAI offers a few built-in tools when using the paid OpenAI API key.
   - `Web Search Tool` lets an agent search the web.
   - `File Search Tool` allows retrieving information from your OpenAI Vector Stores.
   - `Computer Tool` allows automating computer use tasks.
   - `Code Interpreter Tool` lets the LLM execute code in a sandboxed environment.
   - `Hosted MCP Tool` exposes a remote MCP server's tools to the model.
   - `Image Generation Tool` generates images from a prompt.
   - `Local Shell Tool` runs shell commands on your machine.

2. **🧩 Function Tools**  
   - You can use any Python function as a tool.  
   - Fast, easy to debug, perfect for logic or math tasks.

3. **🤖 Agent as Tool**  
   - One agent used as a tool for another (nested agents).  
   - Enables modular systems — **Orchestrator → Sub-agents**.  
   - Example: “Main agent” delegates tasks to specialized “domain agents”.

---

## 🎛️ Orchestrator & Handoff

- **🧠 Orchestrator** = agent managing sub-agents (decides *who does what*).  
- **🔁 Handoff** = passing control or context to another agent.  

Example:  
Trige Agent → detects "agentic ai topic" → hands off → Agentic AI Expert.

---

## ✍️ Docstrings (Homework)

Docstrings = documentation inside code.
Used for explaining purpose, inputs, and outputs.

```python
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"
```

✅ Improves readability
✅ Helps teammates & models understand code
✅ Generates auto-docs

---

## 🔗 References

* [📗 Class Code & Notes](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/05_model_configuration)
* [⚙️ Model Configuration](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/05_model_configuration)
* [🧰 Basic Tools](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/06_basic_tools)
* [🤝 Agents as Tool](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/13_agents_as_tool)
* [🔄 Basic Handoff](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/14_basic_handsoff)
* [🧠 Advanced Tools](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/15_advanced_tools)

