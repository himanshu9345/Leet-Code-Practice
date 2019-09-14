class Solution(object):
    def isValid(self, s):
        if s == "":
            return True
        list1 = list(s)
        new_list = [list1.pop()]

        while list1:
            l1 = list1[-1]
            l2 = new_list[-1]
            # print l1,l2
            if (l2 == ")" and l1 == "(") or (l2 == "]" and l1 == "[") or (l2 == "}" and l1 == "{"):
                list1.pop()
                new_list.pop()
                if list1 and not new_list:
                    new_list.append(list1.pop())
            else:
                new_list.append(list1.pop())
        return len(new_list) == 0

        """
        :type s: str
        :rtype: bool
        """


