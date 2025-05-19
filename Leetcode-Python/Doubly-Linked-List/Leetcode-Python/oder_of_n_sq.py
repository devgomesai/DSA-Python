def print_items(n):
    for i in range(n): # n times
        for j in range(n):  # n times 
            print(i, j)

print_items(10) # n * n =  so Complexity = O( n^2)