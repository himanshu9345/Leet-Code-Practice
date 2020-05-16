nums=[1,4,3,2]
nums=sorted(nums)
sum1=0
for i in range(0,int(len(nums)), 2):
    sum1+=nums[i]
print(sum1)