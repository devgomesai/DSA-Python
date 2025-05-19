
''' #DESCRIPTION#:  add the prev/ prefix values to the current value eg:
            arr = [1,3,6,10,15,21,18]
            so arr[1] = 1 + 3 = 4
            arr[2] = 1+3+6= 10.....
            so new arr will be arr =[4,10.....]
'''
def create_prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr

arr = [1,3,6,10,15,21,18]
prefix_um_array = create_prefix_sum(arr=arr)
print(prefix_um_array)