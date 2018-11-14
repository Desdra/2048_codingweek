from game2048.themes import THEMES

def player_setup_theme():
    theme_number = input("Rentrez le numéro du thème que vous souhaitez avoir")
    if not(theme_number in THEMES.keys()):
        return None
    return theme_number

def player_setup_size():
    size_number = input("Rentrez la taille de grille que vous souhaitez avoir")
    return int(size_number)


def get_player_direction():
    direction = input("Dans quelle direction voulez-vous jouez ? (d : droite, g : gauche, h : haut, b : bas)")
    while not(direction in ["d","g","h","b"]):
        direction = input("Direction invalide, reéssayez (d : droite, g : gauche, h : haut, b : bas)")
    return ["d","g","h","b"].index(direction)
