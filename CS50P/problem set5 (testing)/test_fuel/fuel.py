def main():
        fuel=input("Fraction: ")
        result=convert(fuel)
        print(gauge(result))

def convert(fraction):
        x=int(fraction.split("/")[0])
        y=int(fraction.split("/")[1])
        return round(x/y*100)

def gauge(percentage):
    if percentage ==99 or percentage ==100 :
        return "F"
    elif percentage <=1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()