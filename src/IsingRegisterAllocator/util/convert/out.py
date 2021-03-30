def out(path, convert=False):
    f = open(path)
    data = f.read()
    list_data = eval(data)
    f.close()
    if convert:
        return [
            [
                i
                for i, x in enumerate(g)
                if x==1
            ]
            for g in list_data
        ]
    else :
        return list_data
