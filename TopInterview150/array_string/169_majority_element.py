class Solution(object):
    def majorityElement(self, nums):
        # Hint: What happens to the count when we encounter different elements? [Boyer-Moore Voting Algorithm]
        count = 0 
        res = 0

        # Iterate through the array.
        for n in nums:
            # If count is 0, update the majority element.
            if count == 0:
                res = n
            
            # Increment or decrement the count based on whether the current element is equal to the majority element.
            count += (1 if n == res else -1)
        
        return res 

