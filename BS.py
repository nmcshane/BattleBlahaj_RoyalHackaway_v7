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

def chooseShipPos():
    n = 0
    for i in ships:
        if n == 0:
            ship_Size = 5
        elif n == 1:
            ship_Size = 4
        elif (n == 2) or (n == 3):
            ship_Size = 3
        elif n == 4:
            ship_Size = 3
        print("Enter row number (0-9) for the start of " + i + " (" + str(ship_Size) + " spaces): ")
        x_Row = int(input())
        print("Enter column number (0-9) for the start of " + i + " (" + str(ship_Size) + " spaces): ")
        x_Col = int(input())
        print("Horizontal or vertical? (H or V)")
        x_Orientation = input()


        if n == 0:
            grid[x_Row][x_Col] = 1
            blaharier_Pos = [x_Row, x_Col]
            if x_Orientation == "H":
                for i in range(blaharier_Num - 1):
                    x_Col = x_Col + 1
                    grid[x_Row][x_Col] = 1
            elif x_Orientation == "V":
                for i in range(blaharier_Num - 1):
                    x_Row = x_Row + 1
                    grid[x_Row][x_Col] = 1
            for i in range(10):
                print(grid[i])
        elif n == 1:
            battleblahaj_Pos = [x_Row, x_Col]
            grid[x_Row][x_Col] = 2
            if x_Orientation == "H":
                for i in range(battleblahaj_Num - 1):
                    x_Col = x_Col + 1
                    grid[x_Row][x_Col] = 2
            elif x_Orientation == "V":
                for i in range(battleblahaj_Num - 1):
                    x_Row = x_Row + 1
                    grid[x_Row][x_Col] = 2
            for i in range(10):
                print(grid[i])
        elif n == 2:
            bluiser_Pos = [x_Row, x_Col]
            grid[x_Row][x_Col] = 3
            if x_Orientation == "H":
                for i in range(bluiser_Num - 1):
                    x_Col = x_Col + 1
                    grid[x_Row][x_Col] = 3
            elif x_Orientation == "V":
                for i in range(blaharier_Num - 1):
                    x_Row = x_Row + 1
                    grid[x_Row][x_Col] = 3
            for i in range(10):
                print(grid[i])
        elif n == 3:
            sharkmarine_Pos = [x_Row, x_Col]
            grid[x_Row][x_Col] = 4
            if x_Orientation == "H":
                for i in range(sharkmarine_Num - 1):
                    x_Col = x_Col + 1
                    grid[x_Row][x_Col] = 4
            elif x_Orientation == "V":
                for i in range(sharkmarine_Num - 1):
                    x_Row = x_Row + 1
                    grid[x_Row][x_Col] = 4
            for i in range(10):
                print(grid[i])
        elif n == 4:
            desharker_Pos = [x_Row, x_Col]
            grid[x_Row][x_Col] = 5
            if x_Orientation == "H":
                for i in range(desharker_Num - 1):
                    x_Col = x_Col + 1
                    grid[x_Row][x_Col] = 5
            elif x_Orientation == "V":
                for i in range(desharker_Num - 1):
                    x_Row = x_Row + 1
                    grid[x_Row][x_Col] = 5
            for i in range(10):
                print(grid[i])
        n = n + 1
    for i in range(100):
        print()
    

def hitOrMiss():
    blaharier_Left = 5
    battleblahaj_Left = 4
    bluiser_Left = 3
    sharkmarine_Left = 3
    desharker_Left = 2
    blaharier_Sunk = False
    battleblahaj_Sunk = False
    bluiser_Sunk = False
    sharkmarine_Sunk = False
    desharker_Sunk = False
    print("Enter row number (0-9) to attack: ")
    hit_Row = input()
    print("Enter column number (0-9) to attack: ")
    hit_Col = input()
    for i in range(10):
        for j in range(10):
            if grid[hit_Row][hit_Col] == 1:
                print("HIT")
                blaharier_Left -= 1
                if blaharier_Left <= 0:
                    print("BLAHARIER SUNK")
                    blaharier_Sunk = True
                grid[hit_Row][hit_Col] = 9
            if grid[hit_Row][hit_Col] == 2:
                print("HIT")
                battleblahaj_Left -= 1
                if battleblahaj_Left <= 0:
                    print("BATTLEBLAHAJ SUNK")
                    battleblahaj_Sunk = True
                grid[hit_Row][hit_Col] = 9
            if grid[hit_Row][hit_Col] == 3:
                print("HIT")
                bluiser_Left -= 1
                if bluiser_Left <= 0:
                    print("BLUSIER SUNK")
                    bluiser_Sunk = True
                grid[hit_Row][hit_Col] = 9
            if grid[hit_Row][hit_Col] == 4:
                print("HIT")
                sharkmarine_Left -= 1
                if sharkmarine_Left <= 0:
                    print("SHARKMARINE SUNK")
                    sharkmarine_Sunk = True
                grid[hit_Row][hit_Col] = 9
            if grid[hit_Row][hit_Col] == 5:
                print("HIT")
                desharker_Left -= 1
                if desharker_Left <= 0:
                    print("DESHARKER SUNK")
                    desharker_Sunk = True
                grid[hit_Row][hit_Col] = 9            
            else:
                print("MISS")

def win():
    


chooseShipPos()