# Problems

## 125. Valid Palindrome

**Description**:
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Example**:
```plaintext
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

**Solution**:
This solution utilizes a two-pointer approach to check if a string is a palindrome. We iterate through the string from both ends, comparing characters while skipping non-alphanumeric characters and ignoring case sensitivity.

[Link to code](125_valid_palindrome.py)

**Notes**:
- Time complexity: O(n), where n is the length of the string s.
- Space complexity: O(1), as the comparison is done in-place without using extra space.

## 392. Is Subsequence

**Description**:
Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

**Example**:
```plaintext
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Solution**:
This solution determines if string `s` is a subsequence of string `t` by iteratively comparing characters. It tracks the position of matching characters in `s`, iterating through `t`, and returns true if `s` is fully matched within `t`.

[Link to code](392_is_subsequence.py)

**Notes**:
- Time complexity: O(n), where n is the length of string t.
- Space complexity: O(1), as no extra space is used beyond the input strings.
