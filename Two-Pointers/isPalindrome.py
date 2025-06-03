string = "madaM"

def is_palindrome(string: str)-> bool:
    string = string.lower()
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print(is_palindrome(string))