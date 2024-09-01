class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Hint: Traverse both linked lists simultaneously, adding corresponding values and managing carry.
        dummy = ListNode()
        current = dummy 
        carry = 0

        while l1 or l2 or carry:
            # Get the values from the current nodes or 0 if one list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the remainder of the division by 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next