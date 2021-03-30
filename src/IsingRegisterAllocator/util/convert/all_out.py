from . import out

def all_out(path):
    interference = out(path + "interference.out", True)
    register_unit = out(path + "registerunit.out")
    unit_size = out(path + "unitsize.out")

    return {
        "interference" : interference,
        "register_unit" : register_unit,
        "unit_size" : unit_size
    }