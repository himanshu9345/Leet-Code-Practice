class Solution(object):
    def avoidFlood(self, rains):
        
        # to store dry days
        drydays = []
        # to store answer
        ans = []
        # dict1 in store rain day index
        dict1 = defaultdict(int)
        #iterate over rain array
        for i, val  in enumerate(rains):
            '''
            if rains[i] is 0 then ans[i] can be any thing
            [1,0,2,3,0,1,2]
[1,0,2,0,2,1]
[0,1,1]
[1,0,2,0,2,1]
            '''
            if val == 0:
                ans.append(1)
                drydays.append(i)
            else:
                if val in dict1:
                    index = bisect_left(drydays, dict1[val])
                    # print index, drydays,i,val,dict1[val]
                    # check if not found 
                    if index == len(drydays):
                        return []
                    # reterive the rain 0(dry day index)
                    dindex = drydays[index]
                    # remove dry day index since it used to dry curr lake
                    drydays.pop(index)
                    # can val from 1 to current lake
                    
                    ans[dindex] = val
                    dict1[val] = i
                    ans.append(-1)
                else:
                    ans.append(-1)
                    dict1[val] = i
        return  ans
        
        
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        