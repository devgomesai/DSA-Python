num1 = 11

num2 = num1

print('Before num2 value is updated',end="\n")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to = ", id(num1))
print("num2 points to =  ", id(num2))
print("\n")
num2 = 22
print('After num2 value is updated', end="\n")
print("num1= ", num1)
print("num2= ", num2)

print("\nnum1 points to = ", id(num1))
print("num2 points to =  ", id(num2))
