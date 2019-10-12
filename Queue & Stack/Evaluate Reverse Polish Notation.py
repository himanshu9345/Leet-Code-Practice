class Solution(object):
    def evalRPN(self, tokens):
        op = set(["*", "+", "-", "/"])
        stack = []
        for i in tokens:
            if i in op:
                o2 = int(stack.pop())
                o1 = int(stack.pop())
                if i == "*":
                    stack.append(int(o1 * o2))
                if i == "/":
                    stack.append(int(o1 / o2))
                    if stack[-1] < 0:
                        stack[-1] += 1

                if i == "+":
                    stack.append(int(o1 + o2))
                if i == "-":
                    stack.append(int(o1 - o2))
            else:
                stack.append(int(i))
        return stack[0]
        """
        :type tokens: List[str]
        :rtype: int
        """
