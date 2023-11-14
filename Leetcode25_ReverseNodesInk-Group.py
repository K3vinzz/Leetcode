# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if k == 1:
        return head
    length = 0
    dummy = ListNode(next=head)
    c = dummy
    while c.next:
        length += 1
        c = c.next
    group = length // k
    l = dummy
    p, e = head, head
    c = head.next
    for i in range(group):
        for a in range(k - 1):
            t = c.next
            c.next = p
            p = c
            c = t
        l.next = p
        l = e
        p, e = c, c
        c = t.next if t else None
    l.next = p if p else None
    return dummy.next










