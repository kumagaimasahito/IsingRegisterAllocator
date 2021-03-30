from IsingRegisterAllocator import split_graph_coloring
from dotenv import load_dotenv
import os

load_dotenv()
AMPLIFY_TOKEN = os.environ.get("AMPLIFY_TOKEN")

def test_split_graph_coloring():
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

    solution = split_graph_coloring(list_dependent_variables, num_registers, chunk_size, overlap_size, AMPLIFY_TOKEN)
