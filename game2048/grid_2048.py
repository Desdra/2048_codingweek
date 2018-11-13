import random
import numpy as np

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}
theme = THEMES['0']

def create_grid():
    grid = []
    for i in range(0,4):
        grid.append([' ',' ',' ', ' '])
    return grid

def init_grid():
    grid = create_grid()
    i2,j2 = random.randint(0,3),random.randint(0,3)
    grid[i2][j2] = 2
    i4,j4 = random.randint(0,3),random.randint(0,3)
    while i2 == i4 and j2 == j4:
        i4,j4 = random.randint(0,3),random.randint(0,3)
    grid[i4][j4] = 4
    return grid

def display_grid(grid,theme):
    size = theme_size(theme)
    string = ""
    for i in range(4):
        string += " "
        for j in range(4):
            string += "="*size + " "
        string += "\n|"
        for j in range(4):
            if grid[i][j] == " ":
                string += " "*size + "|"
            else:
                number_size = elem_to_string_size(theme[grid[i][j]])
                string += " "*int((size -number_size)/2) + theme[grid[i][j]] +" "*int(np.ceil((size -number_size)/2)) + "|"
        string += "\n"
    string += " "
    for i in range(4):
        string += "="*size + " "
    return string

def theme_size(theme):
    max = 0
    for case in range(1,14):
        if max < elem_to_string_size(theme[2**case]):
            max = elem_to_string_size(theme[2**case])
    return max

def elem_to_string_size(n):
    if type(n) == type("str"):
        return len(n)
    return int(np.ceil(np.log10(n)))
