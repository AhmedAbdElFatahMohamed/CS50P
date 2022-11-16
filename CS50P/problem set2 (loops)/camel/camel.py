Text=input("camelCase: ")
print("snakecase: ",end='')
for letter in Text :
    if letter.isupper():
        letter=letter.lower()
        letter="_"+letter
    print(letter,end="")