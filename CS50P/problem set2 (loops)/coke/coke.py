Coins=[5,10,25]
total=0
coin=int
while total<50:
        print(f"Amount Due:{50-total}")
        coin=int(input("Insert Coin: "))
        if coin in Coins:
            total=total+coin

if total==50:
    print ("Change Owed: 0")
elif total>50:
    print(f"Change Owed: {total-50}")