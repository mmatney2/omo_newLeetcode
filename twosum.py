def twoSum(nums, t):
    """return index of 2 numbers that add to target"""
    res = []
    hashmap = {}
    # match = t - num
    for i, num in enumerate(nums):
        
        # print(hashmap)
        if (t - nums[i]) in hashmap:
            return [hashmap[t - nums[i]], i] 
        else:
            hashmap[num] = i

            
            # hashmap[num] = i
            # print(hashmap)
        
print(twoSum([3,2,4], 6))