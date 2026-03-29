# write a python program to solve quadratic equations
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))   
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c
# check if discriminant is positive, negative or zero

if discriminant > 0:
    root1 = (-b+ math.sqrt(discriminant)) /(2*a)
    root2 = (-b - math.sqrt(discriminant)) /(2*a)
    print(f"root 1: {root1}")
    print(f"root 2: {root2}")
    
elif discriminant == 0:
    root  = -b / (2*a) 
    print(f"root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"root 1: {real_part} + {imaginary_part}i")
    print(f"root 2: {real_part} - {imaginary_part}i")
           