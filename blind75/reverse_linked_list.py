# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head:
        return None

    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    
    new_list = ListNode(stack.pop())
    new_head = new_list
    while stack:
        new_head.next = ListNode(stack.pop())
        new_head = new_head.next
    
    return new_list

def reverseListPointers(head):
    previous = None
    current = head
    while current:
        forward = current.next
        current.next = previous
        previous = current
        current = forward

    return previous
    

def reverseListRecursive(head):
    # base case where list is empty or has only one element
    if head is None or head.next is None:
        return head
    
    new_head = reverseListRecursive(head.next)
    # reverse pointers
    front = head.next
    front.next = head
    head.next = None # this is important to avoid cycles

    return new_head