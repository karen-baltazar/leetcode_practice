# Problems

| Problem Number | Problem Name                                   | Explanation                                    | Code                                                  |
|----------------|------------------------------------------------|------------------------------------------------|-------------------------------------------------------|
| 2239           | [Find Closest Number to Zero](#2239-find-closest-number-to-zero) | [Explanation](#2239-find-closest-number-to-zero) | [Python Code](./2239_find_closest_number_to_zero.py) |
| 1768           | [Merge Strings Alternately](#1768-merge-strings-alternately) | [Explanation](#1768-merge-strings-alternately) | [Python Code](./1768_merge_strings_alternately.py)  |
| 13             | [Roman to Integer](#13-roman-to-integer) | [Explanation](#13-roman-to-integer)               | [Python Code](./13_roman_to_integer.py)            |

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