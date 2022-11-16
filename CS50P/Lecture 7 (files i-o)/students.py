with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        print(f"{name} is in {house}")

#sorted

students=[]
with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


# dictionay

students=[]
with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student={"name":name,"house":house}
        students.append(student)

def get_name(student):
    return student['name']

for student in sorted(students,key=get_name):                            #passing function as key
    print(f"{student['name']} is in {student['house']}")

#using lambda expressions

students=[]
with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student={"name":name,"house":house}
        students.append(student)

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['house']}")

#using csv

import csv
students=[]
with open("students.csv") as file:
    reader=csv.reader(file)
    for name , home in reader:
        students.append({"name":name,"home":home})

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")

#add headers

import csv
students=[]
with open("students.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name" :row["name"], "home": row["home"]})

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")

# write to csv

import csv
name=input("what is your name?")
home=input("where do you live?")

with open ("students.csv","a") as file:
    writer=csv.writer(file)
    writer.writerow([name,home])

#write with dict:it auto arrange keys and values despite the order

import csv
name=input("what is your name?")
home=input("where do you live?")

with open ("students.csv","a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})