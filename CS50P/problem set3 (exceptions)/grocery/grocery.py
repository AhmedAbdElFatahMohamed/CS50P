import collections
d={}
num=1
while True:
    try:
        item=input("").upper()
        if item in d:
          d[item]=num+1
          continue
        else:
          d[item]=num
          continue

    except EOFError:
        od = collections.OrderedDict(sorted(d.items()))
        for a,b in od.items() :
          print(b,a)
        break
    except KeyError:
        continue