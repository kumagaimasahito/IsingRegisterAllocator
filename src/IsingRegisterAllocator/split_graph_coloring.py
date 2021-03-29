from util import get_qubo
from util.solve_qubo import by_amplify as solve_qubo

def split_graph_coloring(list_dependent_variables, num_registers, chunk_size, overlap_size):
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
    ans = solve_qubo(response["qubits"], response["model"])
    solution.extend(ans)
    # print(solution)

    while arr < num_variables:
        dep = arr - overlap_size
        arr = dep+chunk_size if  dep+chunk_size <= num_variables else num_variables
        list_chunk_resized = resize_chunk(list_dependent_variables, dep, arr)
        allocation = allocate_overlap(ans, chunk_size, overlap_size)
        response = get_qubo.by_amplify_splitted(list_chunk_resized, num_registers, allocation)
        ans = solve_qubo(response["qubits"], response["model"])
        solution.extend(ans[overlap_size:])
        # print(solution)

    return solution

def main():
    list_dependent_variables = [
        [1, 2, 3],
        [0, 2, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 4],
        [1, 2, 3],
        [6],
        [5],
        []
    ]
    num_registers = 4
    chunk_size = 3
    overlap_size = 1

    solution = split_graph_coloring(list_dependent_variables, num_registers, chunk_size, overlap_size)
    print(solution)

if __name__ == "__main__":
    main()