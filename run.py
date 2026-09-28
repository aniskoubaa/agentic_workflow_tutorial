from langchain_core.messages import HumanMessage
from app.graph import build_graph

graph = build_graph()

while True:
    question = input("you> ").strip()
    if question in {"exit", "quit"}:
        break
    result = graph.invoke({"messages": [HumanMessage(question)]})
    print("agent>", result["messages"][-1].content)
