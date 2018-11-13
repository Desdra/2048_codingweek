from game2048.themes import THEMES

def player_setup():
    theme_number = input("Rentrez le numéro du thème que vous souhaitez avoir")
    if not(theme_number in THEMES.keys()):
        return None
    return theme_number

def get_player_direction():
    direction = input("Dans quelle direction voulez-vous jouez ? (d : droite, g : gauche, h : haut, b : bas)")
    while not(direction in ["d","g","h","b"]):
        direction = input("Direction invalide, reéssayez (d : droite, g : gauche, h : haut, b : bas)")
    return ["d","g","h","b"].index(direction)
