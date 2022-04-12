import time
# create the grid
loveGrid = [['.','.','0','0','.','0','0','.','.'],
            ['.','0','0','0','0','0','0','0','.'],
            ['.','0','0','0','0','0','0','0','.'],
            ['.','.','0','0','0','0','0','.','.'],
            ['.','.','.','0','0','0','.','.','.'],
            ['.','.','.','.','0','.','.','.','.']]
# print the grid
while True:
    for i in range(len(loveGrid)):
        for j in range(len(loveGrid[i])):
            print(loveGrid[i][j], end = '')
        print()
    time.sleep(0.5)
    print('\n\n')
