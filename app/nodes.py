"""Node functions. Each node returns an update (a dict), not the whole state."""
from app.llm import model
from app.state import State


def call_model(state: State) -> dict:
    reply = model.invoke(state["messages"])
    return {"messages": [reply]}
