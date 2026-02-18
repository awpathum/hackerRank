def numberOfSubarrays(nums, k):
    left = 0
    odd = 0
    res = 0
    count = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            odd += 1
            count = 0

        while odd == k:
            count += 1
            if nums[left] % 2 == 1:
                odd -= 1
            left += 1

        res += count

    return res


nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums, k))  # 2
