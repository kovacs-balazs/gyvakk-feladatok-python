import re
pattern = re.compile("[a-zA-Z]")
print(', '.join(sorted([s for s in list(input("Szöveg > ")) if pattern.match(s)])))