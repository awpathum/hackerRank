# start
# find the current minimum
# move it to the left
# increment sorted array index by 1.


# nums = [8,6,7,1,0,4,5,2,9,3]
nums = [10,9,8,7,6,5,4,3,2,1,0,-1]


for j in range (0,len(nums) -1):
    cur_min = nums[j]
    min_index = j
    
    for i in range (j+1, len(nums)):
        if nums[i] < cur_min:
            cur_min = nums[i]
            min_index = i

    # swap
    temp = nums[j]
    nums[j] = cur_min
    nums[min_index] = temp

    print(nums)

print(nums)




