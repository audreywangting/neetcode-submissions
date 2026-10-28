# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use prev, curr, temp to keep the nodes
        # use curr to keep iterate

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev # curr 指向prev
            prev = curr # 移動prev 到curr
            curr = temp #移動curr 到temp

        return prev