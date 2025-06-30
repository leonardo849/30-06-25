grades = 0
count = 0

while True:
    grade = int(input("send to me your grade:"))
    if grade == -1:
        print("average:", grades/count)
        break
    elif grade >= 0 and grade <= 10:
        print("grade:", grade)
        grades += grade
        count += 1
        print("grades:", grades, "count:", count)
    else:
        print("what fuck are you doingbro?")

