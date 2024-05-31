# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Hint: Reverse the sublist from left to right using three pointers (prev, cur, and tmpNext).
        
        # Create a dummy node to simplify edge cases where reversing starts from the head
        dummy = ListNode(0, head)

        # Initialize pointers to traverse to the node just before the left position
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Reverse the sublist from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # Connect the reversed sublist back to the original list
        leftPrev.next.next = cur
        leftPrev.next = prev

        # Return the new head of the list
        return dummy.next
