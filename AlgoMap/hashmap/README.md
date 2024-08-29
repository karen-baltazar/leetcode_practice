# Problems

| Problem Number | Problem Name                       | Explanation                                      | Code                                      |
|----------------|------------------------------------|--------------------------------------------------|-------------------------------------------|
| 771            | [Jewels and Stones](#771-jewels-and-stones) | [Explanation](#771-jewels-and-stones)  | [Python Code](./771_jewels_and_stones.py) |

## 771. Jewels and Stones

**Description**:
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

**Example**:
```plaintext
Input:
jewels = "aA"
stones = "aAAbbbb"

Output: 3
```

**Solution**:
The problem can be efficiently solved by converting the `jewels` string into a set, which allows O(1) lookup time for checking whether each stone is a jewel. We then iterate over the `stones` string, counting how many of the stones are also jewels.

[Link to code](771_jewels_and_stones.py)

**Notes**:
- Time complexity: O(n + m), where n is the length of `jewels` and m is the length of `stones`.
- Space complexity: O(n), for the set created from `jewels`.