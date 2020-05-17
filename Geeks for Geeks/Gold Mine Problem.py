gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]] 
  
m = 4
n = 4

def getMaxGold(gold, m, n):
    r, c = [0, -1, 1],[-1, -1, -1]
    maxGold = 0
    for j in range(1, n):
        for i in range(m):
            if gold[i][j] != 0:
                max1 = 0
                for k in range(3):
                    x, y = i + r[k], j + c[k]
                    if 0 <= x < m and 0 <= y < n:
                        max1 = max(max1, gold[x][y])
                if max1 != 0:
                    gold[i][j] += max1
                
            if j == n-1:
                maxGold = max(maxGold, gold[i][j])
    return maxGold
            
tests = int(input())
result = []
for i in range(tests):
    get_mn = input().split(" ")
    m, n = int(get_mn[0]), int(get_mn[1])
    gold = []
    goldArray = input().split(" ")
    count = 0
    max_new = 0
    for i in range(m):
        new = []
        for j in range(n):
            new.append(int(goldArray[count]))
            count += 1
        max_new = max(max_new, new[-1])
        gold.append(new)
    # print (gold, max_new)
    if n <= 1:
        print (max_new)
    else:
        print(getMaxGold(gold, m, n))