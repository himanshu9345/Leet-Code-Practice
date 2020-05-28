from collections import defaultdict

def possibleBipartition( N, dislikes):
    dict1 = defaultdict(list)
    for i,j in dislikes:
        dict1[i].append(j)
        dict1[j].append(i)
    
    visited = {}
    
    def dfs(node, group):
        if node in visited:
            return visited[node] == group
        visited[node] = group
        isTrue = False
        for i in dict1[node]:
            isTrue = dfs(i, 1 - group%2)
            if not isTrue:
                return  False
        return True
    for i in range(1, N+1):
        if i not in visited:
            val = dfs(i, 0)
            if not val:
                return False
    return True
    """
    :type N: int
    :type dislikes: List[List[int]]
    :rtype: bool
    """

def find_parent(arr, i):
    if arr[i]!=i:
        return find_parent(arr, arr[i])
    return i

def union(arr, i, j):
    p_j = find_parent(arr, j)
    arr[p_j] = i
    return p_j
    # if p_i<p_j:
    #     arr[p_j] = p_i
    # elif p_j<p_i:
    #     arr[p_i] = p_j
    # return

def possibleBipartition1( N, dislikes):
    dict1 = defaultdict(list)
    for i,j in dislikes:
        dict1[i].append(j)
        dict1[j].append(i)
    
    arr = [i for i in range(N+1)]
    for i in range(1, N+1):
        i_parrent = find_parent(arr, i)
        if len(dict1[i]) > 0:
            this_grp_parent = find_parent(arr, dict1[i][0])
            if i_parrent == this_grp_parent: return False
            for j in dict1[i]:
                if arr[j] != j:
                    continue
                else:
                    if union(arr, this_grp_parent, j) == i_parrent:
                        return False
    return True

N = 3
dislikes =  [[1,2],[1,3],[2,3]]
print(possibleBipartition1(N, dislikes))
print(possibleBipartition(N, dislikes))
