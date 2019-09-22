class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def nthUglyNumber(self, n, a, b, c):
        # list1=[]
        # min1=min(a,min(b,c))
        # seen=set()
        # for i in range(1,(n*min1/a)+1):
        #     list1.append(i*a)
        #     print i
        #     seen.add(i*a)
        # for i in range(1,((n*min1)/b)+1):
        #     if i*b not in seen:
        #         list1.append(i*b)
        #         seen.add(i*b)
        # for i in range(1,((n*min1)/c)+1):
        #     if i*c not in seen:
        #         list1.append(i*c)
        # list1=sorted(list1)
        # # print list1/
        # return list1[n-1]
        # import heapq
        # l1=[(a,a),(b,b),(c,c)]
        def lcm(x, y):
            return (x * y) / self.gcd(x, y)

        lcm1 = lcm(a, b)
        lcm2 = lcm(b, c)
        lcm3 = lcm(c, a)
        lcm4 = lcm(lcm1, lcm2)

        # print lcm1,lcm2,lcm3,lcm4

        def get_count(x):
            return (x / a) + (x / b) + (x / c) + (x / lcm4) - ((x / lcm1) + (x / lcm2) + (x / lcm3))

        i = 0
        j = 2 * 10 ** 9
        while j - i > 1:
            mid = (i + j) / 2
            count = get_count(mid)
            # print count
            if count >= n:
                j = mid
            else:
                i = mid
        return j

        # print sum1
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
