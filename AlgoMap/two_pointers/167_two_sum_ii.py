class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            diff = numbers[left] + numbers[right] 
            if diff == target:
                return [left + 1, right + 1]
            elif diff > target:
                right -= 1
            else:
                left += 1
