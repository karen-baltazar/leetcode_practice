# Problems
| Problem Number | Problem Name               | Explanation                                             | Code                                                  |
|----------------|----------------------------|---------------------------------------------------------|-------------------------------------------------------|
| 242            | [Valid Anagram](#242-valid-anagram) | [Explanation](#242-valid-anagram)                         | [Python Code](./242_valid_anagram.py)                 |
| 217            | [Contains Duplicate](#217-contains-duplicate) | [Explanation](#217-contains-duplicate)                  | [Python Code](./217_contains_duplicate.py)            |
| 1              | [Two Sum](#1-two-sum) | [Explanation](#1-two-sum)                            | [Python Code](./001_two_sum.py)     |
| 49             | [Group Anagrams](#49-group-anagrams) | [Explanation](#49-group-anagrams)            | [Python Code](./049_group_anagrams.py)           |
| 347            | [Top K Frequent Elements](#347-top-k-frequent-elements) | [Explanation](#347-top-k-frequent-elements) | [Python Code](./347_top_k_frequent_elements.py) |
| 271            | [Encode and Decode Strings](#271-encode-and-decode-strings) | [Explanation](#271-encode-and-decode-strings) | [Python Code](./271_encode_decode_strings.py) |
| 238            | [Product of Array Except Self](#238-product-of-array-except-self) | [Explanation](#238-product-of-array-except-self) | [Python Code](./238_product_of_array_except_self.py) |
| 36             | [Valid Sudoku](#36-valid-sudoku) | [Explanation](#36-valid-sudoku)                      | [Python Code](./036_valid_sudoku.py)           |
| 128            | [Longest Consecutive Sequence](#128-longest-consecutive-sequence) | [Explanation](#128-longest-consecutive-sequence) | [Python Code](./128_longest_consecutive_sequence.py) |

## 217. Contains Duplicate

**Description**:
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

**Example**:
```plaintext
Input: nums = [1,2,3,1]
Output: True
```

**Solution**:
To determine if the array contains duplicates, we can use a set to track the unique elements as we iterate through the array. If we encounter an element that is already in the set, we return `True`. If we finish iterating without finding any duplicates, we return `False`.

[Link to code](217_contains_duplicate.py)

**Notes**:
- **Time complexity**: O(n), where n is the length of the array. Each insertion and lookup in the set is O(1) on average.
- **Space complexity**: O(n), as we store up to n elements in the set.

## 242. Valid Anagram

**Description**:
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise. An anagram is a word or phrase formed by rearranging the letters of another, typically using all the original letters exactly once.

**Example**:
```plaintext
Input: s = "anagram", t = "nagaram"
Output: True
```

**Solution**:
To check if two strings are anagrams, we can compare the frequency of each character in both strings. We first check if the lengths of the strings are equal. If not, they can't be anagrams. We then create two dictionaries to store the frequency of each character in both strings. Finally, we compare the two dictionaries to determine if the strings are anagrams.

[Link to code](242_valid_anagram.py)

**Notes**:
- **Time complexity**: O(n), where n is the length of the strings.
- **Space complexity**: O(n), as we store the frequency of each character in a dictionary.

## 1. Two Sum

**Description**:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. 

**Example**:
```plaintext
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Solution**:
To solve this problem, we use a hash map to store the indices of the numbers we have seen so far. For each number in the list, we compute the difference between the target and the current number. If this difference exists in the hash map, it means we have found the two numbers that add up to the target. Otherwise, we store the current number and its index in the hash map for future reference.

[Link to code](001_two_sum.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the input list `nums`.
- Space complexity: O(n), due to the space used by the hash map to store the indices.

## 49. Group Anagrams

**Description**:
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Example**:
```plaintext
Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
  ["bat"],
  ["nat","tan"],
  ["ate","eat","tea"]
]
```

**Solution**:
To group anagrams, we use a dictionary where each key is a tuple representing the count of each character (from 'a' to 'z') in a word. All anagrams will share the same key, allowing us to group them together efficiently.

**Python Code**:
[Link to code](049_group_anagrams.py)

**Notes**:
- Time complexity: O(n * k), where `n` is the number of strings and `k` is the maximum length of a string.
- Space complexity: O(n * k), due to storing the groups and the character counts.

## 347. Top K Frequent Elements

**Description**:
Given a non-empty array of integers, return the `k` most frequent elements. You may assume that the answer is guaranteed to be unique.

**Example**:
```plaintext
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1, 2]
```

**Solution**:
To solve this problem, we first count the frequency of each element using a dictionary. We then organize these elements into a list of lists, where each index represents the frequency of the elements. Finally, we iterate from the end of this list to gather the top `k` most frequent elements.

**Python Code**:
[Link to code](347_top_k_frequent_elements.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of elements in `nums`.
- Space complexity: O(n), due to the storage of frequency counts and bucket lists.

## 271. Encode and Decode Strings

**Description**:
Design an algorithm to encode and decode a list of strings. The encoding and decoding must be reversible.

**Example**:
```plaintext
Input:
["hello","world"]

Output:
"5#hello5#world"

Decoded Output:
["hello","world"]
```

**Solution**:
To encode the list of strings, concatenate each string's length, a delimiter, and the string itself. For decoding, extract each string length from the encoded string, then retrieve the corresponding string based on its length.

**Python Code**:
[Link to code](271_encode_decode_strings.py)

**Notes**:
- Time complexity: O(n), where `n` is the total number of characters in all strings combined.
- Space complexity: O(n), as we are storing the encoded string.

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

## 36. Valid Sudoku

**Description**:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

**Example**:
```plaintext
Input: 
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

**Solution**:
To validate the Sudoku board, we need to check three conditions:
1. Each row must contain unique digits (excluding '.').
2. Each column must contain unique digits (excluding '.').
3. Each 3x3 sub-box must contain unique digits (excluding '.').

We use sets to track the digits we have seen so far for each row, column, and sub-box. If a duplicate is found, we return false.

[Link to code](036_valid_sudoku.py)

**Notes**:
- Time complexity: O(n^2), where n is the length of the board (9 in this case).
- Space complexity: O(n), due to the use of sets to track seen digits.

## 128. Longest Consecutive Sequence

**Description**:
Find the length of the longest consecutive elements sequence in an unsorted array. The sequence should be consecutive, but not necessarily contiguous.

**Example**:
```plaintext
Input:
nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4], which has length 4.
```

**Solution**:
1. Convert the input list into a set to enable O(1) access time for each element.
2. Iterate through each number and check if it is the start of a sequence (i.e., `n-1` is not in the set).
3. Count the length of the sequence starting from the current number.
4. Update the length of the longest sequence found so far.

[Link to code](128_longest_consecutive_sequence.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the input list.
- Space complexity: O(n) for storing elements in the set.