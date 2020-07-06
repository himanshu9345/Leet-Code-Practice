import math
test = int(input())
for i in range(test):
    n = int(input())
    setx = set()
    sety = set()
    for i in range(4*n-1):
        val = input()
        val = val.split()
        x, y = int(val[0]),int(val[1])
        if x in setx:
            setx.remove(x)
        else:
            setx.add(x)
        
        if y in sety:
            sety.remove(y)
        else:
            sety.add(y)
    print(str(list(setx)[0])+" "+str(list(sety)[0]))
