def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        else:
            start +=1 
            end -= 1
        return True
    
bool_val = is_palindrome('abcdcba')
print(bool_val)