# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|---------------|-------------|--------------|
| 509  | [Fibonacci Number](#509-fibonacci-number) | [Explanation](#509-fibonacci-number) | [Python Code](./509_fibonacci_number.py) |
| 70   | [Climbing Stairs](#70-climbing-stairs) | [Explanation](#70-climbing-stairs) | [Python Code](./070_climbing_stairs.py) |

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

## 70. Climbing Stairs

**Description**:
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Given `n`, the number of steps, return the number of distinct ways you can reach the top.

**Example**:
```plaintext
Input: n = 5
Output: 8
Explanation: There are 8 distinct ways to climb to the top (steps: [1,1,1,1,1], [1,1,1,2], [1,1,2,1], [1,2,1,1], [2,1,1,1], [2,2,1], [2,1,2], [1,2,2]).
```

**Solution**:
This problem can be solved using a **dynamic programming** approach, where the idea is similar to the Fibonacci sequence. At any given step `i`, you can get there by either:
1. Taking one step from step `i - 1`.
2. Taking two steps from step `i - 2`.

The total number of ways to reach step `i` is the sum of the ways to reach steps `i - 1` and `i - 2`. This is the same recurrence relation as Fibonacci.

We can optimize the space complexity by using two variables to track the previous two steps rather than storing all the steps in an array.

Steps:
1. Initialize two variables to store the number of ways to reach the first and second steps.
2. Use a loop to calculate the number of ways to reach each step from 3 to `n`.
3. Return the number of ways to reach the top (`n`).

[Link to code](./070_climbing_stairs.py)

**Notes**:
- Time complexity: O(n) because we calculate the number of ways for each step in a single pass.
- Space complexity: O(1) because we only use two variables to store the results of the previous two steps.