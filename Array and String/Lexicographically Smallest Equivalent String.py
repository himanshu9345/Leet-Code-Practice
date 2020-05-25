# find union
A, B, S = "hello", "world", "hold"
arr = [i for i in range(26)]

def find_parent(arr, i):
    if arr[i]!=i:
        return find_parent(arr, arr[i])
    return i

def union(arr, i, j):
    p_i = find_parent(arr, i)
    p_j = find_parent(arr, j)
    if p_i<p_j:
        arr[p_j] = p_i
    elif p_j<p_i:
        arr[p_i] = p_j
    return

for i in range(len(A)):
    valA = ord(A[i]) - 95
    valB = ord(B[i]) - 95
    union(arr, valA, valB)

ans = ""
for i in S:
    ans += chr(95+find_parent(arr ,ord(i) - 95))

print(ans)
