from amplify import Solver, decode_solution
from amplify.client import FixstarsClient
import numpy as np

def by_amplify(qubits, model, timeout=5000):
    client = FixstarsClient()
    client.parameters.timeout = timeout
    solver = Solver(client)
    result = solver.solve(model)
    values = result[0].values
    q_values = decode_solution(q, values, 1)
    return np.where(np.array(q_values) == 1)[1]