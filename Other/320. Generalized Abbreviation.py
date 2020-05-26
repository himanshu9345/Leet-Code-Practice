s = "word"
result = []
def backtrack(str1, i):
    if i >= len(str1):
        return 
    
    for j in range(i, len(str1)):
        for k in range(1, len(str1)+1):
            if k+j<(len(str1)+1):
                new_str  = str1[:j]+str(k)+str1[k+j:]
                result.append(new_str)
                print(new_str)
                backtrack(new_str, j+len(str(k))+1)

result.append(s)
backtrack(s,0)
print(result)
# ["1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# ['1ord', '1o1d', '1o2', '1or1', '2rd', '2r1', '3d', '4', 'w1rd', 'w1r1', 'w2d', 'w3', 'wo1d', 'wo2', 'wor1']
