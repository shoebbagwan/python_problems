"""#python program for add and divide 
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
sum_result = num1 + num2
# print(f"sum:{num1} + {num2} = {sum_result}")
print(sum_result)"""

#division of numbers 
num3 = float(input("Enter the first number : "))
num4 = float(input("Enter the second number : "))
if num4 == 0:
    print("Error: Division by zero is not allowed")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")    