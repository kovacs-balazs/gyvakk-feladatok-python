numbers = []

while True:
    number = int(input("Szám > "))
    if number == 0:
        break
    numbers.append(number)

paros = [str(num) for num in numbers if num % 2 == 0]
paratlan = [str(num) for num in numbers if num % 2 != 0]

print(f"Páros számok: {', '.join(paros)}")
print(f"Páratlan számok: {', '.join(paratlan)}")