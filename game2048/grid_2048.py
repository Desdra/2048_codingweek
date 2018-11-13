import random

def create_grid():
    grid = []
    for i in range(0,4):
        grid.append([' ',' ',' ', ' '])
    return grid

def init_grid(grid):
    i2,j2 = random.randint(0,3),random.randint(0,3)
    grid[i2][j2] = 2
    i4,j4 = random.randint(0,3),random.randint(0,3)
    while i2 == i4 and j2 == j4:
        i4,j4 = random.randint(0,3),random.randint(0,3)
    grid[i4][j4] = 4
    return grid

print(init_grid(create_grid()))
