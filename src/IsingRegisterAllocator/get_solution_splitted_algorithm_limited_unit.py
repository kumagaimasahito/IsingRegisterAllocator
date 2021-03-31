from .util import get_qubo
from .util.solve_qubo import by_amplify as solve_qubo

def get_solution_splitted_algorithm_limited_unit(interference, num_registers, limitation, chunk_size, overlap_size, token):
    num_variables = len(interference)

    def resize_chunk(interference, dep, arr):
        list_chunk = interference[dep:arr]
        list_chunk_resized = [
            [
                i - dep
                for i in lc
                if dep <= i and i < arr
            ]
            for lc in list_chunk
        ]
        return list_chunk_resized

    def allocate_overlap(ans, chunk_size, overlap_size):
        return {
            i - (chunk_size - overlap_size) : ans[i]
            for i in range(chunk_size-overlap_size, chunk_size)
        }

    def limit_chunk(limitation, dep, arr, allocation={}):
        return {
            i - dep : allocation[i] if i in allocation.keys() else limitation[i]
            for i in range(dep, arr)
        }

    solution = []

    dep = 0
    arr = dep+chunk_size if dep+chunk_size <= num_variables else num_variables
    list_chunk_resized = resize_chunk(interference, dep, arr)
    limitation_chunk = limit_chunk(limitation, dep, arr)
    response = get_qubo.by_amplify_limited(list_chunk_resized, num_registers, limitation_chunk)
    ans = solve_qubo(response["qubits"], response["model"], token)
    solution.extend(ans)

    while arr < num_variables:
        print(solution)
        dep = arr - overlap_size
        arr = dep+chunk_size if  dep+chunk_size <= num_variables else num_variables
        list_chunk_resized = resize_chunk(interference, dep, arr)
        allocation = allocate_overlap(ans, chunk_size, overlap_size)
        limitation_chunk = limit_chunk(limitation, dep, arr, allocation)
        response = get_qubo.by_amplify_splitted(list_chunk_resized, num_registers, limitation_chunk)
        ans = solve_qubo(response["qubits"], response["model"], token)
        solution.extend(ans[overlap_size:])

    return solution
