def mergeTwoLists(self, l1, l2):
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1
    head1 = None
    head = None
    while l1 and l2:
        if head1:
            if l1.val > l2.val:
                head1.next = l2
                head1 = head1.next
                l2 = l2.next
            else:
                head1.next = l1
                head1 = head1.next
                l1 = l1.next
        else:
            if l1.val > l2.val:

                head1 = l2
                l2 = l2.next
            else:
                head1 = l1
                l1 = l1.next
            head = head1
            # print head1.val

    if l1:
        while l1:
            if head1:
                head1.next = l1
                head1 = head1.next
            else:
                head1 = l1
            l1 = l1.next
    if l2:
        while l2:
            if head1:
                head1.next = l2
                head1 = head1.next
            else:
                head1 = l2
            # print(head1.val)

            l2 = l2.next
    return head