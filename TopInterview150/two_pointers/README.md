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
