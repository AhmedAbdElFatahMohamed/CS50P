#Trick:using nested loops to specifiy where we want to exit(line 13) ,using a variable with function to get random integares (line 9)
#Bugs: wrong count doesn't reset after successful answer,raises error win answering with a char
import random

def main():
    C_count=0
    W_count=1
    L_count=0
    Num=get_level()
    while C_count<10:
        x=generate_integare(Num)
        y=generate_integare(Num)
        while True:
            answer=int(input(f"{x} + {y} = "))
            if answer ==x+y:
                C_count=C_count+1
                break
            elif W_count==3:
                print(f" {x} + {y} = ",x+y)
                W_count=1
                L_count=L_count+1
                C_count=C_count+1
                break
            elif answer != x+y:
                print("EEE")
                W_count=W_count+1
                continue


    print(f"Score:{C_count-L_count}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level not in range (1,4):
                continue
            else:
                break
        except:
            continue
    return level

def generate_integare(level):
    while level in range (1,4):
        try:
            if level ==1:
                x=random.randint(0,9)
                return x
            elif level==2:
                x=random.randint(10,99)
                return x
            elif level==3:
                x=random.randint(100,999)
                return x
        except ValueError:
            break


if __name__ == "__main__":
    main()
