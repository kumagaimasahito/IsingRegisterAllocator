from . import load_out, load_allocatable_registers

def load_all_out_allocated(path):
    interference = load_out(path + "interference.out", True)
    res_alloc_reg = load_allocatable_registers(path + "allocatablereg.out")
    limitation = res_alloc_reg["limitation"]
    num_registers = len(res_alloc_reg["to_index"])

    return {
        "interference" : interference,
        "limitation" : limitation,
        "num_registers" : num_registers
    }