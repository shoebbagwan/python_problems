numbers = [10, 25, 8, 45, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
