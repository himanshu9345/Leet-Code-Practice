def getIntersectionNode(self, headA, headB):
    head1=headA
    head2=headB
    if not head1 or not head2:
        return None
    if head1==head2:
        return head1
    while head1 and head2:
        head1=head1.next
        head2=head2.next
        if head1==head2:
            return head1
    if head1==None:
        head1=headB
    if head2==None:
        head2=headA
    while head1 and head2:
        head1=head1.next
        head2=head2.next
        if head1==head2:
            return head1

    if head1==None:
        head1=headB
    if head2==None:
        head2=headA
    while head1 and head2:
        if head1==head2:
            return head1
        head1=head1.next
        head2=head2.next
    return None