# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. use fast & slow pointers to find the mid of the list
            # when the fast reaches the end, slow reaches the mid
        # 2. reverse the second half of the list
        # 3. merge the reversed half and the first half in between
        
        # 1. find the mid
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next 
        slow.next = None

        # 2. reverse the second half
        curr = second
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # new head = prev

        # 3. merge first & second half
        first = head
        second = prev

        while second: # 因為後半不會長於前半
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        









        

