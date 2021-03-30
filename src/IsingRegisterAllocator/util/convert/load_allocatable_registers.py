from collections import Counter

def load_allocatable_registers(path):
    f = open(path)
    data = f.read()
    f.close()

    data = data.replace("[$", "['$").replace(",$", "','$").replace(",]", "',]")
    data = data.replace("[M$", "['$").replace(",M$", "','$")
    dict_data = eval(data)
    # print(dict_data)

    registers = []
    for list_reg in dict_data.values():
        registers.extend(list_reg)

    to_index = {k: i for i, k in enumerate(Counter(registers).keys())}
    to_string = {i: k for i, k in enumerate(Counter(registers).keys())}

    dict_data_converted = {
        i : [
            to_index[reg]
            for reg in regs
        ]
        for i, regs in dict_data.items()
    }
    print(dict_data_converted)

    return {
        "allocatable_registers" : dict_data_converted,
        "to_index" : to_index,
        "to_string" : to_string
    }
