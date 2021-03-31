from IsingRegisterAllocator.util import draw_graph

def test_util_draw_graph_allocated():
    list_dependent_variables = [
        [1, 2, 3, 8, 9, 10, 11, 12, 14, 16, 17, 19],
        [0, 7, 8, 9, 10, 11, 16, 19],
        [0, 5, 10, 11, 19],
        [0, 7, 8, 9, 10, 11, 16, 19],
        [7, 8, 9, 10, 11, 16, 19],
        [7, 8, 9, 10, 11, 16, 19],
        [12, 13],
        [1, 3, 4, 5],
        [0, 1, 3, 4, 5],
        [0, 1, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 6],
        [6],
        [0, 18],
        [19],
        [0, 1, 3, 4, 5],
        [0],
        [14],
        [0, 1, 2, 3, 4, 5, 15]
    ]
    allocation = [14, 21, 22, 25, 29, 22, 31, 28, 18, 26, 19, 28,  3, 32, 27, 29, 28,
        5, 22, 23]

    draw_graph(list_dependent_variables, allocation)

# if __name__ == "__main__":
#     test_util_draw_graph_allocated()