import sys
Rules = "<-----RULES---->\n1.BRUSH DOWN\n2.BRUSH UP\n3.VEHICLE ROTATES RIGHT\n4.VEHICLE ROTATES LEFT\n5.MOVE UP TO X(5_X)\n6.JUMP\n7.REVERSE DIRECTION\n8.VIEW THE MATRIX\n0.EXIT\n"
print(Rules)
correct = 0
while correct == 0:   
    commandlistcheck = [] 
    commandlist = str(input("Please enter the commands with a plus sign (+) between them.\n")).split("+")
    for term in commandlist[1:]: 
        errorbox = []
        for wrongones in term:
            errorbox.append(wrongones)
        if errorbox[0] == "5" and errorbox[1] == "_":
            continue    
        else:
            commandlistcheck.append(int(term))
    correctbox = []
    for check in commandlistcheck:
        if check > 8 or check < 0:
            continue
        else:
           correctbox.append("1")
    if len(commandlistcheck)  == len(correctbox):
        correct = 1
    else:
        print("You entered an incorrect command. Please try again!")
inputn = int(commandlist[0])+2
yaxis = 1
xaxis = 1
thegamemaprow1 = []
thegamemap = []
otherrows = []
rotation = 1 #1 is east, 2 is north, 3 is west and 4 is south.
brushlocation = 0 #0 is brush up, 1 is brush down.
carlocation = 0 #car location should be presented as (yaxis, xaxis)
def gamemapgenerator():
    for unit in range(inputn):   
        thegamemaprow1.append("+")
    otherrows.append("+")
    counter = 0
    while counter<inputn-2: 
        otherrows.append(" ")
        counter += 1
    otherrows.append("+")
    thegamemap.append(thegamemaprow1[:])        
    for rowminus2 in range(inputn-2):
        thegamemap.append(otherrows[:])     
    thegamemap.append(thegamemaprow1[:])
def turn180mechanism():
    global rotation
    if rotation == 1:
        rotation = 3
    elif rotation == 3:
        rotation = 1
    elif rotation == 2:
        rotation = 4
    elif rotation == 4:
        rotation = 2
def turnleftmechanism():
    global rotation
    if rotation == 1:
        rotation = 2
    elif rotation == 2:
        rotation = 3
    elif rotation == 3:
        rotation = 4
    elif rotation == 4:
        rotation = 1
def turnrightmechanism():
    global rotation
    if rotation == 1:
        rotation = 4
    elif rotation == 4:
        rotation = 3
    elif rotation == 3:
        rotation = 2
    elif rotation == 2:
        rotation = 1  
def brushdownmechanism():
    global brushlocation
    global xaxis
    global yaxis
    brushlocation = 1 
    thegamemap[yaxis][xaxis] = "*"
def brushupmechanism():
    global brushlocation
    brushlocation = 0 
def printmapmechanism():
    for counter1 in range(len(thegamemap)):
        for counter2 in range(len(thegamemap[counter1])-1):
            print(thegamemap[counter1][counter2], end="")
        print(thegamemap[counter1][-1])
def jumpmechanism():
    global brushlocation
    global xaxis
    global yaxis
    if rotation == 1:
        if xaxis+3 > len(otherrows)-2:
            xaxis = len(otherrows)-xaxis-3
        else:
            xaxis = xaxis+3
        brushlocation = 0
    elif rotation == 2:
        if yaxis-3 < 1:
            yaxis = len(otherrows)+yaxis-4
        else:
            yaxis = yaxis-3
        brushlocation = 0
    elif rotation == 3:
        if xaxis-3 < 1:
            xaxis = len(otherrows)+xaxis-4
        else:    
            xaxis = xaxis-3
        brushlocation = 0
    elif rotation == 4:
        if yaxis+3 > len(otherrows)-2:
            yaxis = len(otherrows)-yaxis-3
        else:
            yaxis = yaxis+3
        brushlocation = 0
def movemechanism(road):
    global xaxis
    global yaxis
    if rotation == 1:   
        for everymove in range(1, road+1):
            xaxis = xaxis+1
            if xaxis != len(otherrows)-1 and brushlocation == 1:
                thegamemap[yaxis][xaxis] = "*"
            elif xaxis == len(otherrows)-1:
                xaxis = 1
                if brushlocation == 1:
                    thegamemap[yaxis][xaxis] = "*"                           
    elif rotation == 2:
        for everymove in range(1, road+1):
            yaxis = yaxis-1
            if xaxis != 0 and yaxis != 0 and brushlocation == 1:
                thegamemap[yaxis][xaxis] = "*"  
            elif yaxis == 0:
                yaxis = len(otherrows)-2
                if brushlocation == 1:
                    thegamemap[yaxis][xaxis] = "*"
    elif rotation == 3:
        for everymove in range(1, road+1):
            xaxis = xaxis-1
            if xaxis != 0 and yaxis != 0 and brushlocation == 1:
                thegamemap[yaxis][xaxis] = "*"  
            elif xaxis == 0:
                xaxis = len(otherrows)-2
                if brushlocation == 1:
                    thegamemap[yaxis][xaxis] = "*"
    elif rotation == 4:
        for everymove in range(1, road+1):    
            yaxis = yaxis+1
            if yaxis != len(otherrows)-1 and brushlocation == 1:
                thegamemap[yaxis][xaxis] = "*"  
            elif yaxis == len(otherrows)-1:
                yaxis = 1
                if brushlocation == 1:
                    thegamemap[yaxis][xaxis] = "*"
def generalprocess():
    gamemapgenerator()
    for repeat in range(1, int(len(commandlist))):
        checkbox = []
        for commandpart in str(commandlist[repeat]):
            checkbox.append(commandpart)       
        if len(checkbox) == 1:
            if checkbox[0] == "1":
                brushdownmechanism()
            elif checkbox[0] == "2":
                brushupmechanism()
            elif checkbox[0] == "3":
                turnrightmechanism()
            elif checkbox[0] == "4":
                turnleftmechanism()    
            elif checkbox[0] == "6":
                jumpmechanism()
            elif checkbox[0] == "7":
                turn180mechanism()     
            elif checkbox[0] == "8":
                printmapmechanism()
            elif checkbox[0] == "0":
                break
        elif len(checkbox) > 2:       
            if len(checkbox) == 3:               
                movemechanism(int(checkbox[2]))
            else:
                moredigitmove = ""
                for digit in checkbox[2:]:
                    moredigitmove = moredigitmove+digit 
                movemechanism(int(moredigitmove))
generalprocess()        



