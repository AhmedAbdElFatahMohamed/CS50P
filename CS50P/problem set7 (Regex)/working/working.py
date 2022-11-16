import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        matches=re.search(r"(\d+)[\s|:]([0-5]?\d?)\s?([A|P]M) to (\d+)[\s|:]([0-5]?\d?)\s?([A|P]M)",s)
        if matches:
            A=int(matches.group(1))
            B=int(matches.group(4))
            C=matches.group(2)
            D=matches.group(5)
            if matches.group(3)=="AM" and A==12:
                A="00"
            if matches.group(3)=="PM":
                A=A+12
            if matches.group(6)=="PM" and B<12:
                B=B+12
            if not C:
                C="00"
            if not D:
                D="00"
            return f"{A:02}:{C} to {B:02}:{D}"
        else:
            raise ValueError

if __name__ == "__main__":
    main()