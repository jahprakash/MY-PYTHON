# sum until negative number
total_sum = 0
number = 0

while number >= 0:
    number = int(input("Enter a number: "))
    if number >= 0:
        total_sum += number

print("The sum of the numbers is:", total_sum)
