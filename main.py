size = int(input("Select the grid size (3-20): "))
end = False
if size < 3 or size > 20:
    end = True
values = [0 for i in range(size**2)]
turn = "1"

def start():
    global values
    global turn
    global end
    drawgame()
    if checkwin(values, turn) == False:
        place = input("Select where you want to place your marker (" + turn.replace("1", "X").replace("2", "O") + "): ")
        if values[int(place)] == 0 and int(place) <= len(values):
            values[int(place)] = int(turn)
            if turn == "1":
                turn = "2"
            elif turn == "2":
                turn = "1"
        else:
            print("Please choose an empty space!")
    else:
        end = True

def drawgame():
    print("\n")
    var = 0
    var1 = 0
    triliza = size*"╍╍╍╍" + "\n"
    for i in range(size**2):
        var += 1
        var1 += 1
        if var == size:
            var = 0
            if size**2 - var1 > 0:
                triliza = triliza + "┇ " + str(values[i]) + " ┇ \n"
                triliza = triliza + size*"╍╍╍╍" + "\n"
            else:
                triliza = triliza + "┇ " + str(values[i]) + " ┇ \n"
                triliza = triliza + size*"╍╍╍╍" + "\n"
        else:
            triliza = triliza + "┇ " + str(values[i]) + " "
    triliza = triliza.replace("0", " ")
    triliza = triliza.replace("1", "X")
    triliza = triliza.replace("2", "O")
    print(triliza + "\n")

def checkwin(val, turn):
    if turn == "1":
        turn = "O"
    elif turn == "2":
        turn = "X"

    for m in range(0, size**2, size):
        lastn = m
        possible = False
        for n in range(1, size):
            if values[n + m] == values[lastn] and values[n + m] != 0:
                possible = True
                lastn = n + m
            else:
                possible = False
                break
        if possible == True:
            print(turn + " won!!")
            return True

    for m in range(size):
        lastn = m
        possible = False
        for n in range(0, size**2, size):
            if values[n + m] == values[lastn] and values[n + m] != 0:
                possible = True
                lastn = n + m
            else:
                possible = False
                break
        if possible == True:
            print(turn + " won!!")
            return True

    lastm = 0
    possible = False
    for m in range(0, size**2, size + 1):
        if values[m] == values[lastm] and values[m] != 0:
            possible = True
            lastm = m
        else:
            possible = False
            break
    if possible == True:
        print(turn + " won!!")
        return True

    lastm = size - 1
    possible = False
    for m in range(size - 1, size**2 - 1, size - 1):
        if values[m] == values[lastm] and values[m] != 0:
            possible = True
            lastm = m
        else:
            possible = False
            break
    if possible == True:
        print(turn + " won!!")
        return True

    return False

while not end:
    start()
