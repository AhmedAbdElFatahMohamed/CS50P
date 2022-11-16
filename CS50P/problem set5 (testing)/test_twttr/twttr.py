LT=["a","i","e","o","u","O","A","E","I","U"]
def main():
    text=input("input:")
    print(shorten(text))

def shorten(text):
    for character in LT:
        text = text.replace(character, "")
    return text


if __name__ == "__main__":
    main()