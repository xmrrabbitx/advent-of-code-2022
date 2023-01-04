import csv

with open("input.csv", "r") as readObj:

    csv_reader = csv.reader(readObj)

    list_of_csv = list(csv_reader)

    # Y:draw, X:loose, Z:win
    # ROCK:1,PAPER:2,SCISSOR:3

    loss = {"A":"paper","B":"scissor","C":"rock"}
    succ = {"A":"scissor","B":"rock","C":"paper"}
    inp = {"A":"rock","B":"paper","C":"scissor"}
    points = {"rock":1,"paper":2,"scissor":3}

    g = 0
    for x in list_of_csv:
        oponnent = x[0][0]
        you = x[0][2]
        
        # Win scenario
        if you == "Z":
            if(oponnent in loss):
                me = loss[oponnent]
                g += (points[me] + 6)
        # loss scenario
        elif you == "X":
            if(oponnent in succ):
                me = succ[oponnent]
                g += (points[me] + 0) 
        else:
            me = inp[oponnent]
            g += (points[me] + 3)

print(g)




        
        
        