while True :
    try:
        fuel=input("Fraction: ")
        x=int(fuel.split("/")[0])
        y=int(fuel.split("/")[1])
        if round(x/y*100)==99 or round(x/y*100)==100 :
            print("F")
            break
        elif round(x/y*100)<=1:
            print("E")
            break
        elif round(x/y*100)>100:
            continue
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        print(f"{round(x/y*100)}%")
        break