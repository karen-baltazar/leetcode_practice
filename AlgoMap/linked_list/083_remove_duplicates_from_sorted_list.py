class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hint: Traverse the list, and whenever a duplicate is found, adjust the pointers to skip it.
        current = head

        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            
            current = current.next

        return head
