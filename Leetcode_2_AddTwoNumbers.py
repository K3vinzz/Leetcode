# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        isCarry = False
        result = ListNode()
        tail = result
        while l1 and l2:
            node = ListNode()
            node.val = l1.val + l2.val
            if isCarry:
                node.val += 1
                isCarry = False
            if node.val >= 10:
                node.val -= 10
                isCarry = True
            l1 = l1.next
            l2 = l2.next
            tail.next = node
            tail = tail.next

        while l1:
            node = ListNode()
            node.val = l1.val
            if isCarry:
                node.val += 1
                isCarry = False
            if node.val >= 10:
                node.val -= 10
                isCarry = True
            l1 = l1.next
            tail.next = node
            tail = tail.next

        while l2:
            node = ListNode()
            node.val = l2.val
            if isCarry:
                node.val += 1
                isCarry = False
            if node.val >= 10:
                node.val -= 10
                isCarry = True
            l2 = l2.next
            tail.next = node
            tail = tail.next

        if isCarry:
            node = ListNode(1)
            tail.next = node

        return result.next









