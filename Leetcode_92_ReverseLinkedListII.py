from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr = head
        counter = 1
        copyList = []
        while ptr.next:
            if counter >= left and counter <= right:
                copyList.append(ptr)
            ptr = ptr.next
            counter += 1

        for i in range(1, len(copyList)):
            copyList[i - 1].next = copyList[i]

        counter = 1
        ptr = head

        while counter <= right + 1:
            if counter == left - 1:
                ptr.next = copyList[0]
            elif counter == right + 1:
                copyList[-1].next = ptr if ptr else None
            counter += 1
            ptr = ptr.next if ptr.next else None

        return head



