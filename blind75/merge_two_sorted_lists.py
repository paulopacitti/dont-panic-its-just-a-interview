
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    new_list = ListNode()
    head = new_list
    while list1 and list2:
        if list1.val < list2.val:
            new_list.next = ListNode(list1.val)
            new_list = new_list.next

            list1 = list1.next
        elif list1.val > list2.val:
            new_list.next = ListNode(list2.val)
            new_list = new_list.next

            list2 = list2.next
        else:
            new_list.next = ListNode(list1.val)
            new_list = new_list.next
            new_list.next = ListNode(list2.val)
            new_list = new_list.next

            list1 = list1.next
            list2 = list2.next

    if list1:
        new_list.next = list1
    elif list2:
        new_list.next = list2

    return head.next

def merge_two_lists_recursive(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    smaller, larger = (list1, list2) if list1.val < list2.val else (list2, list1)
    smaller.next = merge_two_lists_recursive(smaller.next, larger)
    return smaller