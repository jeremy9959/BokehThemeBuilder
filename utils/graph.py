from bokeh.models import HoverTool, Range1d, ColumnDataSource, LabelSet
import graphviz
from bokeh.plotting import figure
from bokeh.models.graphs import from_networkx
from bokeh.models.glyphs import Circle, Oval, MultiLine
import networkx as nx
from itertools import permutations


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
            (x, {"model": M.select_one({"id": x}).__class__.__name__})
            for x, y in T.items()
        ]
    )
    E = [(y, x) for x, y in permutations(T.keys(), 2) if T[x].issubset(T[y])]
    G.add_edges_from(E)
    K = nx.algorithms.dag.transitive_reduction(G)
    nx.set_node_attributes(K, dict(G.nodes(data="model")), "model")
    nx.set_node_attributes(K, "root", "in")
    for id in K.nodes:
        H = M.select_one({"id": id})
        for x in K.neighbors(id):
            for y in H.properties():
                if y in H.properties_containers():
                    if H.select_one({"id": x}) in getattr(H, y):
                        K.nodes[x]["in"] = y
                else:
                    if getattr(H, y) == H.select_one({"id": x}):
                        K.nodes[x]["in"] = y
    return K


def draw_model(M):
    K = make_graph(M)
    plot = figure(title="Structure Graph for Bokeh Model", height=600, width=600)
    plot.xaxis.visible = False
    plot.yaxis.visible = False
    plot.xgrid.visible = False
    plot.ygrid.visible = False

    K.graph["graph"] = {"rankdir": "LR"}

    graph_renderer = from_networkx(
        K, layout_function=nx.nx_pydot.graphviz_layout, prog="dot"
    )
    graph_renderer.node_renderer.glyph = Circle(
        radius=4, fill_alpha=1, fill_color="lightblue"
    )
    graph_renderer.edge_renderer.glyph = MultiLine(line_width=3, line_color="#ababab")
    plot.renderers = [graph_renderer]
    node_hover_tool = HoverTool(
        tooltips=[("id", "@index"), ("model", "@model"), ("in", "@in")]
    )
    plot.add_tools(node_hover_tool)

    x, y = zip(*graph_renderer.layout_provider.graph_layout.values())
    
    xinterval = max(max(x) - min(x),200)
    yinterval = max(max(y) - min(y),200)
    plot.x_range = Range1d(
        start=min(x) - 0.15 * xinterval, end=max(x) + 0.15 * xinterval
    )
    plot.y_range = Range1d(
        start=min(y) - 0.15 * yinterval, end=max(y) + 0.15 * yinterval
    )

    D = {"x": x, "y": y, "model": list(dict(K.nodes(data="model")).values())}
    labels = LabelSet(
        x="x",
        y="y",
        text="model",
        source=ColumnDataSource(D),
        text_font_size="8pt",
        x_offset=-20,
        y_offset=7,
    )
    plot.renderers.append(labels)

    return plot


def agraph_show(M):
    """use graphviz.Source(x) where x=agraph_show(M) to see this in a notebook"""
    K = make_graph(M)
    K.graph["graph"] = {"rankdir": "LR"}
    K.graph["node"] = {"color": "blue", "fillcolor": "lightblue", "style": "filled"}
    K.graph["edge"] = {"dir": "none"}
    A = nx.nx_agraph.to_agraph(K.reverse())
    A.layout("dot")
    for n, d in K.nodes(data=True):
        a = A.get_node(n)
        a.attr.update(
            {
                "label": a.attr["model"] + "\nid=" + a.attr["label"],
                "fontname": "helvetica",
                "fontsize": "10pt",
            }
        )
    return A.to_string()


def agraph_with_edge_labels(M):
    """use graphviz.Source(x) where x=agraph_show(M) to see this in a notebook"""
    K = make_graph(M)
    K.graph["graph"] = {"rankdir": "LR"}
    K.graph["node"] = {"color": "blue", "fillcolor": "lightblue", "style": "filled"}
    K.graph["edge"] = {"dir": "none"}
    A = nx.nx_agraph.to_agraph(K.reverse())
    A.layout("dot")
    for n, d in K.nodes(data=True):
        a = A.get_node(n)
        a.attr.update(
            {
                "label": a.attr["model"] + "\nid=" + a.attr["label"],
                "fontname": "helvetica",
                "fontsize": "10pt",
            }
        )
    return A.to_string()
