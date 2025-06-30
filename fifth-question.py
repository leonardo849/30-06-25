print("Let's play a game. If you send to me a number that i don't like. I will finish the program")

while True:
    number = int(input("type a number"))
    if number % 2 != 0:
        print("i don't like that number. bye bye")
        break
    