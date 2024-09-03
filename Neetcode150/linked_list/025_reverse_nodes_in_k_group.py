class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Hint: Reverse every k nodes in the list and connect the sublist directly to the next part.

        # Helper function to reverse a sublist and connect it to the next group
        def reverseSublist(start, end_next):
            prev, curr = None, start
            while curr != end_next:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            start.next = end_next  # Directly connect the reversed sublist to the next group
            return prev  # New head of the reversed sublist

        # Count the total number of nodes in the list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        # Create a dummy node to help with the manipulation of the list
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while count >= k:
            group_start = group_prev.next
            group_end = group_start

            # Move the group_end pointer to the end of the k nodes
            for i in range(k - 1):
                group_end = group_end.next

            # The next group starts after group_end
            next_group_start = group_end.next

            # Reverse the current k-group and directly connect it to the next group
            new_group_start = reverseSublist(group_start, next_group_start)

            # Connect the reversed group with the previous part of the list
            group_prev.next = new_group_start

            # Move to the next group
            group_prev = group_start
            count -= k

        return dummy.next
