# 🧠 AgentForge

**AgentForge** is a modular AI observability toolkit designed to trace, debug, and evaluate LLM agent runs step-by-step.  
This project helps developers build reliable, transparent multi-agent workflows by enabling trace visualization, memory inspection, and failure simulation.

---

## ✅ Week 1 Scope: Core Trace Infrastructure

### 🚀 Features Built

- ✅ Gemini-powered agent (via LangChain)
- ✅ Tool usage logging (e.g., Wikipedia tool)
- ✅ Step-by-step trace output in JSON format
- ✅ Streamlit dashboard to visualize:
  - Agent metadata
  - Tool inputs and outputs
  - Memory hits (RAG chunks)
- ✅ Failure case templates:
  - Hallucination
  - Tool misuse
  - Irrelevant memory
  - Skipped tools
- ✅ Prompt evaluation script with manual scoring

---

## 🛠️ How to Run

### 1. 📦 Install Dependencies

```bash
pip install streamlit langchain langchain-google-genai langsmith wikipedia
```
### 2. 🔑 Set Gemini API Key
``` bash 
export GOOGLE_API_KEY=your_api_key_here  # or set in Python
```

### 3. ▶️ Run the Streamlit Dashboard
``` bash 
streamlit run agentforge_dashboard.py
```

### 4. 📁 Upload a Trace
Upload any of the JSON files from /traces or /failures to visualize agent reasoning.


# 🧭 Next Steps (Week 2 Preview)
- Agent Replay + Patch Mode

- Prompt A/B Testing Dashboard

- Automated Evaluation & Self-Fix Pipeline
