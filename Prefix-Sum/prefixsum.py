
''' #DESCRIPTION#:  add the prev/ prefix values to the current value eg:
            arr = [1,3,6,10,15,21,18]
            so arr[1] = 1 + 3 = 4
            arr[2] = 1+3+6= 10.....
            so new arr will be arr =[4,10.....]
'''
def create_prefix_sum(arr):
    """
    The function `create_prefix_sum` generates a prefix sum array from a given input array.
    
    :param arr: The `create_prefix_sum` function takes a list `arr` as input and calculates the prefix
    sum of the elements in the list. It modifies the list in place by replacing each element with the
    sum of all elements up to that index
    :return: The function `create_prefix_sum` returns an array where each element is the sum of all
    elements before it in the input array `arr`.
    """
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr

arr = [1,3,6,10,15,21,18]
prefix_um_array = create_prefix_sum(arr=arr)
print(prefix_um_array)