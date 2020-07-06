import math
test = int(input())
def getSum(str1):
    sum1 = 0
    for i in str1:
        sum1 += int(i)
    return sum1
for i in range(test):
    n = input()
    csum = 0
    msum = 0
    for i in range(int(n)):
        val = input()
        val = val.split()
        c = getSum(val[0])
        m = getSum(val[1])
        if c > m:
            csum += 1
        elif c < m:
            msum += 1
        else:
            csum += 1
            msum += 1
    if csum > msum:
        print(str(0)+" "+str(csum))
    elif csum < msum:
        print(str(1) + " "+ str(msum))
    else:
        print(str(2) + " "+ str(msum))
    