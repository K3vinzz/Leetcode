from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode()
        merge = a

        while list1 and list2:
            if list1.val < list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
            merge = merge.next
            if list1:
                merge.next = list1
            elif list2:
                merge.next = list2
        return a.next













