def split_unit(interference, register_unit):
    num_unit = max(register_unit) + 1
    interference_unit = [{} for i in range(num_unit)]
    for i, x in enumerate(register_unit):
        interference_unit[x][i] = interference[i]
    
    interference_unit_converted = [{} for i in range(num_unit)]
    for x, unit in enumerate(interference_unit):
        unit_key = unit.keys()
        for i, values in unit.items():
            interference_unit_converted[x][i] = [v for v in values if v in unit_key]

    return interference_unit_converted