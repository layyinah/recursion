def unflatterned(dic):
    new={}
    for key,value in dic.items():
        if '.' in key:
            k1,k2=key.split('.')
            value={k2:value}
            key=k1
        new[key]=value
    return new
print(unflatterned({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))