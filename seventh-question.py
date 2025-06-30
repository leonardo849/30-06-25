numbers = []
sum = 0
while len(numbers) < 5:
    number = int(input("type a number"))
    if number % 2 == 0:
        sum += number
    numbers.append(number)
    


print("result:", sum)