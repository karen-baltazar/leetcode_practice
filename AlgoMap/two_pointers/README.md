# Problems

| Problem Number | Problem Name                             | Explanation                                    | Code                                      |
|----------------|------------------------------------------|------------------------------------------------|-------------------------------------------|
| 977            | [Squares of a Sorted Array](#977-squares-of-a-sorted-array) | [Explanation](#977-squares-of-a-sorted-array) | [Python Code](./977_squares_of_a_sorted_array.py) |
| 344            | [Reverse String](#344-reverse-string)    | [Explanation](#344-reverse-string)            | [Python Code](./344_reverse_string.py)    |
| 167            | [Two Sum II - Input Array Is Sorted](#167-two-sum-ii-input-array-is-sorted) | [Explanation](#167-two-sum-ii-input-array-is-sorted) | [Python Code](./167_two_sum_ii.py) |
| 125            | [Valid Palindrome](#125-valid-palindrome)    | [Explanation](#125-valid-palindrome)          | [Python Code](./125_valid_palindrome.py)  |
| 15             | [3Sum](#15-3sum)                               | [Explanation](#15-3sum)                       | [Python Code](./015_3sum.py)               |
| 11             | [Container with Most Water](#11-container-with-most-water) | [Explanation](#11-container-with-most-water) | [Python Code](./011_container_with_most_water.py) |
| 42             | [Trapping Rain Water](#42-trapping-rain-water) | [Explanation](#42-trapping-rain-water)       | [Python Code](./042_trapping_rain_water.py)      |

## 977. Squares of a Sorted Array

**Description**:
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Example**:
```plaintext
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

**Solution**:
The solution involves using two pointers, one starting at the beginning (`left`) and the other at the end (`right`) of the array. We compare the absolute values of the elements at these pointers, square the larger one, and move the pointer inward. We store the results in a new list in reverse order to ensure the final array is sorted in non-decreasing order.

[Link to code](977_squares_of_a_sorted_array.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input array.
- Space complexity: O(n), for storing the result.

## 344. Reverse String

**Description**:  
Given a list of characters `s`, reverse the list in-place.

**Example**:
```plaintext
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Solution**:  
The solution involves using two pointers, `start` and `end`, which initially point to the beginning and end of the list, respectively. We swap the characters at these pointers and then move the pointers towards each other until they meet or cross. This process effectively reverses the list in-place.

[Link to code](344_reverse_string.py)

**Notes**:
- Time complexity: O(n), where n is the length of the list.
- Space complexity: O(1), as the reversal is done in-place.

## 167. Two Sum II - Input Array Is Sorted

**Description**:  
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers in ascending order.

**Example**:
```plaintext
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

**Solution**:  
The solution uses a two-pointer approach. Initialize one pointer at the beginning (`left`) and the other at the end (`right`) of the array. Calculate the sum of the elements at these pointers. If the sum is equal to the target, return the 1-based indices. If the sum is greater than the target, move the right pointer leftward to decrease the sum. If the sum is less than the target, move the left pointer rightward to increase the sum.

[Link to code](167_two_sum_ii.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array.
- Space complexity: O(1), as no additional space is required.

## 125. Valid Palindrome

**Description**:  
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring case.

**Example**:
```plaintext
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

**Solution**:  
The solution uses a two-pointer approach. Initialize one pointer at the start of the string (`start`) and the other at the end (`end`). Skip non-alphanumeric characters and compare the characters at the two pointers. If they do not match, return `False`. If all characters match, return `True`.

[Link to code](125_valid_palindrome.py)

**Notes**:
- Time complexity: O(n), where n is the length of the string.
- Space complexity: O(1), as no additional space is required.

## 15. 3Sum

**Description**:
Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. 

**Example**:
```plaintext
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Solution**:
The solution involves using a combination of sorting and the two-pointer technique. The array is first sorted to enable the two-pointer approach. For each element in the array (considered as the first element of the triplet), two pointers are used to find two other elements that sum to the negative of the fixed element. To avoid duplicates, we skip over duplicate values during the iteration.

**Algorithm**:
1. **Sort** the array to apply the two-pointer technique.
2. **Iterate** over the array with a fixed element.
3. **Use Two Pointers** to find pairs that sum to the negative value of the fixed element.
4. **Avoid Duplicates** by skipping over duplicate values during the search.

[Link to code](./015_3sum.py)

**Notes**:
- Time complexity: O(n^2), where n is the length of the input array. This is due to the nested loop structure where we iterate through the array and use two pointers.
- Space complexity: O(n) for storing the result triplets.

## 11. Container with Most Water

**Description**:
Given an integer array `height` where each element represents the height of a vertical line on a coordinate plane, return the maximum area of water that can be contained between two lines. The width between the lines is the distance between their indices.

**Example**:
```plaintext
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

**Solution**:
The solution uses a two-pointer approach to find the maximum area. The pointers start at the beginning and end of the list and move inward, calculating the area at each step. The pointer pointing to the shorter line is moved to potentially find a taller line that could yield a larger area.

[Link to code](./011_container_with_most_water.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the list. Each element is processed once.
- Space complexity: O(1), as no additional space is used other than a few variables.

## 42. Trapping Rain Water

**Description**:
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example**:
```plaintext
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Solution**:
The main solution involves using auxiliary arrays to keep track of the maximum height to the left and right of each element. We then calculate the trapped water above each element by finding the difference between the minimum of the maximum heights and the height of the current element.

An alternative solution uses a two-pointer approach, which saves space but is slightly more complex. This method involves moving two pointers inward from both ends of the list, adjusting the maximum heights and calculating trapped water on the go.

[Link to code](042_trapping_rain_water.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input list.
- Space complexity: O(n) for the main solution (O(1) for the alternative solution).