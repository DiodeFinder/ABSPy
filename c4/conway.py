# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of list for the details
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Adding a living cell
        else:
            column.append(' ') # Adding a dead cell
        nextCells.append(column) #nextCells is list of column list

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    #print current cells in the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '')
        print()

    # Calculate the next cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbour co ordinates
            # '% WiDTH' ensure leftCoord is always between 0 to WIDTH-1
            leftCoord = (x-1) % WIDTH
            rightCoord =(x+1) % WIDTH
            aboveCoord =(y-1) % HEIGHT
            belowCoord =(y+1) % HEIGHT

            #Count numbers of living neighbours:
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours +=1

            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(1)            
