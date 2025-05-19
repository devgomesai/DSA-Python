def print_items(n):
    for i in range(n): # n times
        print(i)
    for j in range(n): # n times
        print(j)
print_items(10) # n + n = 2n so Complexity = O(n)