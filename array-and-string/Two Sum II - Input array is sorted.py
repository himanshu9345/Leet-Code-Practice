numbers = [2,7,11,15]
target = 9
start=0
end=len(numbers)-1

while(numbers[start]+numbers[end]!=target):
    if numbers[start]+numbers[end]>target:
        end-=1
    if numbers[start]+numbers[end]<target:
        start+=1
    print(start,end)

print( [start,end])