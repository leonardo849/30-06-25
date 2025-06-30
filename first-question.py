count = 0
while count < 5:
    number = int(input("send to me a int:"))
    if number > 0:
        print("positivo")
    elif number == 0:
        print("zero")
    else:
        print("negativo")
    count+=1

