# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while (cur is not None and cur.next is not None):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        if prev is not None:
            cur.next = prev
        
        return cur
