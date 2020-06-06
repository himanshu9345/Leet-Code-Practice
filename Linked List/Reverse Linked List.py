def reverseList(self, head):
    head1 = head

    while (head1 and head1.next):
        next1 = head1.next
        head1.next = head1.next.next
        next1.next = head
        head = next1
    return head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
#         head1=head
        
#         while(head1 and head1.next):
#             next1=head1.next
#             head1.next=head1.next.next
#             next1.next=head
#             head=next1
#         return head
        def helper(head):
            if not head or not head.next:
                return head
            p = helper(head.next)
            head.next.next = head
            head.next  = None
            return p
                        
    
        return helper(head) 
        """
        :type head: ListNode
        :rtype: ListNode
        """
        