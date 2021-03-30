from .util import get_qubo
from .util.solve_qubo import by_amplify as solve_qubo

def get_solution_splitted_algorithm(list_dependent_variables, num_registers, chunk_size, overlap_size, token):
    num_variables = len(list_dependent_variables)

    def resize_chunk(list_dependent_variables, dep, arr):
        list_chunk = list_dependent_variables[dep:arr]
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

    solution = []

    dep = 0
    arr = dep+chunk_size if dep+chunk_size <= num_variables else num_variables
    list_chunk_resized = resize_chunk(list_dependent_variables, dep, arr)
    response = get_qubo.by_amplify(list_chunk_resized, num_registers)
    ans = solve_qubo(response["qubits"], response["model"], token)
    solution.extend(ans)

    while arr < num_variables:
        dep = arr - overlap_size
        arr = dep+chunk_size if  dep+chunk_size <= num_variables else num_variables
        list_chunk_resized = resize_chunk(list_dependent_variables, dep, arr)
        allocation = allocate_overlap(ans, chunk_size, overlap_size)
        response = get_qubo.by_amplify_splitted(list_chunk_resized, num_registers, allocation)
        ans = solve_qubo(response["qubits"], response["model"], token)
        solution.extend(ans[overlap_size:])

    return solution
