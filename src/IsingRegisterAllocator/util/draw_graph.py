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

def main():
    list_dependent_variables = [
        [1, 2, 3],
        [0, 2, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 4],
        [1, 2, 3],
        [6],
        [5]
    ]
    allocation = [1, 0, 2, 2, 1, 2, 1]

    draw_graph(list_dependent_variables, allocation)
    # draw_graph(list_dependent_variables)

if __name__ == "__main__":
    main()