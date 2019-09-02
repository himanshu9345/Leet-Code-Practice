def removeNthFromEnd(self, head, n):
    total = 0
    head1 = head
    while (head1):
        head1 = head1.next
        total += 1
    to_reach = total - n
    # print(total,to_reach)
    if to_reach <= 0:
        return head.next
    head1 = head
    while (to_reach > 1):
        to_reach -= 1
        head1 = head1.next
    # print(head1.val)
    head1.next = head1.next.next
    return head