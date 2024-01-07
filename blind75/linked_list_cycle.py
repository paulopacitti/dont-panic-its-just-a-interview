# https://leetcode.com/problems/linked-list-cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycleFloyds(head):
    # Floyd's turtoise and hare approach, O(1) memory
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def hasCycleSet(head):
    stack = set()
    current = head
    while current != None:
        if current in stack:
            return True
        else:
            stack.add(current)
            current = current.next
    return False