def dup(nums):
#hashset
    charSet = set()
    for num in nums:
        if num in charSet:
            return True
        charSet.add(num)
    return False
print(dup([1,2,3, 1]))
