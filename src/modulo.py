def func(pedras="", joia=""):
    n = 0
    for x in range(0,len(pedras)):
        n+=joia.count(pedras[x],0,len(joia))
    return n
