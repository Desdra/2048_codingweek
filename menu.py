import launcher_p4
import launcher_2048

jeu = int(input("A quel jeu voulez vous jouez ? 0 : 2048, 1: Puissance 4"))
while not(jeu in [0,1]):
    jeu = int(input("jeu non reconnu, réessayez. 0 : 2048, 1: Puissance 4"))

if jeu == 0:
    launcher_2048.launch()
if jeu == 1:
    launcher_p4.launch()
