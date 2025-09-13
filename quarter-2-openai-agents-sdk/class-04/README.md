# 🤖 OpenAI Agents SDK Class 4 - 13 September 2025

This session focused on **prompt engineering**, **image prompting**, and hands-on practice with **OpenAI Agents SDK**.

---

## **🍌 Nano Banana**

* Google’s AI image generation model 
* **Test it here:** [gemini.google.com](https://gemini.google.com/)

**Core Principles for Image Prompts:**

1. **Specificity:** Use detailed descriptions (subject, pose, background, lighting)
2. **Visual Hierarchy:** Subject → environment → lighting → style
3. **Photography Language:** Mention lens, lighting (Rembrandt light), and style (editorial, cinematic)
4. **Branding Elements:** Add logos, text overlays, extra objects for personal branding
5. **Iterate in Layers:** Start broad, refine step-by-step (pose, props, mood)

> 📕 **Full Guide:** [Image Prompting Guide](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering/image_generation)

---

## **🧠 Prompt Engineering Deep Dive**

* **MoE (Mixture of Experts):** Clear, domain-specific prompts activate the right experts
* **CoT (Chain of Thought):** “Let’s think step by step” for reasoning
* **ToT (Tree of Thoughts):** Explore multiple solutions, combine best results
* **Self-Consistency:** Generate multiple reasoning paths, pick most common answer
* **Step-Back Prompting:** Start broad, then go specific
* **ReAct (Reason + Act):** Combine reasoning with actions (e.g., web search, tools)

> 📕 **Full Guide:** [Prompt Engineering Repo](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering)

---

## **6️⃣ The 6-Part Prompting Framework**

1. **Command:** Clear action verbs (“Analyze”, “Create”, “Recommend”)
2. **Context:** Provide details (who, what, when, constraints)
3. **Logic:** Specify output structure: table, list, checklist, JSON
4. **Roleplay:** Tell AI who it is (“You are a senior data scientist…”)
5. **Formatting:** Request organized, scannable output
6. **Questions:** End with “Ask me 10 questions to make this better”

> 💡 **Pro Tip:** Iterate until AI stops asking new questions — then you have enough context.

> 📕 **Full Guide:** [6-Part Prompting Framework](https://github.com/panaversity/learn-low-code-agentic-ai/blob/main/00_prompt_engineering/six_part_prompting_framework.md)

---

## 4. **Hands-On with OpenAI Agents SDK**

### 🔑 Get Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **Create API key**
3. Copy the key and store securely

### 🛠 Install `uv` (Package Manager)

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🖥 Basic Commands

```bash
uv init hello_world     # initialize project
cd hello_world          # change directory 
uv run main.py          # or activate .venv/Scripts/activate.bat first
uv add openai-agents python-dotenv # install dependencies
uv run main.py          # run code
```

Create `.env` file:

```env
GEMINI_API_KEY="paste-your-key-here"
```

---

### 5. **Model Configurations**

Three levels of configuration:

* **Agent Level:** Applies to one agent only
* **Run Level:** Overrides settings for every agent in a single run
* **Global Level:** Defaults for all agents

> 📕 **Full Guide:** [Model Configurations](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/05_model_configuration)

---

## 📕 Resources & Repos

* **[Class Code & Notes](https://github.com/syeda-hoorain-ali/piaic-classes/tree/main/quarter-2-openai-agents-sdk/class-04)**
* **[Image Prompting Guide](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering/image_generation)**
* **[Prompt Engineering Repo](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering)**
* **[6-Part Prompting Framework](https://github.com/panaversity/learn-low-code-agentic-ai/blob/main/00_prompt_engineering/six_part_prompting_framework.md)**
* **[Learn-Agentic-AI Repo](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/)**

---

## ✅ Key Takeaways

* Clearer prompts = better outputs
* 6-Part Framework ensures consistent results
* Image prompts work best with **subject + environment + style + technical details**
* SDK configs let you fine-tune behavior at agent/run/global levels
* Secure your API keys and `.env` files before sharing projects
