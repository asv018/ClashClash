import os
from colorama import init, Fore, Back
init(autoreset=True)


def clearTerminal():
    cmd = 'cls' if os.name == 'nt' or os.name == 'dos' else 'clear'
    os.system(cmd)


def printGame(layoutMap):
    gameLayout = ""
    for i in range(len(layoutMap)):
        for j in range(len(layoutMap[i])):
            gameLayout += layoutMap[i][j]
        gameLayout += "\n"
    os.write(1, str.encode(gameLayout))


def fillColors(startX, startY, height, width, color, layout):
    for i in range(height):
        for j in range(width - 1):
            layout[startX + i][startY + j] = color + layout[startX + i][startY + j] # NOQA
        layout[startX + i][startY + width - 1] = Fore.RESET + Back.RESET + layout[startX + i][startY + width - 1] # NOQA


def checkCollision(startX1, startY1, height1, width1, startX2, startY2, height2, width2): # NOQA
    if startX1 + height1 <= startX2:
        return False
    if startX2 + height2 <= startX1:
        return False
    if startY1 + width1 <= startY2:
        return False
    if startY2 + width2 <= startY1:
        return False
    return True


def displayVictory():
    print(r'''
                         __      ___      _                     _   _ 
                         \ \    / (_)    | |                   | | | |
                          \ \  / / _  ___| |_ ___  _ __ _   _  | | | |
                           \ \/ / | |/ __| __/ _ \| '__| | | | | | | |
                            \  /  | | (__| || (_) | |  | |_| | |_| |_|
                             \/   |_|\___|\__\___/|_|   \__, | (_) (_)
                                                         __/ |        
                                                        |___/         
    ''') # NOQA


def displayDefeat():
    print(r''' 
                          _____        __           _           __
                         |  __ \      / _|         | |     _   / /
                         | |  | | ___| |_ ___  __ _| |_   (_) | | 
                         | |  | |/ _ \  _/ _ \/ _` | __|      | | 
                         | |__| |  __/ ||  __/ (_| | |_    _  | | 
                         |_____/ \___|_| \___|\__,_|\__|  (_) | | 
                                                               \_\
''')  # NOQA