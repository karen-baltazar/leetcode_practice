# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # Hint: Use two pointers, one to track the node before the sequence of duplicates, and the other to traverse the list.
        
        # Create a dummy node to handle edge cases such as the head itself being a duplicate
        dummy = ListNode(0, head)
        # Pointer to the previous node
        prev = dummy

        # Traverse the list
        while head:
            # If the current node has a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link the previous node to the node after the last duplicate
                prev.next = head.next
            else:
                # Move the previous pointer forward if no duplicate
                prev = prev.next
            
            # Move to the next node
            head = head.next

        return dummy.next
