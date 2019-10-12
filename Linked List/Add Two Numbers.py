class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1, l2):
    if not l1 and not l2:
        return l1
    if not l1:
        return l2
    if not l2:
        return l1

    carry = 0
    sum_node = None
    sum_node_ans = None
    while (l1 and l2):
        if sum_node:
            l1.val += l2.val + carry
            print(l1.val)

            carry = l1.val / 10
            l1.val = l1.val % 10

            sum_node.next = l1
            l1 = l1.next
            l2 = l2.next
            sum_node = sum_node.next
        else:
            l1.val += l2.val + carry
            carry = l1.val / 10
            l1.val = l1.val % 10
            sum_node = l1
            l1 = l1.next
            l2 = l2.next
            sum_node_ans = sum_node
    if l1:
        if carry:
            while l1:
                l1.val += carry
                carry = l1.val / 10
                l1.val = l1.val % 10
                if sum_node:
                    sum_node.next = l1
                    sum_node = sum_node.next

                l1 = l1.next
        else:
            sum_node.next = l1

    if l2:
        if carry:
            while l2:
                l2.val += carry
                carry = l2.val / 10
                l2.val = l2.val % 10
                if sum_node:
                    sum_node.next = l2
                    sum_node = sum_node.next
                l2 = l2.next
        else:
            sum_node.next = l2

    if carry:
        sum_node.next = ListNode(carry)
    return sum_node_ans