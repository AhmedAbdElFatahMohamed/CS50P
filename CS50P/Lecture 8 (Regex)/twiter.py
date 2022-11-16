import re

url=input("URL: ").strip()

username=re.sub(r"(^https?://)?(www\.)?twitter\.com/","",url)         #works like string replace
                                                                      #need to escape . with \
print(f"username {username}")

#using sub while the regex doesn't exist will result in false date so we use seaarch

import re
url=input("URL: ").strip()

matches=re.search(r"https?://(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if matches:
    print(f"username: ",matches.group(2))

#using walrus and non capturing group:

import re
url=input("URL: ").strip()

if matches:=re.search(r"https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(f"username: ",matches.group(1))

