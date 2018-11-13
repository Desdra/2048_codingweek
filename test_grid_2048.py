from game2048.grid_2048 import *
from pytest import *

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def test_create_grid():
    assert create_grid() == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

def test_init_grid():
    grid = init_grid()
    twoPresent,fourPresent = 0,0

    for i in grid:
        if 2 in i:
            twoPresent = 1 - twoPresent
        if 4 in i:
            fourPresent = 1 - fourPresent
    assert twoPresent and fourPresent

def test_diplay_grid():
    a=""" ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n|    |    |    |    |\n ==== ==== ==== ==== \n| 2  |    |    | 2  |\n ==== ==== ==== ==== """
    print(a)
    assert display_grid([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [2, ' ', ' ', 2]],THEMES['0'])==a

def test_theme_size():
    assert theme_size(THEMES['0']) == 4
    assert theme_size(THEMES['1']) == 2

def test_elem_to_string_size():
    assert elem_to_string_size("test") == 4
    assert elem_to_string_size(4096) == 4
    assert elem_to_string_size(16384) == 5
