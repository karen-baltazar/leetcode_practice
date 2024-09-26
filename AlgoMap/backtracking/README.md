# Problems

| Problem Number | Problem Name      | Explanation                                     | Code                                         |
|----------------|-------------------|-------------------------------------------------|----------------------------------------------|
| 78   | [Subsets](#78-subsets) | [Explanation](#78-subsets) | [Python Code](./078_subsets.py) |
| 46   | [Permutations](#46-permutations)  | [Explanation](#46-permutations) | [Python Code](./046_permutations.py) |
| 77    | [Combinations](#77-combinations)   | [Explanation](#77-combinations) | [Python Code](./077_combinations.py) |

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

## 46. Permutations

**Description**:
Given an array of distinct integers, return all the possible permutations. You can return the answer in any order.

**Example**:
```plaintext
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Solution**:
We use a backtracking approach to explore all permutations. The function recursively adds unused numbers to the current permutation and backtracks when it reaches the length of the input list.

[Link to code](./046_permutations.py)

**Notes**:
- Time complexity: O(n * n!), where n is the length of the input list. Each permutation is generated, and each is stored.
- Space complexity: O(n), for the recursion stack and storage of the result.

## 77. Combinations

**Description**:
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n]. You can return the answer in any order.

**Example**:
```plaintext
Input: n = 4, k = 2
Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

**Solution**:
The approach uses backtracking to explore all possible combinations of k elements from 1 to n. It builds combinations recursively by adding elements one at a time and backtracks when the desired combination length is reached.

[Link to code](./077_combinations.py)

**Notes**:
- Time complexity: O(C(n, k)), where C(n, k) is the number of combinations.
- Space complexity: O(k), due to the recursion stack and storing current combinations.