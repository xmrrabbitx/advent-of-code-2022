inp = open("part2.txt")

r = inp.readlines()

arr = []
y = 0
g = 0 
for x in r:

    l = x.rstrip("\n")
    
    if(l != ""):
        l = int(l)
        y += l    
    else:
        arr.append(y)
        y = 0
    g += 1
    if (g == len(r)):
        arr.append(y)

# add this codes
first = max(arr)
arr.remove(max(arr))
second = max(arr)
arr.remove(max(arr))
third = max(arr)


result = first + second + third
print(result)