from .util import split_unit, get_qubo
from .util.solve_qubo import by_amplify as solve_qubo

def get_solution_limited_unit(interference, num_registers, limitation, token):
    response = get_qubo.by_amplify_limited(interference, num_registers, limitation)
    solution = solve_qubo(response["qubits"], response["model"], token)
    return solution