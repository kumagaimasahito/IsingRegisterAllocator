from IsingRegisterAllocator.util import draw_graph

def test_util_draw_graph_allocated():
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