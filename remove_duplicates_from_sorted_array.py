class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        # unique_list = []
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                # nums[k] = nums[i+1]
                # k = i + 1
                pass
            else:
                nums[k] = nums[i+1]
                k = k + 1
            
        # print(k-1)
        # print(nums[0:k])

        return k