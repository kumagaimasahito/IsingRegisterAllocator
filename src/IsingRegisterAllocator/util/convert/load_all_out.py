from . import load_out

def load_all_out(path):
    interference = load_out(path + "interference.out", True)
    register_unit = load_out(path + "registerunit.out")
    unit_size = load_out(path + "unitsize.out")

    return {
        "interference" : interference,
        "register_unit" : register_unit,
        "unit_size" : unit_size
    }