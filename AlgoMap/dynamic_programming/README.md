# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|---------------|-------------|--------------|
| 509  | [Fibonacci Number](#509-fibonacci-number) | [Explanation](#509-fibonacci-number) | [Python Code](./509_fibonacci_number.py) |
| 70   | [Climbing Stairs](#70-climbing-stairs) | [Explanation](#70-climbing-stairs) | [Python Code](./070_climbing_stairs.py) |
| 746  | [Min Cost Climbing Stairs](#746-min-cost-climbing-stairs) | [Explanation](#746-min-cost-climbing-stairs) | [Python Code](./746_min_cost_climbing_stairs.py) |
| 198  | [House Robber](#198-house-robber)  | [Explanation](#198-house-robber) | [Python Code](./198_house_robber.py) |
| 62   | [Unique Paths](#62-unique-paths)    | [Explanation](#62-unique-paths) | [Python Code](./062_unique_paths.py) |
| 55   | [Jump Game](#55-jump-game) | [Explanation](#55-jump-game) | [Python Code](./055_jump_game.py) |
| 322  | [Coin Change](#322-coin-change)    | [Explanation](#322-coin-change) | [Python Code](./322_coin_change.py) |

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

## 746. Min Cost Climbing Stairs

**Description**:
You are given an integer array `cost` where `cost[i]` is the cost of `i`-th step on a staircase. Once you pay the cost, you can either climb one or two steps. You need to find the minimum cost to reach the top of the floor. You can either start from step 0 or step 1.

**Example**:
```plaintext
Input: cost = [10, 15, 20]
Output: 15
Explanation: You can start from step 1, pay 15, and reach the top.

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Start from step 0, and pay the following steps: 1 → 2 → 3 → 4 → 6 → top. Total cost = 1 + 1 + 1 + 1 + 1 = 6.
```

**Solution**:  
This problem can be solved using dynamic programming by calculating the minimum cost to reach each step. For each step, you can either come from the step before it or from two steps back. The cost to reach the current step is the minimum of these two options. By keeping track of the minimum costs for the last two steps as you move through the staircase, you can efficiently find the minimum cost to reach the top.

[Link to code](./746_min_cost_climbing_stairs.py)

**Notes**:
- Time complexity: O(n) because we go through the steps once.
- Space complexity: O(1) since we only use two variables (`prev` and `cur`) to store the minimum costs.

## 198. House Robber

**Description**:
You are a robber planning to steal from houses along a street. Each house has a certain amount of money, but if you rob two adjacent houses, you'll trigger the alarm. Determine the maximum amount of money you can steal without robbing two consecutive houses.

**Example**:
```plaintext
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), then rob house 3 (money = 9), and then rob house 5 (money = 1).
Total money you can rob = 2 + 9 + 1 = 12.
```

**Solution**:
This problem can be solved using dynamic programming. At each house, you can either rob it (and add its value to the maximum amount from two houses before) or skip it and take the maximum amount from the previous house. The recurrence relation is:  
`dp[i] = max(nums[i] + dp[i-2], dp[i-1])`

Instead of using an array to store all results, we optimize space by keeping track of the last two results (`prev` for `dp[i-2]` and `cur` for `dp[i-1]`), which we update as we move through the houses.

[Link to code](./198_house_robber.py)

**Notes**:
- Time complexity: O(n), where n is the number of houses.
- Space complexity: O(1), as we only use two variables to store intermediate results.

## 62. Unique Paths

**Description**:
A robot is located at the top-left corner of an `m x n` grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (i.e., `(m-1, n-1)`). How many possible unique paths are there to get to the destination?

**Example**:
```plaintext
Input:
m = 3, n = 7

Output: 28
```

**Solution**:
This problem can be efficiently solved using **dynamic programming**. The idea is to use a 1D array (`dp`) to store the number of ways to reach each cell in a row, reusing this array to calculate the result for the entire grid. At each cell, the number of unique paths is the sum of the paths from the cell above and the cell to the left. This reduces space complexity compared to a full 2D matrix.

[Link to code](./062_unique_paths.py)

**Notes**:
- Time complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns.
- Space complexity: O(n), as we use a single array to store the number of paths for each column.

## 55. Jump Game

**Description**:
You are given an array of non-negative integers `nums` where each element represents the maximum jump length at that position. Your goal is to determine if you can reach the last index starting from the first index.

**Example**:
```plaintext
Input:
nums = [2,3,1,1,4]

Output: True
```

**Solution**:
This problem can be efficiently solved by traversing the array from the back to the front. We maintain a `target` that starts at the last index, and for each index, we check if the value at that index is sufficient to reach the current target. If it is, we update the target to the current index. By the end of the loop, if the target reaches the starting index (0), it means it's possible to reach the last index.

[Link to code](./055_jump_game.py)

**Notes**:
- Time complexity: O(n), where `n` is the length of the input array `nums`.
- Space complexity: O(1), as we only use a constant amount of extra space.

## 322. Coin Change

**Description**:
You are given an integer array `coins` representing different denominations of coins, and an integer `amount` representing a total amount of money. The goal is to find the fewest number of coins needed to make up that amount. If it's not possible to make that amount, return -1.

**Example**:
```plaintext
Input:
coins = [1, 2, 5]
amount = 11

Output: 3
```

**Solution**:
This problem is a classic **dynamic programming** problem where we build up the solution for each amount from `1` to `amount`. We initialize a DP array where each entry represents the minimum number of coins required for that amount. For each amount, we check each coin denomination and calculate the fewest number of coins needed by comparing the current coin option with the previous results in the DP array.

[Link to code](./322_coin_change.py)

**Notes**:
- Time complexity: O(n * m), where `n` is the amount and `m` is the number of coins.
- Space complexity: O(n), where `n` is the amount.