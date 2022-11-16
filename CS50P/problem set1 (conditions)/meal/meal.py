def main():
    time=input("what time is it? ")
    time=convert(time)
    if time >=7 and time <=8:
     print("breakfast time")
    if time >=12 and time <=13:
        print("Lunch time")
    if time >=18 and time <=19:
        print("dinner time")
def convert(time):
    hours,minutes=time.split(":")
    return float(hours)+float(minutes)/60
if __name__ == "__main__":
    main()