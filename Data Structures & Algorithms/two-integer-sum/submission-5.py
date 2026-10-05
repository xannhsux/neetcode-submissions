class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in ans.keys():
                return [ans[comp], i]

            ans[n] = i
                        