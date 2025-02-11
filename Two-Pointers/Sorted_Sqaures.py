list1 = [1,3,4,2,0]

### Sorted Squares
def sorted_square(nums) -> list:
    nums.sort()
    n = len(nums)
    res = [0] * n
    L, R = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[L]) > abs(nums[R]):  
            res[i] = nums[L] ** 2
            L += 1
        else:
            res[i] = nums[R] ** 2
            R -= 1
    return res

print(list1)
print(sorted_square(list1))
    