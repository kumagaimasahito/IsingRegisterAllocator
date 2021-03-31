import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

def draw_graph(list_dependent_variables, allocation=None):
    G = nx.Graph()
    list_nodes = []
    list_edges = []

    if allocation != None:
        to_index = {k: i for i, k in enumerate(Counter(allocation).keys())}

    for i, interference in enumerate(list_dependent_variables):
        if allocation == None:
            list_nodes.append((i, {"color" : "lightblue"}))
        else:
            list_nodes.append((i, {"color" : to_index[allocation[i]]}))

        for x in interference:
            if allocation == None:
                list_edges.append((i, x, {"color" : "black"}))
            else:
                if allocation[i] == allocation[x]:
                    list_edges.append((i, x, {"color" : "red"}))
                else:
                    list_edges.append((i, x, {"color" : "black"}))
    
    G.add_nodes_from(list_nodes)
    G.add_edges_from(list_edges)
    node_color = [node["color"] for node in G.nodes.values()]
    edge_color = [edge["color"] for edge in G.edges.values()]

    fig = plt.figure()
    pos = nx.circular_layout(G)
    if allocation == None:
        nx.draw_networkx(G, pos, edge_color=edge_color, node_color=node_color)
    else :
        cm = plt.cm.get_cmap('hsv')
        nx.draw_networkx(G, pos, cmap=cm, edge_color=edge_color, node_color=node_color)
    plt.show()

# def draw_graph(list_dependent_variables, allocation=None):
#     G = nx.Graph()
#     for i, interference in enumerate(list_dependent_variables):
#         G.add_node(i)
#         for x in interference:
#             G.add_edge(i, x)

#     pos = nx.circular_layout(G)
#     if allocation == None:
#         nx.draw_networkx(G, pos)
#     else :
#         to_index = {k: i for i, k in enumerate(Counter(allocation).keys())}
#         cm = plt.cm.get_cmap('hsv')
#         colors = [to_index[al] for al in allocation]
#         nx.draw_networkx(G, pos, cmap=cm, node_color=colors)
#     plt.show()
