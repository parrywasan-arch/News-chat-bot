from typing import TypedDict, List

class State(TypedDict):
    input: str
    decision: str
    output: str
    history: List[str]
    sentiment: str
    fact_check: str
    error: str
