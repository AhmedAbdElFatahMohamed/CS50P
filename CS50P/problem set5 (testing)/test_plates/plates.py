def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if  not plate.isalnum() or 2<len(plate)>6 or not plate[0:2].isalpha():
        return False
    for i in range(2, len(plate)-1):
        if plate[i-1].isalpha() and plate[i]=="0":
            return False
        elif plate[i].isdigit() and  not plate[i:len(plate)].isdigit():
            return False
        else:
            return True

if __name__ == "__main__":
    main()