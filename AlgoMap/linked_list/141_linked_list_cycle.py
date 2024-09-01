class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hint: Use the two-pointer technique to detect a cycle.
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # Cycle detected
                return True

        return False  # No cycle found
