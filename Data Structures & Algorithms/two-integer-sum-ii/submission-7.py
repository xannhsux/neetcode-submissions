class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            curNum = numbers[l] + numbers[r]
            if curNum > target:
                r -= 1
            elif curNum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
