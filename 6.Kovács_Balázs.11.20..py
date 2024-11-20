import random

kockak = int(input("Kockák > "))
oldalak = int(input("Oldalak > "))

osszeg = 0
for kocka in range(kockak):
    rand = random.randint(1, oldalak)
    print(f"{kocka + 1}. kockával {rand}")
    osszeg += rand

print(f"Dobott értékek összege: {osszeg}")