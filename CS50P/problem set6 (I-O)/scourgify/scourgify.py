#problems: have to use W instead of A to overwrite
#split row before adding to list line 16

import csv
import sys
students=[]
try:
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    else:
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            for row in reader:
                firstname=row["name"].split(",")[1]
                lastname=row["name"].split(",")[0]
                students.append({"first" :firstname.lstrip(), "last": lastname.lstrip(),"house":row['house']})

        with open (sys.argv[2],"w") as file2:
            writer=csv.DictWriter(file2,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in students:
                writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
except FileNotFoundError:
    sys.exit(f"Couldn't read {sys.argv[2]}")

