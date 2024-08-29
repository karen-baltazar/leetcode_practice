# Problems
| Problem Number | Problem Name               | Explanation                                             | Code                                                  |
|----------------|----------------------------|---------------------------------------------------------|-------------------------------------------------------|
| 242            | [Valid Anagram](#242-valid-anagram) | [Explanation](#242-valid-anagram)                         | [Python Code](./242_valid_anagram.py)                 |
| 217            | [Contains Duplicate](#217-contains-duplicate) | [Explanation](#217-contains-duplicate)                  | [Python Code](./217_contains_duplicate.py)            |
| 1              | [Two Sum](#1-two-sum) | [Explanation](#1-two-sum)                            | [Python Code](./001_two_sum.py)     |

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