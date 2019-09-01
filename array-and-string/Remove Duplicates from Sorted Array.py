nums=[0,0,1,1,1,2,2,3,3,4]
# i=0
j=0
# if nums[0]==nums[1]:
#     j=1
# for i in range(1,len(nums)):
#     if nums[i]!=nums[j]:
#         nums[i],nums[j]=nums[j],nums[i]
#         j+=1
# #     # if nums[i]==nums[j]:
k=1
# while(k!=len(nums)-1):
#     while(nums[k]==nums[k+1]):
#         k+=1
#         print(k)
#     if nums[k]!=nums[k-1]:
#         nums[k],nums[j]=nums[j],nums[k]
#         j+=1
#     k+=1
from collections import OrderedDict
for i in range(1,len(nums)):
    if nums[i]!=nums[j]:
        j+=1
        nums[j]=nums[i]





print(nums,j)

# for i in range(len(nums)-1):
#     if nums[i]!=nums[i+1]:
