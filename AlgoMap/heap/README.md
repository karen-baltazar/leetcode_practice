# Problems

| Problem Number | Problem Name                                   | Explanation                                      | Code                                           |
|----------------|------------------------------------------------|--------------------------------------------------|------------------------------------------------|
| 1046 | [Last Stone Weight](#1046-last-stone-weight) | [Explanation](#1046-last-stone-weight)         | [Python Code](./1046_last_stone_weight.py)  |

## 1046. Last Stone Weight

**Description**:
You are given an array of integers `stones` where `stones[i]` is the weight of the i-th stone. Smash the two heaviest stones together. If they have the same weight, both are destroyed; if not, the heavier stone is reduced by the lighter stone's weight. Return the weight of the last remaining stone or 0 if none are left.

**Example**:
```plaintext
Input: stones = [2,7,4,1,8,1]
Output: 1
```

**Solution**:
We use a max-heap to track the heaviest stones. By negating the weights, we can utilize Python's min-heap. We repeatedly pop the two heaviest stones and push the difference back into the heap until one or no stones remain.

[Link to code](./1046_last_stone_weight.py)

**Notes**:
- Time complexity: O(n log n). This arises from the need to heapify the list and perform heap operations (push and pop), which each take O(log n) time.
- Space complexity: O(n) due to storing the stones in the heap.