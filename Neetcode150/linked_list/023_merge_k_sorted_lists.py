# Hint: Use a divide and conquer approach to iteratively merge pairs of linked lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # If the input is empty, return None
        if not lists or len(lists) == 0:
            return 
        
        def mergeList(l1, l2):
            # Create a dummy node to help with merging two lists
            dummy = ListNode()
            tail = dummy

            # Merge two sorted lists
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            # If there are remaining nodes in either l1 or l2, attach them
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2

            return dummy.next

        # Merge lists in pairs until only one list remains
        while len(lists) > 1:
            mergedLists = []

            # Iterate through lists two at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeList(l1, l2))
            lists = mergedLists

        # The last remaining list is the merged result
        return lists[0]
