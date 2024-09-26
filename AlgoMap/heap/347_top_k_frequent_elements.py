from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # Frequency count of elements
        buckets = [[] for _ in range(len(nums) + 1)]  # Buckets to group by frequency

        # Fill buckets based on frequency
        for num, count in freq.items():
            buckets[count].append(num)

        top_k = []
        # Collect top k frequent elements from highest frequency bucket
        for i in range(len(buckets) - 1, 0, -1):
            top_k.extend(buckets[i])
            if len(top_k) >= k:  # Stop when k elements are collected
                return top_k[:k]
