from bokeh.models import HoverTool, Range1d, ColumnDataSource, LabelSet
import graphviz
from bokeh.plotting import figure
from bokeh.models.graphs import from_networkx
from bokeh.models.glyphs import Oval
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


def draw_model(M):
    G = make_graph(M)
    K = hasse(G)
    for n in K.nodes:
        del K.node[n]["s"]

    plot = figure(title="Structure Graph for Bokeh Model", height=600, width=600)
    plot.xaxis.visible = False
    plot.yaxis.visible = False
    plot.xgrid.visible = False
    plot.ygrid.visible = False

    K.graph["graph"] = {"rankdir": "LR"}
    K.graph["nodes"] = {"color": "green"}

    graph_renderer = from_networkx(
        K.reverse(), layout_function=nx.nx_pydot.graphviz_layout, prog="dot"
    )
    graph_renderer.node_renderer.glyph = Oval(
        height=20, width=10, fill_alpha=1, fill_color="lightblue"
    )
    plot.renderers = [graph_renderer]
    node_hover_tool = HoverTool(tooltips=[("id", "@index"), ("kind", "@kind")])

    plot.add_tools(node_hover_tool)

    x, y = zip(*graph_renderer.layout_provider.graph_layout.values())
    xinterval = max(x) - min(x)
    yinterval = max(y) - min(y)
    plot.x_range = Range1d(
        start=min(x) - 0.15 * xinterval, end=max(x) + 0.15 * xinterval
    )
    plot.y_range = Range1d(
        start=min(y) - 0.15 * yinterval, end=max(y) + 0.15 * yinterval
    )
    D = {"x": x, "y": y, "kind": list(dict(K.nodes(data="kind")).values())}
    
    source = ColumnDataSource(D)
    labels = LabelSet(
        x="x",
        y="y",
        text="kind",
        source=source,
        text_font_size="8pt",
        x_offset=-20,
        y_offset=7,
    )
    plot.renderers.append(labels)
    return plot

def agraph_show(M):
    """use graphviz.Source(x) where x=agraph_show(M) to see this in a notebook"""
    G = make_graph(M)
    K = hasse(G)
    for n in K.nodes:
        del K.node[n]['s']
    K.graph['graph']={'rankdir':'LR'}
    K.graph['node']={'color':'blue','fillcolor':'lightblue','style':'filled'}
    K.graph['edge']={'dir':'none'}
    A=nx.nx_agraph.to_agraph(K.reverse())
    A.layout('dot')
    for n, d in K.nodes(data=True):
        a = A.get_node(n)
        a.attr.update({'label': a.attr['kind']+'\nid='+a.attr['label'],'fontname':'helvetica','fontsize':'10pt'})
    return A.to_string()


def hasse_with_edge_labels(model):
    K = hasse(make_graph(model))
    for id in list(K.nodes):
        H = model.select_one({'id':id})
        for x in list(K.reverse().neighbors(id)):
            for y in H.properties():
                if y in H.properties_containers():
                    if H.select_one({'id':x}) in getattr(H,y):
                        K.edges[(x,id)]['label']=y
                else:
                    if getattr(H,y) == H.select_one({'id':x}):
                        K.edges[(x,id)]['label']=y
    return K

def agraph_with_edge_labels(M):
    """use graphviz.Source(x) where x=agraph_show(M) to see this in a notebook"""
    K = hasse_with_edge_labels(make_graph(M))
    for n in K.nodes:
        del K.node[n]['s']
    K.graph['graph']={'rankdir':'LR'}
    K.graph['node']={'color':'blue','fillcolor':'lightblue','style':'filled'}
    K.graph['edge']={'dir':'none'}
    A=nx.nx_agraph.to_agraph(K.reverse())
    A.layout('dot')
    for n, d in K.nodes(data=True):
        a = A.get_node(n)
        a.attr.update({'label': a.attr['kind']+'\nid='+a.attr['label'],'fontname':'helvetica','fontsize':'10pt'})
    return A.to_string()
