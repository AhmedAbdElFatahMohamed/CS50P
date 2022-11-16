months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date:")
        if "/" in date and int(date.split("/")[0]) <=12 and int(date.split("/")[1]) <= 31:
            x=int(date.split("/")[0])
            y=int(date.split("/")[1])
            z=int(date.split("/")[2])
            print(f"{z:02}",end="-")
            print(f"{x:02}",end="-")
            print(f"{y:02}")
            break
        elif " " in date and months.index(date.split(" ")[0])+1 <=12 and int(date.split(" ")[1].split(",")[0]) <= 31 and "," in date:
            x=months.index(date.split(" ")[0])+1
            y=int(date.split(" ")[1].split(",")[0])
            z=int(date.split(" ")[2])
            print(f"{z:02}",end="-")
            print(f"{x:02}",end="-")
            print(f"{y:02}")
            break
    except:
        continue