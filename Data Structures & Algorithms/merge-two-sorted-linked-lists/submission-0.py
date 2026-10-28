# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use dummy head to crea a merged list
        # use tail to keep joining the new node
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2: # 只有兩條list都在時才要一起比較iterate
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next # !! dummy指向虛擬0