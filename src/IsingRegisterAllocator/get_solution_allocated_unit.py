from .util import split_unit, get_qubo
from .util.solve_qubo import by_amplify as solve_qubo

def get_solution_allocated_unit(interference, register_unit, unit_size, token):
    interference_unit = split_unit(interference, register_unit)
    index_table = []
    ans_table = []

    for unit_i, unit in enumerate(interference_unit):
        to_index = {k: i for i, k in enumerate(unit.keys())}
        to_var = {i: k for i, k in enumerate(unit.keys())}

        if len(unit) == 1:
            ans = [0]
        else :
            interference_converted = [
                [
                    to_index[v]
                    for v in values
                ]
                for values in unit.values()
            ]
            response = get_qubo.by_amplify(interference_converted, unit_size[unit_i])
            ans = solve_qubo(response["qubits"], response["model"], token)

        if 0 < unit_i:
            ans = [i + sum(unit_size[:unit_i]) for i in ans]

        index_table.append(to_var)
        ans_table.append(ans)

    solution = [0] * len(interference)
    for unit_i, unit_ans in enumerate(ans_table):
        for i, x in enumerate(unit_ans):
            solution[index_table[unit_i][i]] = x
    
    return solution