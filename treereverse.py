ls=[[1, 2], [3, [4, 5]], 6]
def treereverse(lst,result=None):
    if result is None:
        result=[]
    for i in lst:
        if isinstance(i,list):

             # lst[0]=result.append(treereverse(i))
            result.insert(0,treereverse(i))


        else:
             # result.append(i)
             result.insert(0,i)
    return result
print(treereverse(ls))