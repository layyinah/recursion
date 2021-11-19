ls=[1, 2, [3, 4, [5]]]
def treemap(ls):
    for ele, i in enumerate(ls):
        if isinstance(i,list):
            treemap(i)
        else:
             ls[ele]=ls[ele]**2
    return ls
print(treemap(ls))