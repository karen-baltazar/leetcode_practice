# Problems

| Problem Number | Problem Name                      | Explanation                                           | Code                                            |
|----------------|-----------------------------------|-------------------------------------------------------|-------------------------------------------------|
| 90  | [Subsets II](#90-subsets-ii)     | [Explanation](#90-subsets-ii) | [Python Code](./090_subsets_ii.py) |

## 90. Subsets II

**Description**:
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**Example**:
```plaintext
Input: nums = [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
Explanation: The subsets contain duplicates, so [2] and [2, 2] should only appear once.
```

**Solution**:
The approach uses backtracking to explore all possible subsets:
- Sort the array to handle duplicates easily.
- Use a recursive function to decide whether to include each number.
- Skip over duplicates during the recursive exploration.

[Link to code](./090_subsets_ii.py)

**Notes**:
- Time complexity: O(n * 2^n) due to generating all subsets and creating copies of subsets.
- Space complexity: O(n) for the recursion stack and storing subsets.