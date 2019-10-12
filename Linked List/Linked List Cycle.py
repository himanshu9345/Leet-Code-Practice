class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = [3,4]
cycle_element=3

def build_list(head):
    head_node = ListNode(head[0])
    head1 = head_node
    for i in head[1:len(head)]:
        head1.next = ListNode(i)
        head1 = head1.next
    return head_node
head_node=build_list(head)


def create_cycle(head_node,cycle_element):
    head_node_copy=head_node
    while(head_node_copy.next is not None):
        head_node_copy=head_node_copy.next

    while(head_node and head_node.val!=cycle_element):
        head_node=head_node.next
    if head_node:
        head_node_copy.next=head_node
    return

def printlist(head_node):
    while(head_node is not None):
        print(head_node.val)
        head_node=head_node.next
    return

create_cycle(head_node,cycle_element)
#printlist(head_node)

#######################Solution################################
def hasCycle( head):
    if not head:
        return False
    if head.next==None:
        return False

    slow=head
    fast=head.next.next
    # if fast==None:
    #     return False
    while(fast and slow and fast.val!=slow.val):

        if slow==None or fast==None or fast.next==None:
            return False
        slow = slow.next
        fast = fast.next.next
    if fast and slow:
        return True
    return False



print (hasCycle(head_node))