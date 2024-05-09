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
To check if a string is a palindrome, we can utilize a two-pointer approach. We filter out non-alphanumeric characters, convert the string to lowercase, and then compare characters symmetrically from both ends.

[Link to code](125_valid_palindrome.py)

**Notes**:
- Time complexity: O(n), where n is the length of the string s.
- Space complexity: O(1), as the comparison is done in-place without using extra space.