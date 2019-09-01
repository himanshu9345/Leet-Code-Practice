nums=[0,1,0,0,3,12,0,6]
nums=[0,0,5]

j=0
for i in range(len(nums)):
    while(j<len(nums) and nums[j]!=0):
        j+=1
    if nums[i]!=0 and j<len(nums) and i>j:
        print(i,j)
        nums[i],nums[j]=nums[j],nums[i]
# last = 0

# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[i], nums[last] = nums[last], nums[i]
#         last += 1
print(nums)

