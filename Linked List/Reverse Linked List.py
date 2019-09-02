def reverseList(self, head):
    head1 = head

    while (head1 and head1.next):
        next1 = head1.next
        head1.next = head1.next.next
        next1.next = head
        head = next1
    return head