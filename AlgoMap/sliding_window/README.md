# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 643            | [Maximum Average Subarray I](#643-maximum-average-subarray-i) | [Explanation](#643-maximum-average-subarray-i)       | [Python Code](./643_maximum_average_subarray.py) |
| 1004           | [Max Consecutive Ones III](#1004-max-consecutive-ones-iii) | [Explanation](#1004-max-consecutive-ones-iii)        | [Python Code](./1004_max_consecutive_ones_iii.py) |
| 3              | [Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters) | [Explanation](#3-longest-substring-without-repeating-characters) | [Python Code](./003_longest_substring.py)      |
| 424            | [Longest Repeating Character Replacement](#424-longest-repeating-character-replacement) | [Explanation](#424-longest-repeating-character-replacement) | [Python Code](./424_character_replacement.py) |
| 209            | [Minimum Size Subarray Sum](#209-minimum-size-subarray-sum) | [Explanation](#209-minimum-size-subarray-sum) | [Python Code](./209_min_subarray_sum.py) |
| 567            | [Permutation in String](#567-permutation-in-string) | [Explanation](#567-permutation-in-string)            | [Python Code](./567_permutation_in_string.py) |

## 643. Maximum Average Subarray I

**Description**:
Given an integer array `nums` and an integer `k`, find the contiguous subarray of length `k` that has the maximum average value, and return this value.

**Example**:
```plaintext
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
```

**Solution**:
The solution uses a sliding window approach. Initially, the sum of the first `k` elements is calculated. Then, as the window slides through the array, the sum is adjusted by subtracting the element that leaves the window and adding the element that enters. The maximum sum encountered during this process is recorded, and the maximum average is obtained by dividing this sum by `k`.

[Link to code](./643_maximum_average_subarray.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the array.
- Space complexity: O(1), as only a few variables are used for the sliding window calculation.

## 1004. Max Consecutive Ones III

**Description**:
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.

**Example**:
```plaintext
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
```

**Solution**:
The solution uses a sliding window approach. We expand the window by moving the `right` pointer across the array and count the number of `0`s encountered. If the count of `0`s exceeds `k`, we shrink the window from the left by moving the `left` pointer until the number of `0`s is back within the allowed limit. The length of the longest valid window gives the desired result.

[Link to code](./1004_max_consecutive_ones_iii.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array.
- Space complexity: O(1), as only a few variables are used to track the window and the count of zeros.

## 3. Longest Substring Without Repeating Characters

**Description**:
Given a string `s`, find the length of the longest substring without repeating characters.

**Example**:
```plaintext
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Solution**:
The problem can be efficiently solved using a sliding window approach. The idea is to maintain a window using two pointers, `left` and `right`, which represent the current substring. As the `right` pointer expands the window, if a duplicate character is found, the `left` pointer is moved to shrink the window until the substring is valid again (i.e., contains no repeating characters). The `max_length` variable keeps track of the maximum length of any valid substring encountered during the process.

[Link to code](./003_longest_substring.py)

**Notes**:
- Time complexity: O(n), where n is the length of the string.
- Space complexity: O(min(n, m)), where m is the size of the character set.

## 424. Longest Repeating Character Replacement

**Description**:
Given a string `s` and an integer `k`, you are allowed to replace up to `k` characters in the string, and you need to find the length of the longest substring containing the same letter after performing at most `k` replacements.

**Example**:
```plaintext
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'B' in "AABABBA" to get "AAAA", which has the longest repeating letters.
```

**Solution**:
The solution employs a sliding window technique to efficiently find the longest valid substring that can be transformed into a string with all identical characters by replacing at most `k` characters.

1. **Sliding Window Mechanism**:
   - The window is defined by two pointers, `left` and `right`, which represent the start and end of the current substring under consideration.
   - As the `right` pointer expands the window by moving to the right, the count of each character within the window is tracked using an array `char_count`.

2. **Validity Check**:
   - At each step, the algorithm checks if the current window is valid. A window is considered valid if the number of characters that need to be replaced (i.e., the total number of characters in the window minus the count of the most frequent character) does not exceed `k`.
   - The check is performed using the condition `(right - left + 1) - max(char_count) <= k`. If this condition holds true, the window is valid, and we may have found a new maximum length for a valid substring.

3. **Handling Invalid Windows**:
   - If the window becomes invalid (i.e., the condition above is false), the algorithm adjusts by moving the `left` pointer to the right, effectively shrinking the window from the left. This process continues until the window becomes valid again.
   - The character count for the character that is being excluded (at the `left` pointer) is decremented as the window shrinks.

4. **Updating the Maximum Length**:
   - Throughout this process, the algorithm keeps track of the maximum length of any valid window encountered.

By the end of the iteration, the length of the longest valid window is returned, representing the longest substring that can be obtained by replacing at most `k` characters to make all characters in the substring the same.

[Link to code](./424_character_replacement.py)

**Notes**:
- Time complexity: O(n), where n is the length of the string `s`.
- Space complexity: O(1), since the size of the `char_count` array is constant (26 for uppercase English letters).

## 209. Minimum Size Subarray Sum

**Description**:
Given an array `nums` and an integer `target`, find the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If no such subarray exists, return 0.

**Example**:
```plaintext
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] is the smallest subarray with a sum of at least 7.

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
Explanation: No subarray has a sum greater than or equal to 11.
```

**Solution**:
The solution employs the sliding window technique to efficiently find the minimal subarray length. It maintains a window defined by two pointers, `left` and `right`. As the `right` pointer expands the window by iterating through the array and accumulating the sum, the `left` pointer shrinks the window from the left when the sum meets or exceeds the target. During this process, the algorithm keeps track of the minimum length of valid subarrays. If no valid subarray is found, it returns 0.

[Link to code](./209_min_subarray_sum.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array `nums`.
- Space complexity: O(1), as it uses only a few variables.

## 567. Permutation in String

**Description**:
Given two strings `s1` and `s2`, determine if `s2` contains a permutation of `s1`. In other words, check if one of `s1`'s permutations is a substring of `s2`.

**Example**:
```plaintext
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
Explanation: s2 does not contain any permutation of s1.
```

**Solution**:
The solution involves creating frequency counts for the characters in `s1` and comparing them with a sliding window of the same length in `s2`. If the frequency counts match at any point, it indicates that `s2` contains a permutation of `s1`. The window slides across `s2`, adjusting the frequency count by removing the character that goes out of the window and adding the new character that enters the window.

[Link to code](./567_permutation_in_string.py)

**Notes**:
- Time complexity: O(n), where n is the length of `s2`.
- Space complexity: O(1), since the frequency array has a fixed size of 26.