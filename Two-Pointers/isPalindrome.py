string = "madaM"


def is_palindrome(string: str)-> bool:
    string = string.lower()
    length = len(string)
    p1, p2 = 0, length - 1
    for i in range(length):
        if string[p1] == string[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True

print(is_palindrome(string))