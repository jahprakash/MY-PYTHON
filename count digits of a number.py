# count digits of a number
n = 12345
count = 0

while n != 0:
  n =n // 10
  count += 1
print("the number of digits is:", count)
