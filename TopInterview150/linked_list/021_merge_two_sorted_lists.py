# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        tail = dummy

        # Traverse both lists until one of them is exhausted
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Move to the next node in the merged list
            tail = tail.next

        # If there are remaining nodes, attach them to the merged list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the merged list, skipping the dummy node
        return dummy.next

# Note: The dummy node is used to provide a starting point for the merged list. 
# It simplifies the handling of edge cases by avoiding the need to check if the merged 
# list is empty at each step. Once the merging is complete, we return dummy.next to skip 
# the dummy node and return the actual merged list.
