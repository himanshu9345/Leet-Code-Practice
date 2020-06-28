import math
test = int(input())
for i in range(test):
    val = input()
    val = val.split()
    x = int(val[0])
    y = int(val[1])
    n = int(val[2])
    # if n%x==y:
    #     print(n)
    #     continue
    div = math.ceil((n/x))
    k = x*(div) + y
    while k>n:
        k -= x
    print(k)