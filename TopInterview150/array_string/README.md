# Problems

## 88. Merge Sorted Array

**Description**:
Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array. Assume that `nums1` has enough space (size that is equal to `m + n`) to hold additional elements from `nums2`.

**Example**:
```plaintext
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]
```

**Solution**:
To merge two sorted arrays, we can use a two-pointer approach. We initialize two pointers, one for each array, starting from the end of the valid elements in each array. We compare the elements pointed to by such pointers, and fill nums1 from the end with the largest element, updating the pointers accordingly. 

[Link to code](088_merge_sorted_array.py)

**Notes**:
- Time complexity: O(m + n), where m and n are the lengths of nums1 and nums2, respectively.
- Space complexity: O(1), since the merge is done in-place without using extra space.

## 27. Remove Element

**Description**:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

**Example**:
```plaintext
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

**Solution**:
To remove all occurrences of val from the array nums in-place, we can use a two-pointer approach. We initialize two pointers (i and j) at the start and end of the array respectively. While j points to a non-val element, we copy it to the position pointed by i and increment i. If j points to a val element, we only decrement j to move towards the start of the array. After processing all elements, i will represent the count of non-val elements, and we can return it. 

[Link to code](027_remove_element.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array nums.
- Space complexity: O(1), as the removal is done in-place without using extra space.

## 26. Remove Duplicates from Sorted Array

**Description**:
Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and returns the new length.

**Example**:
```plaintext
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

**Solution**:
To remove duplicates from a sorted array nums, we can use a two-pointer approach. We initialize two pointers (i and j) at the start and next positions of the array respectively. While j is within the array bounds, if nums[i] is not equal to nums[j], we increment i and update nums[i] with nums[j]. After processing all elements, i will represent the count of unique elements, and we can return i + 1. 

[Link to code](026_remove_duplicates.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array nums.
- Space complexity: O(1), as the removal is done in-place without using extra space.

## 80. Remove Duplicates from Sorted Array II

**Description**:
Given a sorted array `nums`, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

**Example**:
```plaintext
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
```

**Solution**:
To remove duplicates from a sorted array nums while keeping at most two duplicates of each element, we can utilize two pointers. We initialize two pointers, l and r, to track the position of the elements in the array. We also use a counter count to count the number of consecutive duplicates. We iterate over the array using the pointer r, counting consecutive duplicates. If we encounter a new element, we copy it to the position pointed by l, updating l accordingly. We repeat this process, copying at most two duplicates of each element, until we have processed all elements in the array.

[Link to code](080_remove_duplicates_2.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array nums.
- Space complexity: O(1), as the removal is done in-place without using extra space.

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

## 189. Rotate Array

**Description**:
Given an array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example**:
```plaintext
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Solution**:
To rotate the array in-place, we adjust the value of k to ensure it's within the range of the list length. Then, we rotate the list by reversing sublists: first, we reverse the entire list, then we reverse the first k elements, and finally, we reverse the remaining elements.

[Link to code](189_rotate_array.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array.
- Space complexity: O(1), as the rotation is done in-place without using extra space.

## 121. Best Time to Buy and Sell Stock

**Description**:
Given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day, find the maximum profit you can achieve from this stock by buying on one day and selling on another day.

**Example**:
```plaintext
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
```

**Solution**:
To maximize profit, we want to find the maximum difference between two prices (buying price and selling price). We iterate through the prices array and keep track of the minimum price encountered so far. For each price, we calculate the profit if we sell at that price and update the maximum profit if necessary.

[Link to code](121_buy_sell_stock.py)

**Notes**:
- Time complexity: O(n), where n is the length of the prices array.
- Space complexity: O(1), as the algorithm uses only a constant amount of extra space.
