from utils import disassemble, explode, obj_props_to_df2
from bokeh.models import Plot
from bokeh.plotting import Figure
import networkx as nx
from itertools import permutations
import graphviz
import matplotlib.pyplot as plt


def tree(M):
    d = {}
    for m in M.references():
        d[m.id] = set([y.id for y in m.references()])
    return d


def make_graph(M):
    G = nx.DiGraph()
    T = tree(M)
    G.add_nodes_from(
        [
            (x, {"s": y, "kind": M.select_one({"id": x}).__class__.__name__})
            for x, y in T.items()
        ]
    )
    E = [(y, x) for x, y in permutations(T.keys(), 2) if T[x].issubset(T[y])]
    G.add_edges_from(E)
    return G


def leaves(G):
    return [x for x, y in G.in_degree() if y == 0]


def minimal_elements(G):
    return [x for x, y in G.in_degree() if y == 0]


def hasse(G):
    levels = {}
    H = G.copy()
    i = 0
    while len(H.nodes) > 0:
        roots = minimal_elements(H)
        levels[i] = roots
        i += 1
        H.remove_nodes_from(roots)
    K = nx.DiGraph()
    K.add_nodes_from(G.nodes(data=True))
    for j in range(i - 1, 0, -1):
        for n in levels[j]:
            for m in levels[j - 1]:
                if G.node[n]["s"].issubset(G.node[m]["s"]):
                    K.add_edge(n, m)
    return K


def plot_graph(K):
    node_labels = nx.get_node_attributes(K, "kind")
    P = nx.nx_pydot.graphviz_layout(K.reverse(), prog="dot")
    nx.draw_networkx(K, P, arrows=False, labels=node_labels)
