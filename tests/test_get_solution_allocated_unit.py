from IsingRegisterAllocator import get_solution_allocated_unit
from dotenv import load_dotenv
import os

load_dotenv()
AMPLIFY_TOKEN = os.environ.get("AMPLIFY_TOKEN")

def test_get_solution_allocated_unit():
    interference = [
        [
            i
            for i, x in enumerate(g)
            if x==1
        ]
        for g in [
            [0,1,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,1,],
            [1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,],
            [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,],
            [1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,],
            [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,],
            [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,],
            [0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
            [1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,],
        ]
    ]
    register_unit = [0,1,1,1,1,1,2,1,1,1,1,1,3,2,1,1,1,4,1,1,]
    unit_size = [15,16,15,15,15,]

    solution = get_solution_allocated_unit(interference, register_unit, unit_size, AMPLIFY_TOKEN)
#     print(solution)

# if __name__ == "__main__":
#     test_get_solution_allocated_unit()