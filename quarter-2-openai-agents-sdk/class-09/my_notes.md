# 🤖 OpenAI Agents SDK – Class 9 (19 October 2025)

https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus
ide for coding
wsl window sub-system for linux

1st markdown
2nd git for version control
3rd ai cli (gemini, codex, claude sonnet)


4th mcp
5th test driven development



what is docker image // copy all steps
orchestration with Kubernetes // group of systems // clustors
micro services // facebook // 1. like, 2. streaming, 3. post, 4. comment
dapr // to manage all micro services // run one more container with docer container in system
ray // distributing computing // make 50 computers 1 system and manage it like single




microsoft make it's new package: "spec-kit"
panaversity fored it to enhance it
just like vs code to cursor



┌─────────────────────────────────────────────────────────────────┐
│              AI-Driven Development (AIDD) Workflow              │
└─────────────────────────────────────────────────────────────────┘

PHASE 1: SPECIFICATION (Pillars 1, 6)
   │
   ├─→ Write system requirements in spec.md (Markdown)
   ├─→ Define agent behaviors and protocols using SDD+ templates
   ├─→ Define org standards in constitution.md
   └─→ Version control all specs with Git (Pillar 2)
   │
   ▼
PHASE 2: IMPLEMENTATION (Pillars 3, 4, 5)
   │
   ├─→ Use an AI CLI (Gemini, Codex, Claude) to interpret specs
   ├─→ Coding Agent writes tests first (TDD) to match acceptance criteria
   ├─→ Coding Agent generates implementation code to pass tests
   └─→ Coding Agent interacts with envirnoment via MCP plugins
   │
   ▼
PHASE 3: INTEGRATION & VALIDATION (Pillar 2)
   │
   ├─→ CI pipeline on GitHub Actions is triggered
   ├─→ Lints specs, runs all tests, checks for spec alignment
   ├─→ Human developer reviews the pull request (spec + code)
   └─→ "No green, no merge" policy enforced
   │
   ▼
PHASE 4: DEPLOYMENT & ORCHESTRATION (Pillar 7)
   │
   ├─→ Build Docker containers for agents and services
   ├─→ Deploy to a Kubernetes cluster
   ├─→ Manage state and communication with Dapr
   └─→ Scale compute tasks with Ray







///////////////////////////////////////


Window button -> task manager   (if you don't see complete panel click "More details") -> performance -> visulaization

bios setting -> enable virtulaization

Window button - turn windows feature on and off -> check virtule machine plateform -> ok -> restart your system


search wsl -> black
- open power shell
- run "wsl --status"
- run "wsl --install -d Ubuntu" // we are installing operating system named "ubuntu" in windows
- write you name in account and password // make sure to save it

now check if wsl icon is turned blue -> open it

https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus/01a_ai_cli/01_big_free_tiers
https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718

install nodejs
node --version /node -v // versionshould be above 20

npm install -g @google/gemini-cli
gemini -v

on wsl : sudo snap install gemini


//////////////////////////////
https://github.com/panaversity/spec-kit-plus

spec-kit -> spec = specifications

install uv in wsl/ubuntu
uv installation guide: https://docs.astral.sh/uv/getting-started/installation/
open cmd -> run "wsl" this will open wsl in command prompt
in wsl : curl -LsSf https://astral.sh/uv/install.sh | sh
install "uv tool install specifyplus"


goto directory: run "specifyplus init speckit_hello_world" #or "sp init speckit_hello_world"
If you’re inside the folder already: "specifyplus init ."
choose you ai assistant if gemini install "gemini", if qwen install select "qwen"
choose script type "sh" means bash for linux and "ps" means powershell for window: choose "sh"
run -> /sp.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
run -> /sp.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
run -> /sp.clarify
run -> /sp.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
run -> /sp.tasks
run -> /sp.analyze
run /sp.implement

////////////////////////////

flags
slash commands are send to ai cli

in constitution folder we write rules


/////////////////////////
slash commands
/sp.constitution = Define your project rules
/sp.specify = Describe what to build
/sp.plan = Make a build plan
/sp.implement = Generate code files

////////////////////////////////
simple commands for linux
change folder
create folder
go back one folder
check what is in current directory
change drive

/////////////////////////////////////

goal to achieve create login/signup with fastapi using sqlite for backend

on cmd write "wsl"
cd /mnt/e
mkdir hello_world
cd hello_world
gemini / qwen
prompt "create a login managment system with sqlite and html, cs"





///////////////////////////
guardrails in openai agents sdk
https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/18_guardrails

class code: https://colab.research.google.com/drive/1pQCYRMO922Vo2jXin_Q3io8sbugNtKM8?usp=sharing



