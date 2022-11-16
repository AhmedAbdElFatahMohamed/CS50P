from validator_collection import validators, checkers, errors
try:
    email_address = validators.email(input("what's your email address? "))
    if email_address:
        print ("Valid")
except:
    print("Invalid")