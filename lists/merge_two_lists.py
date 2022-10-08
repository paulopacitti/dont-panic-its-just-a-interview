# description: https://leetcode.com/problems/merge-two-sorted-lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(l, v):
    l.next = ListNode(v)
    l = l.next
    return l


def mergeTwoLists(list1, list2):
    output = ListNode()
    node_output = output
    node_1 = list1
    node_2 = list2
    while node_1 and node_2:
        if node_1.val < node_2.val:
            node_output = insert(node_output, node_1.val)
            node_1 = node_1.next
        elif node_2.val < node_1.val:
            node_output = insert(node_output, node_2.val)
            node_2 = node_2.next
        else:
            node_output = insert(node_output, node_1.val)
            node_output = insert(node_output, node_2.val)
            node_1 = node_1.next
            node_2 = node_2.next
    while node_1:
        node_output = insert(node_output, node_1.val)
        node_1 = node_1.next
    while node_2:
        node_output = insert(node_output, node_2.val)
        node_2 = node_2.next
    return output.next


array1 = [1, 2, 4]
array2 = [1, 3, 4]
list1 = ListNode()
node_1 = list1
list2 = ListNode()
node_2 = list2
for e in array1:
    node_1.val = e
    node_1.next = ListNode()
    node_1 = node_1.next
for e in array2:
    node_2.val = e
    node_2.next = ListNode()
    node_2 = node_2.next
output = mergeTwoLists(list1, list2)
while output:
    print(output.val)
    output = output.next
