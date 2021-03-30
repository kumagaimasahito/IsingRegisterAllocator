from IsingRegisterAllocator.util import get_qubo

def test_util_get_qubo_by_amplify_limited():
    list_dependent_variables = [
        [1, 2, 3],
        [0, 2, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 4],
        [1, 2, 3],
        [6],
        [5]
    ]
    num_registers = 4
    limitation = {1:[2, 3], 3:[0, 1, 2]}

    solution = get_qubo.by_amplify_limited(list_dependent_variables, num_registers, limitation)
#     print(solution)

# if __name__ == "__main__":
#     test_util_get_qubo_by_amplify_limited()