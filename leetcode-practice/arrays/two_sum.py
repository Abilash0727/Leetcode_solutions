def twosums(nums, target):
    seen = {}
    for i in range(len(nums)): # {2 : 0, 7 : 1,}
        current_num = nums[i]
        num_needed = target - current_num
        if num_needed in seen:
            return [seen[num_needed], i]
        seen[current_num] = i
    return []  # [2,11,10,14,5,1,6,9,3]

