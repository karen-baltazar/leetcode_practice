# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 76             | [Minimum Window Substring](#76-minimum-window-substring) | [Explanation](#76-minimum-window-substring)          | [Python Code](./076_minimum_window_substring.py) |
| 239 | [Sliding Window Maximum](#239-sliding-window-maximum) | [Explanation](#239-sliding-window-maximum) | [Python Code](./239_sliding_window_maximum.py) |
| 3              | [Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters) | [Explanation](#3-longest-substring-without-repeating-characters) | [Python Code](./003_longest_substring.py)      |
| 424            | [Longest Repeating Character Replacement](#424-longest-repeating-character-replacement) | [Explanation](#424-longest-repeating-character-replacement) | [Python Code](./424_character_replacement.py) |
| 567            | [Permutation in String](#567-permutation-in-string) | [Explanation](#567-permutation-in-string)            | [Python Code](./567_permutation_in_string.py) |

## 76. Minimum Window Substring

**Description**:
Given two strings `s` and `t`, return the minimum window in `s` which will contain all the characters in `t`. If there is no such window in `s` that covers all characters in `t`, return an empty string `""`.

**Example**:
```plaintext
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Solution**:
This problem is solved using a sliding window technique combined with a hash map to keep track of the frequency of characters in both `t` and the current window of `s`. The idea is to use two pointers (`left` and `right`) to form a window that can slide over `s`.

1. **Initial Setup**: 
   - We first create a frequency map (`t_freq`) to count the occurrences of each character in `t`.
   - We also maintain a `window` frequency map for the current window in `s`.
   - Two pointers, `left` and `right`, are initialized to define the boundaries of the window.

2. **Expanding the Window**:
   - We start expanding the window by moving the `right` pointer to the right through the string `s`.
   - For each character added to the window, we update the `window` frequency map.
   - If the frequency of the current character in the window matches its required frequency in `t`, we increment a `have` counter.

3. **Contracting the Window**:
   - Once all characters from `t` are within the window (`have == need`), we try to minimize the window size by moving the `left` pointer to the right.
   - During this contraction, if the current window length is smaller than any previously recorded window, we update our result.
   - If moving the `left` pointer causes the window to lose a necessary character (i.e., `have` becomes less than `need`), we stop contracting and continue expanding with the `right` pointer.

4. **Result**:
   - The process continues until the `right` pointer has traversed the entire string `s`. The smallest valid window recorded is the answer.

This approach efficiently narrows down the minimal window containing all characters of `t` by balancing expansion and contraction, ensuring that the solution is optimal.

[Link to code](./076_minimum_window_substring.py)

**Notes**:
- Time complexity: O(N), where `N` is the length of `s`.
- Space complexity: O(m + n), where `m` is the number of unique characters in `t` and `n` is the number of unique characters in `s` (or limited by the alphabet size).

## 239. Sliding Window Maximum

**Description**:
Given an array `nums` and an integer `k`, you need to find the maximum value in every sliding window of size `k` in the array.

**Example**:
```plaintext
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Solution**:
This problem is efficiently solved using a deque (double-ended queue). The deque is used to store the indices of elements in the array. The core idea is to maintain the deque in such a way that:
1. The indices in the deque are in decreasing order of the values in `nums`.
2. The element at the front of the deque is always the largest element in the current window.

The algorithm processes each element of the array in linear time (`O(n)`), ensuring that each element is added and removed from the deque only once. This approach is significantly faster than a brute-force approach, which would involve recalculating the maximum for each window from scratch.

- The `deque` stores the indices of the elements, not the elements themselves. This allows easy comparison and maintenance of the sliding window.
- For each new element, the algorithm removes elements from the deque that are smaller than the new element, as they are no longer useful.
- If the index at the front of the deque is out of the current window (i.e., its index is less than `left`), it is removed from the deque.
- After the first `k` elements are processed, the algorithm starts appending the maximum value of each window (which is at the front of the deque) to the result list.

This solution is optimal for the problem's constraints and ensures that the sliding window maximum is found in linear time.

**Notes**:
- Time complexity: O(n), where `n` is the length of the array `nums`.
- Space complexity: O(k), due to the maximum size of the deque being equal to the window size `k`.

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