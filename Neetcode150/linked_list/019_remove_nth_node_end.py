class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Hint: Use two pointers to find the N-th node from the end.
        dummy = ListNode(next=head)
        left = right = dummy

        # Move the right pointer n+1 steps ahead
        for _ in range(n + 1):
            right = right.next

        # Move both pointers until the right pointer reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the N-th node from the end
        left.next = left.next.next

        return dummy.next
