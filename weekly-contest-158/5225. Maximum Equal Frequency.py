def change(dict1, n, dict2, count):
    if n in dict1:
        dict2[dict1[n]].remove(n)
        if not dict2[dict1[n]]:
            del dict2[dict1[n]]
            count -= 1
        dict1[n] += 1

    else:
        dict1[n] = 1

    if dict1[n] in dict2:
        dict2[dict1[n]].add(n)
    else:
        dict2[dict1[n]] = set([n])
        count += 1
    return count

def check(dict2):
    keys1=dict2.keys()
    c=0
    for k in dict2:
        if len(dict2[k])==1:
            if k==1:
                return True
            for k1 in dict2:
                if k1!=k:
                    if k1%2 and not k%2 and k>k1:
                        return True
                    if k%2 and not k1%2 and k>k1:
                        return True

                    if k1==1 and not k%2:
                        return True


    return False

def maxEqualFreq(nums):
    dict1 = {}
    dict2 = {}
    length = 0
    count = 0
    for i, v in enumerate(nums):
        count = change(dict1, v, dict2, count)
        # print(dict1,"ggg", dict2)
        if count==1:
            for k in dict2:
                if k==1 or len(dict2[k])==1:
                    length = i + 1
        print(i,dict2)

        if count == 2 and check(dict2):
            # print (i,dict2)
            length = i + 1
    return length

# nums=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,65,75,39,10,58,47,97,29,62,77,49,1,18,22,6,73,16,4,11,78,70,81,86,89,45,24,64,56,98,4,72,94,81,90,25,93,83,42,3,28,77,78,100,54,73,86,31,2,48,19,21,90,35,8,48,71,87,23,87,3,44,96,33,51,22,22,36,20,94,86,26,15,17,52,2,21,32,70,42,32,52,74,25,44,89,30,71,96,1,80]
# nums =[1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,42,21,45,27,78,39,78,24,47,60,22,33,45,18,56,91,93,66,79,65,43,7,57,63,74,25,11,14,100,95,19,3,22,18,94,52,91,33,95,16,93,63,65,8,88,51,47,7,51,77,36,48,89,72,81,75,13,69,9,31,16,38,34,76,7,82,10,90,64,28,22,99,40,88,27,94,85,43,75,95,86,82,46,9,74,67,51,93,97,35,2,49]
nums=[10,2,8,9,3,8,1,5,2,3,7,6]
nums=[1,2,3,1,2,3,4,4,4,4,1,2,3,5,6]
nums=[1,1]
nums=[2,2,1,1,5,3,3,5]
nums=[1,2]
print(maxEqualFreq(nums))