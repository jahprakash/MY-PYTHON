#smallest elements in a list
numbers = [10, 20, 30, 40, 50]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("The smallest element in the list is:", smallest)
