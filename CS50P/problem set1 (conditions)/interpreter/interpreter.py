express=input("Expression: ")
x=express.split(" ")[0]
y=express.split(" ")[1]
z=express.split(" ")[2]
x=float(x)
z=float(z)
if y=="+":
    print(round(x+z,2))
elif y=="-":
    print(round(x-z,2))
elif y=="*":
    print(round(x*z,2))
else:
    print(round(x/z,2))