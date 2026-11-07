# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. get the pointer before the nth element i want to remove
        # 2. let it point to the n-1th pointer
        # use the fast & slow pointers, to let the slow pointer stops at where the n-1th node
        # eg. 1, 2, 3, 4
        # slow & fast both start from dummy
        # we want slow to stop at 2
        # when the fast moves to the end>> fast has to move n+1 than slow
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # move fast n+1 step ahead, then move them together

        for i in range(n+1):
            fast = fast.next

        while fast: # 讓fast走到none
            slow = slow.next
            fast = fast.next

        # when slow is pointing to the prev
        slow.next = slow.next.next

        return dummy.next # 不能回傳head因為可能刪掉head

