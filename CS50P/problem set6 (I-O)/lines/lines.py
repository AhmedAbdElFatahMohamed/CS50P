# problems : using line=="\n" resulted in errors
# using startswith without strip resulted in errors

import sys

count = 0
try:
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith("#"):  # check for commented lines
                    count = count
                elif line.isspace():  # check for empty lines
                    count = count
                else:
                    count = count + 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
