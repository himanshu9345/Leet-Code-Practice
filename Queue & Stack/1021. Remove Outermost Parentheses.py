class Solution(object):
    def removeOuterParentheses(self, S):
        stack = []
        open1 = 0
        res = ""
        for i in S:
            if open1 == 0:
                # print stac/
                if stack:
                    stack.pop()
                res += "".join(stack)
                stack = []
                open1 = 0

            if i == "(":
                open1 += 1
                if open1 > 1:
                    stack.append(i)
            else:
                open1 -= 1
                stack.append(i)

        if stack:
            stack.pop()
            res += "".join(stack)
        return res

        """
        :type S: str
        :rtype: str
        """
