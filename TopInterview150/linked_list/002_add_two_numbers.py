# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Hint: What happens if the two lists have different lengths?
        
        # Create a dummy node to form the result list
        dummy = ListNode()
        # Pointer to the current node in the result list
        cur = dummy
        # Variable to store carry over
        carry = 0

        # Traverse both lists until the end
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if one list is shorter
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the new digit and carry over
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # Create a new node with the calculated value
            cur.next = ListNode(val)

            # Move to the next nodes in the lists and the result list
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result list, skipping the dummy node
        return dummy.next
