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

## 167. Two Sum II - Input Array Is Sorted

**Description**:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

**Example**:
```plaintext
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Solution**:
This solution finds two numbers in a sorted array that sum up to a target using a two-pointer approach. It leverages the fact that the array is sorted to optimize the comparison, incrementally adjusting pointers to converge on the target sum.

[Link to code](167_two_sum_2.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input array.
- Space complexity: O(1), as the solution uses only constant extra space.

## 11. Container With Most Water

**Description**:
Given `n` non-negative integers `height` representing the heights of the vertical lines on a 2D plane, calculate the maximum area of water that can be trapped between the vertical lines.

**Example**:
```plaintext
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is obtained by choosing the minimum of the heights of the two vertical lines (8 and 7) and multiplying the difference in their indices (8-1 = 7).
```

**Solution**:
This solution employs a two-pointer approach to find the maximum area of water that can be trapped between vertical lines. Initially, we place one pointer at the start of the array and another at the end. We then calculate the area between these pointers and move the pointer with the smaller height towards the center. By doing so, we ensure that we explore areas with the potential for higher water containment, maximizing the trapped water area as the pointers converge.

[Link to code](011_water_container.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the input array.
- Space complexity: O(1), as the solution uses only constant extra space.
