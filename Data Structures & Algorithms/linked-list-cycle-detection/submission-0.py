# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use fast & slow pointers
        # if the fast pointer catch up w/ the slow pointer: cycle exists, return true
        # else: return false
        fast = head
        slow = head

        # 用何時停止思考while loop條件
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True


        return False 