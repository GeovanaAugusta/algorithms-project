def find_duplicate(nums):

    nums.sort()
    
    if len(nums) <= 1 or any(isinstance(x, str) for x in nums) is True:
        return False

    if any(i < 0 for i in nums):
        return False

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False