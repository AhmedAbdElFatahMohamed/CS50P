LT=["a","i","e","o","u","O"]
text=input("input:")
for letter in text:
    if letter not in LT:
        print(letter,end="")