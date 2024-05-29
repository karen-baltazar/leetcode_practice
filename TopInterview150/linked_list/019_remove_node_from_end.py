# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Hint: Use two pointers. Move one pointer n steps ahead first, then move both pointers until the first one reaches the end.

        # Create a dummy node that points to the head of the list
        dummy = ListNode(0, head)
        # Initialize two pointers, left starting from dummy and right from head
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end of the list
        while right:
            left = left.next
            right = right.next

        # Skip the nth node from the end
        left.next = left.next.next

        # Return the head of the modified list
        return dummy.next
