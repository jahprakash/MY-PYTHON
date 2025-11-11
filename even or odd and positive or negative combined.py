# even/odd and positive/negative combined

number = int(input("Enter a number: "))
#check if the number is positive,negative,or zero
if number > 0:
    # Check if the positive number is even or odd
    if number % 2 == 0:
        print("The number {number} is Even and Positive.")
    else:
        print("The number {number} is Odd and Positive.")
elif number < 0:
    # Check if the negative number is even or odd
    if number % 2 == 0:
        print("The number {number} is Even and Negative.")
    else:
        print("The number {number} is Odd and Negative.")
else:
    print("The number is zero, which is neither positive nor negative.")
