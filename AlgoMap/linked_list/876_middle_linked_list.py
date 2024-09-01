class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hint: Use the two-pointer technique to find the middle node.
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow  # The slow pointer will be at the middle node
