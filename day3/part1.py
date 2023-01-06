from enum import Enum
import string

inp = open("input.txt")
r = inp.readlines()

az = list(string.ascii_lowercase)
AZ = list(string.ascii_uppercase)
lowerAlpha = Enum('loweralpha', az, start=1)
upperAlpha = Enum('upperalpha', AZ, start=27)

arr = []

for x in r:
    l = x.rstrip("\n")

    # 
    m = int(len(l) / 2)
    f = int(len(l))
    
    part1 = list(l[0:m])
    part2 = l[m:f]

    s = set(part2)
    re = [x for x in part1 if x in s]
    
    rmdup = list(dict.fromkeys(re))

    for loweralpha in lowerAlpha:
        if (rmdup[0] == loweralpha.name):
            arr.append(lower alpha.value)
            
    for upperalpha in upperAlpha:
        if (rmdup[0] == upperalpha.name):
            arr.append(upperalpha.value)


print(sum(arr))

