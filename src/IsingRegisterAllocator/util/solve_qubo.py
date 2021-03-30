from amplify import Solver, decode_solution
from amplify.client import FixstarsClient
import numpy as np

def by_amplify(qubits, model, token, timeout=5000):
    client = FixstarsClient()
    client.token = token
    client.parameters.timeout = timeout
    solver = Solver(client)
    solver.filter_solution = False
    result = solver.solve(model)
    values = result[0].values
    q_values = decode_solution(qubits, values, 1)
    return np.where(np.array(q_values) == 1)[1]
