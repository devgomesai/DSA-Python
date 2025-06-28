# arr = [3,2,7,5,9,6,2]
# k = 6
# print(arr[:k]) # [3, 2, 7, 5, 9, 6]
# print(arr[k:]) # [2]

from typing import List
def two_sum(nums:List[int], target:int):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[num] = i