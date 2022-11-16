#return a name list
names=[]
for _ in range (3):
    name=input("wha's your name? ")
    names.append(name)
for name in sorted(names):
    print(f"hello, {name}")

#write to file:

name=input("what's your name? ")
file=open("name.txt","a")
file.write(f"{name}\n")
file.close()

with open("name.txt","a") as file:                                     # this replaces the need to add file.close()
    file.write(f"{name}\n")


# read from file:

with open ("name.txt","r") as file:
  lines=file.readlines()
  for line in lines:                                         #iterate through read lines
     print ("hello,",line.strip())
  for line in file:                                        #iterate through lines in file
        print ("hello,",line.strip())

# print sorted lines from file:

names=[]
with open ("name.txt") as file:                              #no need to add read since the default is read
    for line in file:
        names.append(line.strip())
for name in sorted(names,reverse=True):                                    #add reverse to sorted function
    print(f"hello,{name}")

#more ompact

with open ("name.txt") as file:
    for line in sorted(file):
        print("hello,",line.strip())