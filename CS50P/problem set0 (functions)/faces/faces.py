def convert (text):
    if ":)" in text or ":(":
     return text.replace(":)","\U0001F642").replace(":(","\U0001F641")

def main():
    text=input("")
    print (convert(text))


main()


