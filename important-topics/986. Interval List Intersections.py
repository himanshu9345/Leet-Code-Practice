A = [[0,1],[5,10],[12,23],[27,29]]
B = [[1,5],[8,12],[15,24],[25,26]]
def intervalIntersection( A, B):#memory limit exceeded
    seen=set()
    dict1={}
    for v,i in enumerate(A):
        for j in [i for i in range(i[0],i[1]+1)]:
            dict1[j]=v
    ans=[]
    dict2 = {}
    for v,i in enumerate(B):
        ans+=[i for i in range(i[0],i[1]+1)]
        for j in [i for i in range(i[0],i[1]+1)]:
            dict2[j]=v
    result=[]
    for i in ans:
        if i in dict1:
            result.append((i,dict1[i],dict2[i]))
    ans=[]
    if result:
        start=result[0][0]
    for i,v in enumerate(result):
        j,one,sec=v
        if i<len(result)-1:
            if j!=result[i+1][0]-1:
                ans.append([start,j])
                start=result[i+1][0]
            else:
                if one!=result[i+1][1] or sec!=result[i+1][2]:
                    ans.append([start, j])
                    start=result[i+1][0]
        else:
            ans.append([start,j])

    print(ans)

def intervalIntersection2(A,B):
    ans=[]
    i=0
    j=0
    while i<len(A) and j<len(B):
        low=max(A[i][0],B[j][0])
        high=min(A[i][1],B[j][1])
        if low<=high:
            ans.append([low,high])
        if A[i][1]<B[j][1]:
            i+=1
        else:
            j+=1
    return ans


print (A,B)
# intervalIntersection(A,B)
print(intervalIntersection2(A,B))