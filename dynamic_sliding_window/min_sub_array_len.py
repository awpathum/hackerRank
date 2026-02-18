class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # r = 0
        l = 0
        t = 0
        min_len = float('inf')
        # print(min_len)

        for r in range(len(nums)):
            t = t + nums[r]
            while t >= target:
                min_len = min(min_len,r-l+1)
                t = t - nums[l]
                l = l + 1

        return 0 if min_len == float('inf') else min_len