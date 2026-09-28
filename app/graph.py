"""build_graph(): all the wiring lives here. You write this file."""
from langgraph.graph import StateGraph, START, END

from app.nodes import call_model
from app.state import State


def build_graph():
    # Stage 1: add the "model" node, connect START -> model -> END, then compile.
    raise NotImplementedError("Stage 1: write the wiring")
