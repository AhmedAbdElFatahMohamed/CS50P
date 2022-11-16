#using a full regex for the whole ip resulted in test error
#her code is cleaner

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate (ip):
    pattern=r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    matches=re.search(pattern,ip,re.IGNORECASE)
    if matches:
        return "True"
    else :
        return "False"

if __name__ == "__main__":
    main()


# import re

# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate (ip):
#     if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
#         num_list=ip.split(".")
#         for num in num_list:
#             if int(num)<0 or int(num)>255:
#                 return False
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     main()