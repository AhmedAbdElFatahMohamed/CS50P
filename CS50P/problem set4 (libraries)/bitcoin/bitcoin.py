#trick/Bug:Check if input is string (Line 11)

import requests
import json
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

try:
    i = sys.argv[1]
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    # elif i.isalpha():
    elif not isfloat(i):
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
        O = response.json()
        O = O["bpi"]["USD"]["rate"]
        amount = (
            float(O.split(",")[0] + O.split(",")[1].split(".")[0] + O.split(".")[1])
            / 10000
            * float(sys.argv[1])
        )
        print(f"${amount:,.4f}")
except (requests.RequestException, ValueError):
    sys.exit()
