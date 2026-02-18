class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        initial_array = nums[0:k]
        max_sum = sum(initial_array)
        
        if len(nums) == 1 or len(nums) == k:
            return max_sum/k

        sum1 = max_sum
        for i in range(1, len(nums) - k + 1):
            sum1 =  sum1 - nums[i-1] + nums[i+k-1]
            max_sum = max(max_sum, sum1)
        
        return max_sum/k