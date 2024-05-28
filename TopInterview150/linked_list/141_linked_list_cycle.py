# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # Hint: Why is moving one pointer twice as fast as the other effective for cycle detection?

        # Initialize two pointers, slow and fast, both starting at the head of the list
        slow, fast = head, head

        # Traverse the linked list with two pointers
        while fast and fast.next:
            slow = slow.next  # Move slow pointer by one step
            fast = fast.next.next  # Move fast pointer by two steps

            # If slow and fast meet, there's a cycle in the list
            if slow == fast:
                return True

        # If we reach the end of the list, there's no cycle
        return False
