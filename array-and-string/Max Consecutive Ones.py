nums=[1,1,0,1,1,1]
one_count=0
one_count_till_now=0
for i in nums:
    if i!=1:
        one_count=max(one_count,one_count_till_now)
        one_count_till_now=0
    else:
        one_count_till_now+=1
print(max(one_count_till_now,one_count))