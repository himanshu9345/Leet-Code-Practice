class Solution(object):
    def hammingDistance(self, x, y):
        #creating 32 bit string or x xor y
        binaryx = "{:032b}".format(x^y)
        #counting 1 from xor value
        count=0
        for i in binaryx:
            if i=="1":
                count+=1
        return count

        
        """
        :type x: int
        :type y: int
        :rtype: int
        """

# more optimal
class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        while xor:
            count+=1
            xor = xor & (xor-1)
        return count
        