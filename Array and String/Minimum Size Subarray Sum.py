import math
s = 7
nums = [2,3,1,2,4,3]
sum1=0
start=0
end=0
sum_helper=math.inf
while(end!=len(nums)):
    if sum1<s:
        sum1+=nums[end]
        end+=1
    if sum1>=s:
        sum_helper=min(sum_helper,end-start)
        sum1-=nums[start]
        start+=1
    # print(start,end)
print(min(sum_helper,end-start))

