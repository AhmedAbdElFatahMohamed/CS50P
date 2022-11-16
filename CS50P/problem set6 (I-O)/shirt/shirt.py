import sys
import os
from PIL import Image
from PIL import ImageOps

ext=[".png",".jpg",".jpeg"]

try:
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv)==3:
        t1=os.path.splitext(sys.argv[1])
        t2=os.path.splitext(sys.argv[2])
        if t1[1] not in ext or t2[1] not in ext:
            sys.exit("Invalid output")
        elif t1[1] != t2[1]:
            sys.exit("Input and output have different extensions")
        else:
            shirt = Image.open("shirt.png")
            photo=Image.open(sys.argv[1])
            size = shirt.size
            new=ImageOps.fit(photo,size)
            new.paste(shirt, shirt)
            new.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("input does not exist")





