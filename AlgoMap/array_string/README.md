# Problems

| Problem Number | Problem Name                                   | Explanation                                    | Code                                                  |
|----------------|------------------------------------------------|------------------------------------------------|-------------------------------------------------------|
| 2239           | [Find Closest Number to Zero](#2239-find-closest-number-to-zero) | [Explanation](#2239-find-closest-number-to-zero) | [Python Code](./2239_find_closest_number_to_zero.py) |
| 1768           | [Merge Strings Alternately](#1768-merge-strings-alternately) | [Explanation](#1768-merge-strings-alternately) | [Python Code](./1768_merge_strings_alternately.py)  |
| 13             | [Roman to Integer](#13-roman-to-integer) | [Explanation](#13-roman-to-integer)               | [Python Code](./13_roman_to_integer.py)            |
| 392            | [Is Subsequence](#392-is-subsequence) | [Explanation](#392-is-subsequence)               | [Python Code](./392_is_subsequence.py)             |
| 121            | [Buy Sell Stock](#121-best-time-to-buy-and-sell-stock) | [Explanation](#121-best-time-to-buy-and-sell-stock)          | [Python Code](./121_buy_sell_stock.py)       |
| 14             | [Longest Common Prefix](#14-longest-common-prefix) | [Explanation](#14-longest-common-prefix) | [Python Code](./14_longest_common_prefix.py) |
| 228            | [Summary Ranges](#228-summary-ranges) | [Explanation](#228-summary-ranges) | [Python Code](./228_summary_ranges.py) |
| 238            | [Product of Array Except Self](#238-product-of-array-except-self) | [Explanation](#238-product-of-array-except-self) | [Python Code](./238_product_of_array_except_self.py) |
| 56             | [Merge Intervals](#56-merge-intervals) | [Explanation](#56-merge-intervals) | [Python Code](./56_merge_intervals.py) |

## 2239. Find Closest Number to Zero

**Description**:
Given an integer array `nums`, return the number with the smallest absolute value. If there are multiple numbers with the same smallest absolute value, return the positive number.

**Example**:
```plaintext
Input:
nums = [-4, -2, 1, 4]

Output: 1
```

**Solution**:
To find the number with the smallest absolute value, iterate through the list while tracking the number with the smallest absolute value. If two numbers have the same smallest absolute value, return the positive number.

[Link to code](2239_find_closest_number_to_zero.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input list `nums`.
- Space complexity: O(1), since no additional space is used beyond a few variables.

## 1768. Merge Strings Alternately

**Description**:
Given two strings `word1` and `word2`, merge them alternately to form a new string. The characters of `word1` and `word2` should be alternated as long as possible. If one string is longer than the other, append the remaining characters of the longer string at the end.

**Example**:
```plaintext
Input:
word1 = "abc"
word2 = "pqrstu"

Output: "apbqcrstu"
```

**Solution**:
To merge the strings alternately, iterate through both strings and add characters from each string to the result list in turn. After reaching the end of the shorter string, append the remaining characters from the longer string.

[Link to code](1768_merge_strings_alternately.py)

**Notes**:
- Time complexity: O(m + n), where m and n are the lengths of `word1` and `word2`, respectively.
- Space complexity: O(m + n), due to the space needed to store the merged string.

## 13. Roman to Integer

**Description**:
Convert a Roman numeral string to an integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. When a smaller numeral appears before a larger one, it indicates subtraction. For example, IV is 4, and IX is 9.

**Example**:
```plaintext
Input:
s = "MCMXCIV"

Output: 1994
```

**Solution**:
To convert a Roman numeral string to an integer, use a dictionary to map each Roman numeral to its corresponding integer value. Traverse the string while checking for subtractive cases where a smaller numeral precedes a larger one.

[Link to code](13_roman_to_integer.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input string.
- Space complexity: O(1), since the space used is independent of the input size.

## 392. Is Subsequence

**Description**:
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

**Example**:
```plaintext
Input:
s = "abc", t = "ahbgdc"

Output: true
```

**Solution**:
To determine if `s` is a subsequence of `t`, use two pointers: one for each string. Traverse `t` and try to match characters in `s`. If you can match all characters of `s` in order, `s` is a subsequence of `t`.

[Link to code](392_is_subsequence.py)

**Notes**:
- Time complexity: O(n), where n is the length of string `t`.
- Space complexity: O(1), as only a few extra variables are used.

## 121. Best Time to Buy and Sell Stock

**Description**:
Given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day, find the maximum profit you can achieve from this stock by buying on one day and selling on another day.

**Example**:
```plaintext
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
```

**Solution**:
To maximize profit, we want to find the maximum difference between two prices (buying price and selling price). We iterate through the prices array and keep track of the minimum price encountered so far. For each price, we calculate the profit if we sell at that price and update the maximum profit if necessary.

[Link to code](121_buy_sell_stock.py)

**Notes**:
- Time complexity: O(n), where n is the length of the prices array.
- Space complexity: O(1), as the algorithm uses only a constant amount of extra space.

## 14. Longest Common Prefix

**Description**:
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

**Example**:
```plaintext
Input:
strs = ["flower","flow","flight"]

Output: "fl"
```

**Solution**:
To find the longest common prefix, determine the minimum length among all strings and then compare characters at each position up to that length. Return the common prefix found during this comparison.

[Link to code](14_longest_common_prefix.py)

**Notes**:
- Time complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.
- Space complexity: O(1), as only a few extra variables are used.

## 228. Summary Ranges

**Description**:
Given a sorted integer array without duplicates, return the summary of its ranges. A range `[a,b]` is represented as a string `a->b` if `a` is not equal to `b`. Otherwise, it is represented as a string `a`.

**Example**:
```plaintext
Input:
nums = [0,1,2,4,5,7]

Output: ["0->2","4->5","7"]
```

**Solution**:
To summarize ranges, traverse the list and identify continuous sequences. Use a while loop to determine the start and end of each range, then format and store these ranges accordingly.

[Link to code](228_summary_ranges.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the input list.
- Space complexity: O(n), as the result list stores all ranges.

## 238. Product of Array Except Self

**Description**:
Given an integer array `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Example**:
```plaintext
Input:
[1,2,3,4]

Output:
[24,12,8,6]
```

**Solution**:
To solve this problem without using division, we can use two passes over the array. The first pass calculates the prefix products (product of all elements before the current element), and the second pass calculates the postfix products (product of all elements after the current element) and combines them with the prefix products.

**Python Code**:
[Link to code](238_product_of_array_except_self.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of elements in the input array.
- Space complexity: O(1) (excluding the space used for the output array).

## 56. Merge Intervals

**Description**:
Given a collection of intervals, merge all overlapping intervals. An interval `[a, b]` is represented as a list of integers `[a, b]`. The goal is to combine all intervals that overlap into one continuous interval.

**Example**:
```plaintext
Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]
```

**Solution**:
Sort the intervals by their starting points. Then, iterate through the sorted intervals and merge overlapping intervals by comparing the end of the last interval in the merged list with the start of the current interval.

[Link to code](56_merge_intervals.py)

**Notes**:
- Time complexity: O(n log n), due to the sorting step.
- Space complexity: O(n), for storing the merged intervals.