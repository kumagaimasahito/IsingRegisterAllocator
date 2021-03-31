from IsingRegisterAllocator.util import draw_graph

def test_util_draw_graph():
    graph = [
        [0,0,0,1,0,1,1,1,1,0,],
        [0,0,0,0,0,1,1,0,0,0,],
        [0,0,0,0,0,0,0,0,0,0,],
        [1,0,0,0,1,0,0,1,1,0,],
        [0,0,0,1,0,0,0,0,0,0,],
        [1,1,0,0,0,0,1,0,0,0,],
        [1,1,0,0,0,1,0,0,0,0,],
        [1,0,0,1,0,0,0,0,0,0,],
        [1,0,0,1,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,0,],
    ]
    list_dependent_variables = [
        [
            i
            for i, x in enumerate(g)
            if x==1
        ]
        for g in graph
    ]
    draw_graph(list_dependent_variables)

# if __name__ == "__main__":
#     test_util_draw_graph()