def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_to_index:
            return [num_to_index[diff], i]
        num_to_index[num] = i
    return None
