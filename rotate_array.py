class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_nums = list(range(k))
        # print(new_nums)
        for i in range(0, k):
            new_index = (n - 1 - i + k) % n
            print(f" {nums[n-1-i]}:{new_index}")
            new_nums[new_index] = nums[n - 1 - i]

            print(new_nums)
        nums = new_nums + nums[0:k+1]
        print(nums)
        
