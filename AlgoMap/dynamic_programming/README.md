# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|---------------|-------------|--------------|
| 509  | [Fibonacci Number](#509-fibonacci-number) | [Explanation](#509-fibonacci-number) | [Python Code](./509_fibonacci_number.py) |

## 509. Fibonacci Number

**Description**:
The Fibonacci sequence is defined as follows:
- F(0) = 0
- F(1) = 1
- F(n) = F(n - 1) + F(n - 2) for n > 1

Given `n`, calculate F(n).

**Example**:
```plaintext
Input: n = 5
Output: 5
Explanation: The Fibonacci sequence is [0, 1, 1, 2, 3, 5], and F(5) = 5.
```

**Solution**:
We can solve this problem using **dynamic programming** to avoid redundant calculations. Instead of recalculating Fibonacci numbers multiple times, we store the results in an array (DP array). This way, we can compute each Fibonacci number only once, improving the efficiency of the algorithm.

The approach involves:
1. Initializing a DP array where `dp[i]` represents the Fibonacci number `F(i)`.
2. Setting the base cases: `dp[0] = 0` and `dp[1] = 1`.
3. Using a loop to calculate each Fibonacci number starting from `dp[2]` to `dp[n]` by summing the two previous numbers.
4. Returning `dp[n]` as the result, which is the Fibonacci number for `n`.

[Link to code](./509_fibonacci_number.py)

**Notes**:
- Time complexity: O(n), since we compute each Fibonacci number once.
- Space complexity: O(n), due to the space required to store the Fibonacci numbers in the DP array.