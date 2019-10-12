def removeElements(self, head, val):
    head1 = head
    prev = None
    count = 0
    while head1 and head1.next:
        if head1.val == val:
            if not prev:
                head = head.next
                head1 = head1.next
            else:
                # print(head1.val,count,prev.val)
                prev.next = head1.next
                head1 = head1.next
        else:
            prev = head1
            head1 = head1.next
        count += 1
    if head1:
        if head1.val == val:
            if prev:
                prev.next = None
            else:
                return None

    return head