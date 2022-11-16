name=input("what's your name? ").strip()
if "," in name:
    last,first=name.split(", ")
    name =f"{first} {last}"
print(f"hello,{name}")

#using regex groups:

import re
name=input("what's your name? ").strip()
matches=re.search(r"^(.+),(.+)$", name)
if matches:
    last,first=matches.group()    #captures the groups from the search
    name=f"{first} {last}"
print(f"hello, {name}")

# spliting groups:

import re
name=input("what's your name? ").strip()
matches=re.search(r"^(.+),(.+)$", name)
if matches:
    last=matches.group(1)
    first=matches.group(2)
    name=f"{first} {last}"
print(f"hello, {name}")

#concat group:

import re
name=input("what's your name? ").strip()
matches=re.search(r"^(.+), *(.+)$", name)
if matches:
    name=matches.group(2)+" "+matches.group(1)
print(f"hello, {name}")

#using walrus operators (:=) to combine boolean condition

import re
name=input("what's your name? ").strip()
if matches:=re.search(r"^(.+), *(.+)$", name):
    name=matches.group(2)+" "+matches.group(1)
print(f"hello, {name}")