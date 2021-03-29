def convert_interference(path)
    f = open(path)
    data = f.read()
    list_data = eval(data)
    f.close()
    return [
        [
            i
            for i, x in enumerate(g)
            if x==1
        ]
        for g in list_data
    ]