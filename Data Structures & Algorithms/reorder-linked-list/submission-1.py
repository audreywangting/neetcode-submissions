# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. cut the list into half
        # 2. reverse the second half list
        # 3. merge the first half & the second half

        # 1. use slow & fast pointer
            # when the fast pointer reaches the end of the list, 
            # slow pointer reaches the middle of the list
            # slow.next as the head of the second half 
        slow = head
        fast = head 
        while fast.next and fast.next.next: 
            slow = slow.next
            fast = fast.next.next
        
        h2 = slow.next 
        slow.next = None


        # 2. prev, curr, temp ptr 
            # temp keep curr's place
            # change the ptr's direction
            # move the ptr
            # prev = head of the reverse list
        prev = None
        curr = h2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # new head: prev

        # 3. use temp1 & temp2 ptr, merging two list (head & prev)
            # 1, 2, 3
            # h, t1

            # 6, 5, 4
            # p, t2

            # 1, 6, 2, 5, 3, 4 
            # h, p, t1, t2 
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

        return 
        




