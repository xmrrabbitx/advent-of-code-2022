import csv

with open("part1.csv", "r") as readObj:

    csv_reader = csv.reader(readObj)

    list_of_csv = list(csv_reader)

    # A,X:rock , B,Y:paper , C,Z:scissor
    loss = {"A":"Z","B":"X","C":"Y"}
    succ = {"A":"Y","B":"Z","X":"Y","C":"X"}
    points = {"X":1,"Y":2,"Z":3}
    y = 0
    f = 0
    p = 0
    for x in list_of_csv:

        oponnent = x[0][0]
        you = x[0][2]
        l = {oponnent:you}

        if((oponnent,you) in succ.items()):
            p = 6
        elif((oponnent,you) in loss.items()):
            p = 0
        else:
            p = 3
        if(you in points.keys()):
            g = points[you]
            d = (g+p)
            f += (g+p)
    print(f)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            



        
        
        