class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hint: Use a frequency count and bucket sort to efficiently find the top k elements.

        # Dictionary to count the frequency of each number
        count = {}
        # List of lists to store numbers according to their frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Count the frequency of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Organize the numbers in the freq list according to their frequency
        for n, c in count.items():
            freq[c].append(n)

        # List to store the k most frequent elements
        top = []
        # Iterate over the freq list from the end to the beginning
        # to get elements with the highest frequencies
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                top.append(n)
                # If we have added k elements, return the top list
                if len(top) == k:
                    return top
