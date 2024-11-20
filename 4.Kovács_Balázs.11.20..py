szoveg = input("Szöveg > ").lower()
letters = set([s for s in list(szoveg) if s.strip() != ""])

for letter in letters:
    print(f"{letter} előfordulása: {szoveg.count(letter)}")

