# Problems

| Problem Number | Problem Name      | Explanation                                     | Code                                         |
|----------------|-------------------|-------------------------------------------------|----------------------------------------------|
| 78   | [Subsets](#78-subsets) | [Explanation](#78-subsets) | [Python Code](./078_subsets.py) |

## 78. Subsets

**Description**:
Given a set of distinct integers, nums, return all possible subsets (the power set).

**Example**:
```plaintext
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

**Solution**:
We use a backtracking approach to explore all subsets. For each element, we decide to either include it in the current subset or exclude it. This allows us to build subsets recursively.

[Link to code](./078_subsets.py)

**Notes**:
- Time complexity: O(2^n), where n is the number of elements in `nums`, as each element can either be included or excluded.
- Space complexity: O(n), for the space used by the recursion stack and storing subsets.