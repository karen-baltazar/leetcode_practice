class Solution(object):
    def majorityElement(self, nums):

        # Initialize an empty dictionary.
        dict = {}

        # Iterate over each element in the nums list.
        for elem in nums:
            # If the element is not in the dictionary, add it with a count of 1.
            if elem not in dict:
                dict[elem] = 1
            # If the element is already in the dictionary, increment its count.
            else:
                dict[elem] += 1

        v = list(dict.values())  # List of occurrence counts.
        k = list(dict.keys())    # List of unique elements.

        # Return the element with the maximum occurrence count.
        return k[v.index(max(v))]
