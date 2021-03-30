import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(list_dependent_variables, allocation=None):
    G = nx.Graph()
    for i, interference in enumerate(list_dependent_variables):
        G.add_node(i)
        for x in interference:
            G.add_edge(i, x)

    if allocation == None:
        nx.draw_networkx(G)
    else :
        nx.draw_networkx(G, node_color = allocation)
    plt.show()
