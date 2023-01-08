from enum import Enum
import string
from collections import Counter

inp = open("input.txt")
r = inp.readlines()

az = list(string.ascii_lowercase)
AZ = list(string.ascii_uppercase)
lowerAlpha = Enum('loweralpha', az, start=1)
upperAlpha = Enum('upperalpha', AZ, start=27)


jo = []
arr = []
for x in r:
    l = x.rstrip("\n")

    jo.append(list(l))


le = int(len(r)/3)


lis = []
y = 0 
g = 3
for x in range(le):
    lis.append(jo[y:g])
    y += 3
    g += 3

ll = []
k = 0
ar = []

for f in lis:
    for x in f:
        x = set(x)
        x = list(x)
        ll = x + ll
    ar.append(ll)
    ll = []
rmdup = []
for y in ar:
    for n in Counter(y):
        if(Counter(y)[n]) >= 3:
           rmdup.append(n)

points = []
for g in rmdup:         
    for loweralpha in lowerAlpha:
            if (g == loweralpha.name):
                points.append(loweralpha.value)
                
    for upperalpha in upperAlpha:
            if (g == upperalpha.name):
                points.append(upperalpha.value)

print(sum(points))
