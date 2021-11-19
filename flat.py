def flattened(d,key="",seperator="."):
    flatdict=[]
    for k,v in d.items():
        new=key+seperator+k if key else k
        if isinstance(v,dict):
            flatdict.extend(flattened(v,new,seperator=seperator).items())
        else:
            flatdict.append(v)
    return(flatdict)
print(flattened({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))