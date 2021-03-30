from . import load_out, load_allocatable_registers

def load_all_out_allocated():
    interference = load_out(path + "interference.out", True)
    res_alloc_reg = load_allocatable_registers(path + "allocatablereg.out")
    allocatable_registers = res_alloc_reg["allocatable_registers"]
    num_registers = len(res_alloc_reg["to_index"])

    return {
        "interference" : interference,
        "allocatable_registers" : allocatable_registers,
        "num_registers" : num_registers
    }