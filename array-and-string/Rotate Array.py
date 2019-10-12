nums=[1,2,3,4,5,6,7]
k = 3
# nums=[-1,-100,3,99]
# k = 3
gg=nums[:]
print(nums[(len(nums)-k)%len(nums):len(nums)],nums[0:(len(nums)-k)%len(nums)])
gg[0:k]=nums[(len(nums)-k)%len(nums):len(nums)]
gg[k:len(nums)]=nums[0:(len(nums)-k)%len(nums)]
for i,val in enumerate(gg):# print(gg)
    nums[i]=val
print(nums)

#sol2
# def reverse():
