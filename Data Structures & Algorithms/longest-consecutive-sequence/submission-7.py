class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        ans = 1
        cnt = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1

            ans = max(ans, cnt)
        return ans