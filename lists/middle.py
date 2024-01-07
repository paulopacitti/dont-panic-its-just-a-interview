# description: https://leetcode.com/problems/middle-of-the-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNodeFloyd(head):
    fast = head
    slow = head

    while fast and fast.next and slow:
        slow = slow.next
        fast = fast.next.next
    return slow

def middleNode(head):
    array = []
    while head:
        array.append(head)
        head = head.next
    return array[len(array)//2]