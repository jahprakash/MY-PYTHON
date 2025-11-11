# skip multiples of 3 
for number in range(1, 51):
    if number % 3 == 0:
        continue
    print(number)
