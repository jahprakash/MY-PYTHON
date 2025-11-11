#while loop
n=int(input("enter a positive integer"))
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1
print("The sum of the first", n, "positive integers is:", sum_of_numbers)
