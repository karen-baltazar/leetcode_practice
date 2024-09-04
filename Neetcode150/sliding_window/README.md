# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 76             | [Minimum Window Substring](#76-minimum-window-substring) | [Explanation](#76-minimum-window-substring)          | [Python Code](./076_minimum_window_substring.py) |

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
