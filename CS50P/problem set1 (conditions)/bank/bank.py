reply=input("Greeting: ").strip().lower()
if reply.split(",")[0]=="hello":
    print("$0")
elif reply[0]=="h":
    print("$20")
else:
    print("$100")