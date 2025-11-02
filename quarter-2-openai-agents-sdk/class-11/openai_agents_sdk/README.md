# Context Management

Context management in the OpenAI Agents SDK refers to handling additional data that your code can use during an agent’s execution. This “context” comes in two main forms:

[Learning Reference](https://openai.github.io/openai-agents-python/context/)

### 1. Local Context

**What It Is:**
Local context is any data or dependencies you pass to your agent's run that your code (tools, lifecycle hooks, etc.) can use. It’s entirely internal and never sent to the LLM.

**How It Works:**
- **Creating Context:**
  You create a Python object—often using a dataclass or a Pydantic model—to encapsulate data like a username, user ID, logger, or helper functions.

- **Passing Context:**
  You pass this object to the run method (e.g., `Runner.run(..., context=your_context)`). The SDK wraps your object in a `RunContextWrapper`, making it available to every tool function, lifecycle hook, or callback during that run via `wrapper.context`.

- **Key Point:**
  All parts of a single agent run must share the same type of context, ensuring consistency.

**Example Use Cases:**
- Storing user details (e.g., a username or ID) that your tools might need.
- Injecting dependencies such as loggers or data fetchers.
- Providing helper functions accessible throughout the run.

*Note:* This local context is not exposed to the LLM. It’s solely for your backend logic and operations.

---

# 🧠 [Sessions](https://openai.github.io/openai-agents-python/sessions/): Making Agents Remember Conversations

## 🎯 What is Session Memory?

Think of **Session Memory** like **giving your agent a notebook** where it writes down everything you talk about. Without session memory, it's like talking to someone with severe amnesia - they forget everything you just said! With session memory, your agent remembers the entire conversation.

### 🧒 Simple Analogy: The Conversation Notebook

Imagine talking to a friend:

- **Without Memory**: "Hi, what's your name?" → "I'm Alice" → "What's your name?" → "I'm Alice" (forgets immediately!)
- **With Memory**: "Hi, what's your name?" → "I'm Alice" → "What state do you live in?" → "I live in California" (remembers I'm Alice!)

Session memory is like giving your agent a perfect memory of your conversation!

## Sessions in OpenAI Agents SDK

The Agents SDK provides built-in session memory to automatically maintain conversation history across multiple agent runs, eliminating the need to manually handle .to_input_list() between turns.

Sessions stores conversation history for a specific session, allowing agents to maintain context without requiring explicit manual memory management. This is particularly useful for building chat applications or multi-turn conversations where you want the agent to remember previous interactions.


---

## 🧠 The Core Concept

**Without Session Memory (Default)**:

```python
# Each conversation is independent - agent forgets everything!
result1 = Runner.run_sync(agent, "What city is the Golden Gate Bridge in?")
# Agent: "San Francisco"

result2 = Runner.run_sync(agent, "What state is it in?")
# Agent: "What are you referring to?" (forgot about San Francisco!)
```

**With Session Memory**:

```python
# Agent remembers the conversation!
session = SQLiteSession("conversation_123")

result1 = Runner.run_sync(agent, "What city is the Golden Gate Bridge in?", session=session)
# Agent: "San Francisco"

result2 = Runner.run_sync(agent, "What state is it in?", session=session)
# Agent: "California" (remembers we were talking about San Francisco!)
```

---

## 🔧 How Session Memory Works

### **The Magic Behind the Scenes**

When you use session memory, the agent automatically:

1. **Before each run**: Retrieves all previous conversation history
2. **During the run**: Processes your new message with full context
3. **After the run**: Saves the new message and response to memory

```python
# What happens automatically:
session = SQLiteSession("user_123")

# Turn 1
result1 = Runner.run_sync(agent, "Hello", session=session)
# Memory now: [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi!"}]

# Turn 2
result2 = Runner.run_sync(agent, "How are you?", session=session)
# Memory loads previous history + adds new messages
# Memory now: [previous messages + new user message + new assistant response]
```

### **Session Storage Options**

| Storage Type          | Code                                     | When to Use                    |
| --------------------- | ---------------------------------------- | ------------------------------ |
| **No Memory**         | `Runner.run_sync(agent, query)`          | Quick tests, one-off questions |
| **Temporary Memory**  | `SQLiteSession("session_id")`            | Current session only           |
| **Persistent Memory** | `SQLiteSession("session_id", "<db...>")` | Save conversations forever     |

---
