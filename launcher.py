from game2048.game import *
from game2048.grid_2048 import *
from game2048.player_interaction import *


grid = init_grid()
theme_number = player_setup_theme()
player_size = player_setup_size()
while 1:
    print(display_grid(grid, theme_number, player_size))
    direction = get_player_direction()
    grid = evolve_grid(grid,direction)
    if not(check_for_lost(grid)):
        grid = create_new_tile(grid)
    else:
        print("Vous avez perdu, dommage")
        break
