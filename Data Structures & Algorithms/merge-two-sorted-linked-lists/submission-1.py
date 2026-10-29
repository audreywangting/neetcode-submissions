# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new listnode for append the smaller element between list1 and list2
        # if any of the list is None and the other is not, append the other one's head
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            # 要記得移動tail!!
            tail = tail.next

        if not list1 and list2:
            tail.next = list2
        if list1 and not list2:
            tail.next = list1

        return dummy.next