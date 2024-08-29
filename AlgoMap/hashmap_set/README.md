# Problems

| Problem Number | Problem Name                       | Explanation                                      | Code                                      |
|----------------|------------------------------------|--------------------------------------------------|-------------------------------------------|
| 771            | [Jewels and Stones](#771-jewels-and-stones) | [Explanation](#771-jewels-and-stones)  | [Python Code](./771_jewels_and_stones.py) |
| 217            | [Contains Duplicate](#217-contains-duplicate) | [Explanation](#217-contains-duplicate)                  | [Python Code](./217_contains_duplicate.py)            |
| 382            | [Ransom Note](#382-ransom-note)    | [Explanation](#382-ransom-note)  | [Python Code](./382_ransom_note.py)       |
| 242            | [Valid Anagram](#242-valid-anagram) | [Explanation](#242-valid-anagram)                         | [Python Code](./242_valid_anagram.py)                 |

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