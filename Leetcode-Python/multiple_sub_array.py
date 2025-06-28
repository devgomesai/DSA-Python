def get_multiple_subarray(nums, target):
    # Sliding Window Problem
    result = []
    sum = 0
    j = 0
    for i in range(len(nums)):
        sum += nums[i]
        while sum > target and j <= i:
            sum -= nums[j]
            j += 1
        if sum == target:
            result.append(nums[j:i+1])
    return result

nums = [1, 2, 1, 3, 1, 1, 1, 3, 1, 2, 2, 8, 9]
target = 10
print(get_multiple_subarray(nums=nums, target=target))

