from langgraph.graph import StateGraph, END
from state import State
from nodes import router_node, news_node, chat_node, memory_node, sentiment_node, fact_check_node,response_node
builder = StateGraph(State)

builder.add_node("router", router_node)
builder.add_node("news", news_node)
builder.add_node("chat", chat_node)
builder.add_node("memory", memory_node)
builder.add_node("sentiment_analysis", sentiment_node)
builder.add_node("fact_checker", fact_check_node)
builder.add_node("response", response_node)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    lambda state: state["decision"],
    {
        "news": "news",
        "chat": "chat"
    }
)

builder.add_edge("news", "sentiment_analysis")
builder.add_edge("chat", "sentiment_analysis")
builder.add_edge("sentiment_analysis", "fact_checker")
builder.add_edge("fact_checker", "response")
builder.add_edge("response", "memory")
builder.add_edge("memory", END)

graph = builder.compile()
