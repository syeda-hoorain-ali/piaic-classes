# 🤖 OpenAI Agents SDK Class 3 – 30 August 2025


prompt engeneering
context engeneering


rag = retrival augmented generation, what is it?
ux = user experience
llm = large language model, what is large language model?

precision/recall = (balls in A class should 90, balls in B class should 10, llm put all balls in class A, what is accuracy?, 90%? no, accuracy of class A is 100% and accuracy of class B is 0%, now check average)

diffirence between prompt engeeniring and context engeenering

how llm work? it predict word by word (token) to complete your answer, it first check data that it trained on, if something not available, it searchs internet, if not even on intrnet it give up
hallucinations = giving the data that don't even exists

top_k = top 3 students from every city (even the topper is 25%)
top_p = every student to score above 80%
Top-K: Limits choices to top K most likely tokens
Top-P: Limits choices based on cumulative probability

 Zero-Shot Prompting
The simplest approach—just ask directly without examples.
 One-Shot Prompting
Provide a single example to guide the response format.
Few-Shot Prompting
Provide multiple examples to establish a clear pattern.


system prompt = overall context and behavior guidelines. (like how your parent teach you since you were kid)
user prompt = someone ask you a question
tool schema = every object except you (how to use it)
tool msg = give answer using any object
ai response = you answer direct to that person

CoT - chain of thought - step by step

self consistent = Ask the same question multiple times with different phrasings

step back prompting = Ask a more general question first, then use that context for the specific question, aik prompt k againt koi outline aai, phir us per futher proccessing

re + act = reasoning + actions = reasoning before action, reasoning before calling tool  

Tree of Thoughts (ToT) = Explore multiple reasoning branches simultaneously for complex problems.


MoE = mixture of experts and prompt engeeniring

vectors = value in numbers
  - sparts network: more zero's in digits (9 zero, member 2)
  - dence network: members other than 0 value (9 members, 1 zero) 


MoE vs handoff
1 brain different parts vs different parts



n8n -> code and expressions

# Code and Expressions

[Code in n8n#](https://docs.n8n.io/code/)

[Expressions](https://docs.n8n.io/code/expressions/)

[Check incoming data](https://docs.n8n.io/code/cookbook/expressions/check-incoming-data/)

## Quick cheat sheet

```text
// Current item
{{ $json.foo }}

// Other node
{{ $node["Node Name"].json.bar }}

// Combine text + values
{{ `Hello ${$json.first} ${$json.last}` }}

// Conditional
{{ $json.total > 50 ? 'High' : 'Low' }}

// Arrays
{{ ($json.list || []).filter(x => x.active).length }}

// Date
{{ (new Date($json.timestamp)).toISOString() }}
```


# openai agents sdk

what is uv 
uv installation `pip install uv`
create project `uv init hello_world` or `.` for creaate project in same folder
change dirctory `cd hello_world`
install dependencies `uv add openai-agents python-dotenv`

create agent 
gemini api key https://aistudio.google.com/apikey
dotenv file




https://github.com/panaversity/learn-n8n-agentic-ai/tree/main/00_prompt_engineering
https://github.com/panaversity/learn-n8n-agentic-ai/tree/main/03_code_expressions
https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/01_uv
https://docs.astral.sh/uv/getting-started/installation/
https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/

