def main():
    name=input("what is your name? ")
    print(hello(name))

def hello(to="world"):      #to is default value
    return f"hello, {to}"

if __name__=='__main__':
    main()