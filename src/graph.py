import networkx as nx

from data.drugs import DRUGS, Role

ENZYME = "CYP3A4"


def build_graph():
    graph = nx.DiGraph()
    graph.add_node(ENZYME, kind="enzyme")
    for drug in DRUGS:
        graph.add_node(drug.name, kind="drug")
        graph.add_edge(
            drug.name,
            ENZYME,
            role=drug.role,
            strength=drug.strength,
            sensitive=drug.sensitive,
        )
    return graph