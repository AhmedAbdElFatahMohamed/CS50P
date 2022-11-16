import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches:=re.search(r"^<iframe.+https?://(www\.)?youtube\.com/embed/(\w+)",s):
        s="https://youtu.be/"+matches.group(2)
        return s


if __name__ == "__main__":
    main()