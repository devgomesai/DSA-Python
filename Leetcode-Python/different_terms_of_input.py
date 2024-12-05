def print_items(a,b):
    for a in range(a): # O(a) based on input a can be [0, 1, 2, ..9] or combinations of them
        print(a)
    for b in range(b): # O(b) based on input b can be [0, 1, 2, ..9] or combinations of them
        print(b)

print_items(a=10, b=5) # a + b =  so Complexity = O(a+b) based on input a and input b