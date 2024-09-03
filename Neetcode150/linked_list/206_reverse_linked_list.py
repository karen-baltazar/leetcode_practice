class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hint: Use a dummy node and rearrange the pointers as you traverse the list.
        dummy = ListNode()

        while head:
            temp = head  # Temporarily store the current node.
            head = head.next  # Move to the next node.
            temp.next = dummy.next  # Insert the node at the beginning of the reversed list.
            dummy.next = temp  # Update the dummy's next to the newly added node.

        return dummy.next
