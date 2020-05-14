class Solution(object):
    def removeKdigits(self, num, k):
        if k==len(num):
            return "0"
        stack=[]
        for i  in num:
            # i=int(i)
            if stack:
                if stack[-1]<i:
                    stack.append(i)
                else:
                    # removing all digits great then current digit(i)
                    while stack and k and stack[-1]>i:
                        stack.pop()
                        k-=1
                    stack.append(i)
            else:
                # if stack is empty
                stack.append(i)
        
        # if big number are at end
        while stack and k>0:
            stack.pop()
            k-=1
        
        # checking leading zeros
        zero_start=0
        for i in stack:
            if i=='0':
                zero_start+=1
            else:
                break
        if len(stack)==zero_start:
            return "0"
        else:
            return "".join(stack[zero_start:])

        