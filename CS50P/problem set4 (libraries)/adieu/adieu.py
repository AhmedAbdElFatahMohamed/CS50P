import inflect
p = inflect.engine()
song=[]
while True:
    try:
        text=input("Name: ")
        song.append(text)
        mylist = p.join((song))
        continue
    except EOFError:
        print("\n")
        print("Adieu, adieu, to",mylist)
        break
