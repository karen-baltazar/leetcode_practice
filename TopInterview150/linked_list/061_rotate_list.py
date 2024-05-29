# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):        
        # Hint: First make the list a circular one, then find the new tail and break the circle.

        # If the list is empty, return the head
        if not head:
            return head

        # Initialize the length of the list and set the tail to the head initially
        length, tail = 1, head

        # Traverse the list to find the length and the tail node
        while tail.next:
            tail = tail.next
            length += 1

        # Find the effective rotations needed as k could be larger than length
        k = k % length

        # If no rotation is needed, return the head
        if k == 0:
            return head

        # Move to the new tail, which is (length - k - 1) nodes from the start
        cur = head
        for i in range(length - k - 1):
            cur = cur.next

        # The new head is the node next to the new tail
        newHead = cur.next
        # Break the list to make it non-circular again
        cur.next = None
        # Connect the old tail to the old head to complete the rotation
        tail.next = head

        # Return the new head
        return newHead
