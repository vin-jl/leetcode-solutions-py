# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]

        def merge2Lists(list1: ListNode, list2: ListNode) -> ListNode:
            if not list1: return list2
            if not list2: return list1

            if list1.val < list2.val:
                list1.next = merge2Lists(list1.next, list2)
                return list1
            else:
                list2.next = merge2Lists(list1, list2.next)
                return list2

        mid = floor(len(lists)/2)
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge2Lists(left, right)
