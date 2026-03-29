"""#write a program to convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit")




# Alternative method using f-strings
# print(f"{celsius} degree Celsius is equal to {(celsius * 9/5) + 32} degree Fahrenheit")
"""



# write a program to display calendar.
import calendar
year = int(input("Enter year : "))
month = int(input("Enter month :"))
cal = calendar.month(year, month)
print(cal)
