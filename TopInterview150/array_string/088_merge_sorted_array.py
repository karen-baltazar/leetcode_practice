class Solution(object):

    def merge(self, nums1, m, nums2, n):
        # Hint: How to I get the highest number?
        # Note: Do not return anything, modify nums1 in-place instead.
        i = m + n - 1
        m -= 1
        n -= 1

        while n >= 0:
            if nums2[n] > nums1[m] or m < 0:
                nums1[i] = nums2[n]
                i -= 1
                n -= 1
            else:
                nums1[i] = nums1[m]
                i -= 1
                m -= 1
