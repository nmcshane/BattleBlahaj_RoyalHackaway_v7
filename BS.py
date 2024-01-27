rows, rows = (5, 5)
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(10):
    print(grid[i])

blaharier_Num = 5
battleblahaj_Num = 4
bluiser_Num = 3
sharkmarine_Num = 3
desharker_Num = 2

blaharier_Pos = [0, 0]
battleblahaj_Pos = [0, 0]
bluiser_Pos = [0, 0]
sharkmarine_Pos = [0, 0]
desharker_Pos = [0, 0]

ships = ["blaharier", "battleblahaj", "bluiser", "sharkmarine", "desharker"]
n = 0
for i in ships:
    print("Enter row number for start of " + i + ": ")
    x_Row = int(input())
    print("Enter column number for start of " + i + ": ")
    x_Col = int(input())
    print("Horizontal or vertical? (H or V)")
    x_Orientation = input()
    if n == 0:
        blaharier_Pos = [[x_Row], [x_Col]]
        if x_Orientation == "H":
            for i in range(blaharier_Num):
                x
                grid[[x_Row], [x_Col+i]] = 1;
        elif x_Orientation == "V":
            for i in range(blaharier_Num):
                grid[[x_Row+1], [x_Col]] = 1;
        print(blaharier_Pos)
    elif n == 1:
        battleblahaj_Pos = [[x_Row], [x_Col]]
        if x_Orientation == "H":
            for i in range(battleblahaj_Num):
                grid[[x_Row], [x_Col+i]] = 2;
        elif x_Orientation == "V":
            for i in range(battleblahaj_Num):
                grid[[x_Row+1], [x_Col]] = 2;
        print(battleblahaj_Pos)
    elif n == 2:
        bluiser_Pos = [[x_Row], [x_Col]]
        if x_Orientation == "H":
            for i in range(bluiser_Num):
                grid[[x_Row], [x_Col+i]] = 3;
        elif x_Orientation == "V":
            for i in range(blaharier_Num):
                grid[[x_Row+1], [x_Col]] = 3;
        print(bluiser_Pos)
    elif n == 3:
        sharkmarine_Pos = [[x_Row], [x_Col]]
        if x_Orientation == "H":
            for i in range(sharkmarine_Num):
                grid[[x_Row], [x_Col+i]] = 4;
        elif x_Orientation == "V":
            for i in range(sharkmarine_Num):
                grid[[x_Row+1], [x_Col]] = 4;
        print(sharkmarine_Pos)
    elif n == 4:
        desharker_Pos = [[x_Row], [x_Col]]
        if x_Orientation == "H":
            for i in range(desharker_Num):
                grid[[x_Row], [x_Col+i]] = 5;
        elif x_Orientation == "V":
            for i in range(desharker_Num):
                grid[[x_Row+1], [x_Col]] = 5;
        print(desharker_Pos)
    n = n + 1
