# Problems

| Problem Number | Problem Name                       | Explanation                                      | Code                                      |
|----------------|------------------------------------|--------------------------------------------------|-------------------------------------------|
| 771            | [Jewels and Stones](#771-jewels-and-stones) | [Explanation](#771-jewels-and-stones)  | [Python Code](./771_jewels_and_stones.py) |
| 217            | [Contains Duplicate](#217-contains-duplicate) | [Explanation](#217-contains-duplicate)                  | [Python Code](./217_contains_duplicate.py)            |
| 382            | [Ransom Note](#382-ransom-note)    | [Explanation](#382-ransom-note)  | [Python Code](./382_ransom_note.py)       |
| 242            | [Valid Anagram](#242-valid-anagram) | [Explanation](#242-valid-anagram)                         | [Python Code](./242_valid_anagram.py)                 |
| 1189           | [Maximum Number of Balloons](#1189-max-number-of-balloons)  | [Explanation](#1189-max-number-of-balloons)  | [Python Code](./1189_max_number_of_balloons.py) |
| 36             | [Valid Sudoku](#36-valid-sudoku) | [Explanation](#36-valid-sudoku)                      | [Python Code](./036_valid_sudoku.py)           |
| 1              | [Two Sum](#1-two-sum) | [Explanation](#1-two-sum)                            | [Python Code](./001_two_sum.py)     |
| 49             | [Group Anagrams](#49-group-anagrams) | [Explanation](#49-group-anagrams)            | [Python Code](./049_group_anagrams.py)           |
| 169             | [Group Anagrams](#169-majority-element) | [Explanation](#169-majority-element)            | [Python Code](./169_majority_element.py)           |
| 128            | [Longest Consecutive Sequence](#128-longest-consecutive-sequence) | [Explanation](#128-longest-consecutive-sequence) | [Python Code](./128_longest_consecutive_sequence.py) |

## 771. Jewels and Stones

**Description**:
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

**Example**:
```plaintext
Input:
jewels = "aA"
stones = "aAAbbbb"

Output: 3
```

**Solution**:
The problem can be efficiently solved by converting the `jewels` string into a set, which allows O(1) lookup time for checking whether each stone is a jewel. We then iterate over the `stones` string, counting how many of the stones are also jewels.

[Link to code](771_jewels_and_stones.py)

**Notes**:
- Time complexity: O(n + m), where n is the length of `jewels` and m is the length of `stones`.
- Space complexity: O(n), for the set created from `jewels`.

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

## 382. Ransom Note

**Description**:
Given two strings `ransomNote` and `magazine`, return `True` if `ransomNote` can be constructed using the letters from `magazine`. Each letter in `magazine` can only be used once in `ransomNote`.

**Example**:
```plaintext
Input:
ransomNote = "a"
magazine = "b"

Output: False
```

**Solution**:
The solution involves creating a hashmap (dictionary) to count the frequency of each character in `magazine`. We then check each character in `ransomNote` against this hashmap, decrementing the count each time a character is used. If at any point a character is not available or runs out, return `False`.

[Link to code](382_ransom_note.py)

**Notes**:
- Time complexity: O(n + m), where n is the length of `ransomNote` and m is the length of `magazine`.
- Space complexity: O(n), for storing the frequency count of characters in `magazine`.

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

## 1189. Maximum Number of Balloons

**Description**:
Given a string `text`, you need to return the maximum number of instances of the word "balloon" that can be formed using the characters in `text`. Each character in `text` can only be used once.

**Example**:
```plaintext
Input: text = "nlaebolko"
Output: 1
```

**Solution**:
The solution involves counting the frequency of the characters 'b', 'a', 'l', 'o', and 'n' in the input text. Since the word "balloon" requires 'l' and 'o' to appear twice, we divide their counts by 2. The result is the minimum number of times we can form the word "balloon" using the characters from the input text.

[Link to code](1189_max_number_of_balloons.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input text.
- Space complexity: O(1), since we're only counting a fixed set of characters.

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

[Link to code](049_group_anagrams.py)

**Notes**:
- Time complexity: O(n * k), where `n` is the number of strings and `k` is the maximum length of a string.
- Space complexity: O(n * k), due to storing the groups and the character counts.

## 169. Majority Element

**Description**:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times.

You may assume that the majority element always exists in the array.

**Example**:
```plaintext
Input: [3,2,3]
Output: 3
```

**Solution**:
To efficiently find the majority element, we can utilize the Boyer-Moore Voting Algorithm. This algorithm allows us to determine the majority element in a single pass through the array while maintaining a count of the current majority element. The key idea is to update the count based on whether the current element is equal to the majority element, and reset the majority element and count if the count reaches 0.

[Link to code](169_majority_element.py)

**Notes**:
- Time complexity: O(n), where n is the size of the array.
- Space complexity: O(1), as the algorithm uses constant extra space.

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