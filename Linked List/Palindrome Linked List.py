def reverse_ll(head):
    if not head or not head.next:
        return head
    p=reverse_ll(head.next)
    head.next.next=head
    head.next=None
    # print(p.val)
    return p
def isPalindrome(self, head):
    # head_r=reverse_ll(head)
    # head1=head
    if not head or not head.next:
        return True
    slow = head
    fast = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if fast.next:
        fast = fast.next
        slow = slow.next

    # print slow.val,fast.val

    head_r = reverse_ll(slow)
    # print head_r.next.val

    while head_r != head:
        if head.next == head_r:
            return head.val == head_r.val
        elif head.val != head_r.val:
            return False
        else:
            head = head.next
            head_r = head_r.next
    return True