import math
test = int(input())
for i in range(test):
    n = input()
    val = input()
    val = val.split()
    sum1 = 0
    for v in range(len(val[1:])):
        sum1 += abs(int(val[v]) - int(val[v+1])) - 1
    print(sum1)

