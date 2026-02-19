nums = [10,9,8,7,6,5,4,3,2,1,0,-1]

for j in range(1,len(nums)):
    i = j
    while i != 0:
        if nums[i] < nums[i-1]:
            # pass
            #swap
            temp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = temp
            i = i - 1
        else:
            break
    
    # print(nums)

print(nums)