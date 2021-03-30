from IsingRegisterAllocator import get_solution_limited_unit
from dotenv import load_dotenv
import os

load_dotenv()
AMPLIFY_TOKEN = os.environ.get("AMPLIFY_TOKEN")

def test_get_solution_limited_unit():
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
    num_registers = 37
    limitation = {0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 1: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 2: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 3: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 4: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 5: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 6: [31, 32, 33, 34, 35, 36], 7: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 8: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 9: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 10: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 11: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 12: [2, 3, 4, 5, 9, 10], 13: [31, 32, 33, 34, 35, 36], 14: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 15: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 16: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 17: [2, 3, 4, 5, 9, 10], 18: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 19: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}

    solution = get_solution_limited_unit(interference, num_registers, limitation, AMPLIFY_TOKEN)
#     print(solution)

# if __name__ == "__main__":
#     test_get_solution_limited_unit()