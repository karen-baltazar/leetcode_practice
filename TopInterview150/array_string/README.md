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

**Solution Explanation**:
To merge two sorted arrays, we can use a two-pointer approach. We initialize two pointers, one for each array, starting from the end of the valid elements in each array. We compare the elements pointed to by such pointers, and fill nums1 from the end with the largest element, updating the pointers accordingly.

**Notes**:
- This solution uses a two-pointer approach to merge two sorted arrays in-place.
- Time complexity: O(m + n), where m and n are the lengths of nums1 and nums2, respectively.
- Space complexity: O(1), since the merge is done in-place without using extra space.
