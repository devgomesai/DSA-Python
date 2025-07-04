def minMaxDifference(num: int) -> int:
    max_value = str(9) # 9
    min_value = str(0) # 0
    
    num_str = str(num) # "11891"
    max_value_nums = int(num_str.replace(min(num_str),max_value)) 
    print(max_value_nums)  # "99899"
    min_value_nums = int(num_str.replace(min(num_str),min_value))
    print(min_value_nums) # 00890

    return max_value_nums - min_value_nums


num = 11891
print(minMaxDifference(num=num))