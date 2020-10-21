def get_set():
    f = open("/usr/share/dict/words","rt")
    out_set = set([])
    
    for word in f.readlines():
        out_set.add(word)

    f.close()

    return out_set
