#chaecking for @ and . in input:

email=input("what's your email? ").strip()

if '@' in email and "." in email:
    print("Valid")
else :
    print("Invalid")

#checking for username and domain:

email=input("what's your email? ").strip()

username,domain=email.split("@")
if (username) and ("." in domain):     #these are 2 conditions it will check if username exists and . in domain
    print("Valid")
else :
    print("Invalid")

#using endswith:
email=input("what's your email? ").strip()

username,domain=email.split("@")
if (username) and email.endswith(".edu"):
    print("Valid")
else :
    print("Invalid")


#using Regex:
import re
email=input("what's your email? ").strip()

if re.search(r"^\w+@(\w\.)?\w+\.edu$",email,re.IGNORECASE):                    #adding r at the start of the search  to avoid misinterpreting the \
    print("Valid")
else :
    print("Invalid")



