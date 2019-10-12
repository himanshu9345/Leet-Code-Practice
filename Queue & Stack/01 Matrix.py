mat=[[0,0,0],
 [0,1,0],
 [1,1,1]]
def bfs(matrix,m,n,i,j):
    seen=set()
    seen.add((i,j))
    queue=[(i,j)]
    r,c=[-1,0,1,0],[0,1,0,-1]
    level=1
    while queue:
        new_q=[]
        for k in queue:
            x,y=k
            for c1 in range(4):
                m1,n1=x+r[c1],y+c[c1]
                if 0<=m1<m and 0<=n1<n and (m1,n1) not in seen:
                    # print(m1,n1)
                    if matrix[m1][n1]==0:
                        return level
                    new_q.append((m1,n1))
                    seen.add((m1,n1))
        queue=new_q
        level+=1
    return

def updateMatrix( matrix):
    seen=set()
    new_mat=[]
    # print(new_mat)
    for i in range(len(matrix)):
        list1=[]
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:

                list1.append(bfs(matrix,len(matrix),len(matrix[0]),i,j))
            else:
                list1.append(matrix[i][j])
        new_mat.append(list1)
    return new_mat

print(updateMatrix(mat))