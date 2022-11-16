total=0
items={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:
    try:
        item=input("Item: ").title()
        if item in items:
            total=total+items[item]
            print("Total:$%.2f" % round(total, 2))
            continue
    except EOFError:
        print("\n")
        break
    except KeyError:
        continue