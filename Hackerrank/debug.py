def pairs(k, nums):
    # Write your code here
    empty_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            tot = abs(nums[i] - nums[j])
            if tot == k:
                empty_list.extend([nums[j],nums[i]])
    return empty_list
print(pairs(5,[1,5,3,4,2]))