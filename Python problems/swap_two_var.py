a = input("Enter first variable: ")
b = input("Enter second variable: ")

print(f"Before swapping: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")

#write a program to swap 2 variable without using temp

a = 5
b = 10

a,b = b, a
print(f"After swapping without using temp: a = {a}, b = {b}")