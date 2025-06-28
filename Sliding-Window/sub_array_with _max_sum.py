import time
import random

# Generate a large array for testing
large_array = [random.randint(1, 100) for _ in range(10000)]
k = 100


# Efficient approach: O(n)
def max_sub_array_sum_best(arr, k):
    n = len(arr)
     
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_start_index = 0

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i + 1
    return arr[max_start_index:max_start_index + k], max_sum

# Measuring time for efficient approach
start_time = time.time()
for _ in range(10):  # Repeat 10 times
    result2 = max_sub_array_sum_best(large_array, k)
end_time = time.time()
print("Efficient result:", result2)
print("Time taken (efficient):", (end_time - start_time) / 10)  # Average time
