from tabulate import tabulate
import csv
import sys

pizza=[]
try:
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        with open(sys.argv[1]) as file:
            reader=csv.reader(file)
            for row in reader:
                pizza.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizza[1:],headers=pizza[0],tablefmt="grid"))





