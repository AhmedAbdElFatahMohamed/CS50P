#here we are passing the value of our name as argument when we run the code

#handling wrong user input using try,catch:

import sys
try:
    print("Hello, my name is",sys.argv[1])
except IndexError:
    print("Too few Arguments")

#handling wrong user input using conditions:

import sys
if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("Hello, my name is",sys.argv[1])

#handling wrong user input using sys.exit:

import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")       #it will show the msg and exit immediately without raising name error
elif len(sys.argv)>2:
    sys.exit("Too many arguments")
print("Hello, my name is",sys.argv[1])

#Printing all names in arguments:

import sys
if len(sys.argv)<2:
    print("Too few arguments")

for name in sys.argv[1:]:              #specify the start and end of our argument that we want to slice
    print("Hello, my name is",name)
