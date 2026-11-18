# NewsBot — Multi-Node Agentic AI Assistant (LangGraph + Azure OpenAI)

**NewsBot** is a 7-node Agentic AI application built with **LangGraph**, **Azure OpenAI**, and **Streamlit**. It routes user queries between news and general chat workflows, classifies response sentiment (`Positive`, `Negative`, `Neutral`), runs a reliability fact-check (`Reliable`, `Needs Verification`, `Uncertain`), and tracks conversation history with built-in error handling.

## Workflow Architecture

```mermaid```
flowchart TD
    START([User Input]) --> R[router: Keyword Intent Routing]
    R -->|contains 'news'| N[news: Generate News Response]
    R -->|general query| C[chat: Context-Aware LLM Chat]
    N --> S[sentiment_analysis: Positive / Negative / Neutral]
    C --> S
    S --> F[fact_checker: Reliable / Needs Verification / Uncertain]
    F --> RES[response: Prepare Final Output]
    RES --> M[memory: Append Input to History]
    M --> FINISH([END])

#Key Features
Intent Routing (router_node): Inspects incoming queries and routes requests containing "news" to news_node, while routing general queries to chat_node.
Context-Aware Chat & Error Handling (chat_node): Incorporates conversation history into the LLM prompt and captures runtime exceptions into state["error"] for clean UI error display in Streamlit.
Automated Sentiment Analysis (sentiment_node): Classifies generated responses into Positive, Negative, or Neutral.
Reliability Guardrail (fact_check_node): Evaluates output credibility as Reliable, Needs Verification, or Uncertain before displaying results.
Dual Interfaces (App.py & main.py): Run either through an interactive Streamlit web UI or directly via CLI

#Project Structure
App.py — Streamlit web interface displaying the response, sentiment, fact-check status, and error alerts
graph.py — LangGraph StateGraph definition, conditional routing edges, and workflow compilation
nodes.py — Implementation of router_node, news_node, chat_node, sentiment_node, fact_check_node, response_node, and memory_node
tools.py — Configures AzureChatOpenAI using python-dotenv environment variables
state.py — TypedDict schema (input, decision, output, history, sentiment, fact_check, error)
main.py — Terminal entry point for testing graph execution
requirements.txt — Python package dependencies
