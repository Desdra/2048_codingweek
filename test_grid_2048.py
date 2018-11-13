from game2048.grid_2048 import *
from pytest import *


def test_create_grid():
    assert create_grid() == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

def test_init_grid():
    grid = init_grid(create_grid())
    twoPresent,fourPresent = 0,0

    for i in grid:
        if 2 in i:
            twoPresent = 1 - twoPresent
        if 4 in i:
            fourPresent = 1 - fourPresent
    assert twoPresent and fourPresent
