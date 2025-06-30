numbers = []

while len(numbers) < 5:
    number = int(input("type a number"))
    numbers.append(number)
    

sum = 0
for number in numbers:
    
    if number % 2 == 0:
        sum += number

print("result:", sum)