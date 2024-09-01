class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Solution 1: Using a Dictionary (Commented Out)
        # n = 0
        # node_map = {}
        #
        # current = head
        # while current:
        #     n += 1
        #     node_map[n] = current
        #     current = current.next
        #
        # node_map[(n // 2) + 1].next = None
        # op = (n // 2) - 1 if n % 2 == 0 else n // 2
        #
        # current = head
        # for i in range(op):
        #     temp = current.next
        #     current.next = node_map[n]
        #     current.next.next = temp
        #     current = temp
        #     n -= 1

        # Solution 2: Two Pointers Approach
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge the two halves
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
