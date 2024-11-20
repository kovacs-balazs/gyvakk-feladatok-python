inputNumber = int(input("Szám > "))
for i in range(1, 11):
    for j in range(1, 11):
        number = i * j
        if number < 10:
            print(" ", number, end=" ")
        elif number > 9 and number < 100:
            print("", number, end=" ")
        else:
            print(number, end=" ")
    print()

print(" ")
for i in range(1, 11):
    for j in range(1, 11):
        number = i * j * inputNumber
        print(number, end=" ")
    print()