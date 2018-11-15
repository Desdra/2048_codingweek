from gamep4.game_p4 import *
from gamep4.grid_p4 import *
from gamep4.player_interaction_p4 import *

def launch():
    """lance le jeu"""
    (size_number_horizontal,size_number_vertical,size_column) = (6,6,8)# player_setup_size()
    grid = create_grid(size_number_horizontal,size_number_vertical)
    player = 0
    print(display_grid(grid, size_column))
    while 1:
        print("C'est le tour du joueur", player+1)
        move = get_player_move(size_number_horizontal, grid)
        make_a_move(grid, player, move)
        print(display_grid(grid,size_column))
        if is_last_move_winning(grid,player, move):
            print("le joueur ", player +1 , "gagne")
            break
        player = 1-player


if __name__ == "__main__" :
    launch()
