def main():
    name=getname()
    house=gethouse()
    print(f"{name} is from {house}")

def getname():
    return input("name: ")

def gethouse():
    return input("house: ")

if __name__=="__main__":
    main()

#return multiple values:

def main():
    name,house=getstudent()
    print(f"{name} is from {house}")

def getstudent():
    name=input("name: ")
    house=input("house: ")
    return name,house

if __name__=="__main__":
    main()


#using tuples:

def main():
    student=getstudent()
    print(f"{student[0]} is from {student[1]}")

def getstudent():
    name=input("name: ")
    house=input("house: ")
    return (name,house)

if __name__=="__main__":
    main()

#using dic:

def main():
    student=getstudent()
    print(f"{student['name']} is from {student['house']}")  #use single quotes for keys

def getstudent():
    student={}
    student["name"]=input("name: ")
    student["house"]=input("house: ")
    return student

if __name__=="__main__":
    main()


#another approach:

def main():
    student=getstudent()
    print(f"{student['name']} is from {student['house']}")  #use single quotes for keys

def getstudent():
    name=input("name: ")
    house=input("house: ")
    return {"name":name,"house":house}

if __name__=="__main__":
    main()


#using class:

class Student:        #the student class is empty but it still exists
    ...
def main():
    student=getstudent()
    print(f"{student.name} is from {student.house}")

def getstudent():
    student=Student
    student.name=input("name: ")                    #name,house are attributes for Student class
    student.house=input("house: ")
    return student

if __name__=="__main__":
    main()

#correctly writing the class

class Student:
    def __init__(self,name,house=None):               #if we want to make the attribute optional
        if not name:                                  #checks if  the name is empty
            raise ValueError("Missing name")
        if house not in["Gryffindor","Slytherin","RavenClaw","HufflePuff"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house

def main():
    student=getstudent()
    print(f"{student.name} is from {student.house}")

def getstudent():
    name=input("name: ")
    house=input("house: ")
    return Student(name,house)

if __name__=="__main__":
    main()

# adding print and a method:

class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in["Gryffindor","Slytherin","RavenClaw","HufflePuff"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
        self.patronus=patronus
    def __str__ (self):
        return f"{self.name} is from {self.house} and his patronus is an {self.patronus}"

    def charm(self):
        match self.patronus:
            case "stag":
                return"🐎"
            case "otter":
                return"🦦"
            case "dog":
                return"🐶"
            case _:
                return"🔮"

def main():
    student=getstudent()
    print(student)
    print(student.charm())

def getstudent():
    name=input("name: ")
    house=input("house: ")
    patronus=input("patronus: ")
    return Student(name,house,patronus)

if __name__=="__main__":
    main()

#building more defensively:

class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
    def __str__ (self):                                  #allows the use of print
        return f"{self.name} is from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

#this is a defensive code to prevent the change of housevalue using dot nutation

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in["Gryffindor","Slytherin","RavenClaw","HufflePuff"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student=getstudent()
    # student.house="davidson"                   we can change the house value after the initial declartion using dot nutation
    student._house="davidson"
    print(student)

def getstudent():
    name=input("name: ")
    house=input("house: ")
    return Student(name,house)

if __name__=="__main__":
    main()

#using class method

class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
    def __str__ (self):                                  #allows the use of print
        return f"{self.name} is from {self.house}"

    @classmethod  #doesn't force me to create student object first
    def get (cls):
        name=input("name:")
        house=input("house:")
        return cls(name,house)

def main():
    student=Student.get()
    print(student)


if __name__=="__main__":
    main()