from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []  # Min-heap to store the nodes

        # Initialize the heap with the first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()  # Dummy node to simplify merging
        cur = dummy  # Pointer to build the merged list

        while heap:
            val, i, node = heapq.heappop(heap)  # Get the smallest node
            cur.next = node  # Add it to the merged list
            cur = cur.next  # Move the pointer forward
            node = node.next  # Move to the next node in the list
            
            if node:  # If there's a next node, add it to the heap
                heapq.heappush(heap, (node.val, i, node))

        return dummy.next  # Return the merged list
