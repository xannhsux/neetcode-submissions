class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #length of nums array
        n = len(nums)
        #initialize result array
        res = [1] * n

        #prefix
        #at position 0 default prefix = 1
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        
        #postfix 
        #doing the calculation backwards
        #at n - 1 postfix defult 1
        postfix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res

