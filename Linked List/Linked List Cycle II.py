#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = [3]
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

def detectCycle( head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    if not fast or not fast.next:
        return None

    fast=head
    # print (slow.val)
    if slow:
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
            # print(slow.val,fast.val)
        return slow
    return None



print(detectCycle(head_node).val)