def rotateRight(self, head, k):
    if not head:
        return None
    ll_len = 0
    head1 = head
    while head1:
        head1 = head1.next
        ll_len += 1
    new_k = k % ll_len
    fast = head
    slow = head
    for i in range(new_k):
        fast = fast.next
    while (fast.next):
        fast = fast.next
        slow = slow.next
    head1 = head
    fast.next = head

    temp = slow.next
    slow.next = None
    head = temp
    return head