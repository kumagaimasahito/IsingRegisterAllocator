from IsingRegisterAllocator.util import get_qubo

def test_util_get_qubo_by_amplify():
    list_dependent_variables = [
        [1, 2, 3],
        [0, 2, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 4],
        [1, 2, 3],
        [6],
        [5]
    ]
    num_registers = 3

    get_qubo.by_amplify(list_dependent_variables, num_registers)