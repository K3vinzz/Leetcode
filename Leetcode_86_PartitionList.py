from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or x >= 100 or x <= -100:
            return head
        dummy = ListNode(next=head)
        cur = dummy
        isFindLess, isFindGreat = False, False
        while cur.next:
            cur = cur.next
            if cur.val < x:
                if not isFindLess:
                    less = cur
                    lp = cur
                    isFindLess = True
                else:
                    lp.next = cur
            elif cur.val >= x:
                if not isFindGreat:
                    great = cur
                    gp = cur
                    isFindGreat = True
                else:
                    gp.next = cur
        dummy.next = less
        lp.next = great
        gp.next = None
        return dummy.next

s = Solution()
l = ListNode(1,None)
l2 = ListNode(5,l)
print(s.partition(x=3, head=l2))