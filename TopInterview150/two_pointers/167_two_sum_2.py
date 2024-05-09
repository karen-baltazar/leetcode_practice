class Solution(object):
    def twoSum(self, numbers, target):
        # Hint: Incrementally increase/decrease one pointer while comparing with the other
        left = 0
        right = len(numbers) - 1

        # Continue searching until the two pointers meet
        while left < right:
            # Calculate the sum of the numbers at the current positions
            curr_sum = numbers[left] + numbers[right]

            # If the sum equals the target, return the indices of the two numbers
            if curr_sum == target:
                return [left + 1, right + 1]
            
            # If the sum is greater than the target, move the right pointer to the left
            elif curr_sum > target:
                right -= 1
            
            # If the sum is less than the target, move the left pointer to the right
            else:
                left += 1

        # If no such pair is found, return an empty list
        return []
