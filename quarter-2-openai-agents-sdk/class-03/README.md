# 🤖 OpenAI Agents SDK Class 3 - 30 August 2025

This document summarizes everything we covered in our third class, focusing on **Prompt Engineering**, **Context Engineering**, LLM fundamentals, and the **OpenAI Agents SDK**.

---

## 1. Key Concepts

### Prompt Engineering

* **What it is:** Crafting instructions (prompts) so AI models produce better results.
* **Goal:** Tell the model *how* to behave and *what* to produce.

### Context Engineering

* **What it is:** Supplying the model with the right *information* for accurate answers.
* **Goal:** Give the model the *facts/examples* it should rely on.

**One-liner:**

> Prompt Engineering = *How you ask*
> Context Engineering = *What you show*

---

### Retrieval-Augmented Generation (RAG)

RAG helps models fetch information from external sources (like documents or knowledge bases) before answering—reducing hallucinations.

---

### Large Language Model (LLM)

* LLMs predict text **word by word (token by token)**.
* They use training data first; if not found, they may search online; if still unavailable, they stop or hallucinate.
* Example: ChatGPT, Claude, Gemini.

---

### UX – User Experience

How users interact with your AI system: smooth, intuitive, and useful.

---

## 2. AI Vocabulary Cheat Sheet

| Term                         | Meaning                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| **Hallucinations**           | AI confidently giving wrong or fake information                                    |
| **Top-K**                    | Pick top *K* most likely words (e.g., top 3 students per city)                     |
| **Top-P**                    | Pick words until cumulative probability hits *P* (e.g., all students scoring >80%) |
| **Zero-Shot**                | Just ask the question, no examples                                                 |
| **One-Shot**                 | Give one example before asking                                                     |
| **Few-Shot**                 | Give multiple examples to guide the model                                          |
| **CoT (Chain of Thought)**   | Step-by-step reasoning                                                             |
| **Self-Consistency**         | Ask multiple times, choose the most common answer                                  |
| **Step-Back Prompting**      | Start broad → then ask specifics                                                   |
| **ReAct (Reason + Act)**     | Think first, then use tools/actions                                                |
| **ToT (Tree of Thoughts)**   | Explore multiple solution branches before deciding                                 |
| **MoE (Mixture of Experts)** | One model with specialized parts (experts)                                         |

---

## 3. Prompting Techniques

### System vs User Prompts

* **System Prompt:** Rules + personality for the AI (like parental guidance).
* **User Prompt:** Actual user question.

---

### Reasoning Styles

1. **Chain of Thought (CoT):** Think step by step.
2. **Self-Consistency:** Ask in different ways → pick the common answer.
3. **Step-Back Prompting:** Start general → go specific.
4. **ReAct:** Reason + use tools.
5. **Tree of Thoughts (ToT):** Explore multiple options → pick the best one.

---

## 4. Accuracy Metrics

* **Precision:** Out of all positive predictions, how many are correct?
* **Recall:** Out of all actual positives, how many did we catch?
* **Example:**

  * 90 balls in A, 10 in B.
  * LLM puts all balls in A → A = 100%, B = 0%, Average = 50%.

---

## 5. Working with n8n

* **Expressions**: Dynamic code in workflows using `{{ }}` syntax.
* Examples:

  ```text
  {{ $json.name }}               → Access a field  
  {{ $json.price * $json.qty }}   → Do math  
  {{ $json.total > 100 ? 'VIP' : 'Regular' }} → Conditional  
  ```
* Use `$node["NodeName"].json.data` for data from other nodes.

**Cheat sheet:**

* Strings + math
* Conditionals
* Arrays & objects
* Dates & formatting

---

## 6. OpenAI Agents SDK Basics

### Installation

```bash
pip install uv                        # install uv
uv init hello_world                   # create project
cd hello_world                        # go to folder
uv add openai-agents python-dotenv    # install dependencies
uv run main.py                        # run the code
```

### Setup

* Create `.env` file with your API keys.
* Example for **Gemini API key**: [Get key here](https://aistudio.google.com/apikey)

---

## 7. MoE vs Handoff

* **MoE:** One brain with multiple specialized parts.
* **Handoff:** Different tasks → different models or systems.

---

## 8. Key Links

* [Prompt Engineering Guide](https://github.com/panaversity/learn-n8n-agentic-ai/tree/main/00_prompt_engineering)
* [n8n Expressions](https://docs.n8n.io/code/expressions/)
* [UV Installation](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/01_uv/)
* [OpenAI Agents SDK Setup](https://github.com/panaversity/learn-agentic-ai/blob/main/01_ai_agents_first/04_hello_agent/)

