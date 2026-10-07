class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [ [] for i in range(len(nums) + 1)]

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        #key value pair
        for num,cnt in counter.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res

