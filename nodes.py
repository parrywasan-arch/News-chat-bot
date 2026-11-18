from tools import llm

def router_node(state):
    query = state["input"].lower()

    if "news" in query:
        state["decision"] = "news"
    else:
        state["decision"] = "chat"

    return state


def news_node(state):
    response = llm.invoke(
        f"Give latest news about {state['input']}"
    )

    state["output"] = response.content
    return state


def chat_node(state):
    try:
        history_text = "\n".join(state["history"])

        prompt = f"""
        Previous conversation:
        {history_text}

        Current question:
        {state['input']}
        """

        response = llm.invoke(prompt)

        state["output"] = response.content

    except Exception as e:
        state["error"] = str(e)

    return state


def sentiment_node(state):
    prompt = f"""
    Analyze the sentiment of the following text.
    Return only one word:

    Positive
    Negative
    Neutral

    Text:
    {state['output']}
    """

    response = llm.invoke(prompt)

    state["sentiment"] = response.content.strip()
    return state


def fact_check_node(state):
    prompt = f"""
    Review the following text and classify it as:

    Reliable
    Needs Verification
    Uncertain

    Return only one option.

    Text:
    {state['output']}
    """

    response = llm.invoke(prompt)

    state["fact_check"] = response.content.strip()
    return state


def memory_node(state):
    state["history"].append(state["input"])
    return state


def error_handler_node(state):
    if state["error"]:
        state["output"] =sentiment_node
        f"Error: {state['error']}"

    return state

def response_node(state):
    return state
