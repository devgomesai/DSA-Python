list1 = [1,3,5]
list2 = [2,3,7]


def items_in_common(list1, list2):
    # For set the python convert it to list to get the index value
    list_set = list(set(list1)) # [1,3,5]
    print(list_set)
    for item in list2:
        if item in list_set:
            return True, list_set.index(item)
    return False
    

# def markfunc(list1, list2):
#     new_list = list1 + list2
#     print(new_list)
#     data = set(new_list)
#     print(data) 
#     if len(data) != len(new_list):
#         return True
#     else:
#         return False
    
print(items_in_common(list1, list2))

