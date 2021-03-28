from amplify import Solver, decode_solution
from amplify.client import FixstarsClient
import numpy as np
from . import config

def by_amplify(qubits, model, timeout=5000):
    client = FixstarsClient()
    client.token = config.AMPLIFY_TOKEN
    client.parameters.timeout = timeout
    solver = Solver(client)
    solver.filter_solution = False
    result = solver.solve(model)
    values = result[0].values
    q_values = decode_solution(qubits, values, 1)
    return np.where(np.array(q_values) == 1)[1]

def main():
    import get_qubo
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

    response = get_qubo.by_amplify(list_dependent_variables, num_registers)
    ans = by_amplify(response["qubits"], response["model"])
    print(ans)

if __name__ == "__main__":
    main()