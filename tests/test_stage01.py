from app.graph import build_graph


def test_graph_compiles():
    graph = build_graph()
    assert "model" in graph.get_graph().nodes
