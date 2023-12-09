from src.characters import Barbarians
from src.king import King
from src.building import Castle, TownHall, Hut, Wall, Cannon
from src.gameSetting import Game
from src.input import Get
from src.utilities import * # NOQA
from src.init import * # NOQA
from time import sleep
from colorama import init, Fore
import os
init(autoreset=False)

available = os.listdir("replays/")

repNum = 1
for replay in available:
    print(repNum, replay)
    repNum += 1

selectedRep = int(input("Select replay: "))
if selectedRep < 1 or selectedRep > len(available):
    print("Invalid replay number")
    exit()

for i in range(5):
    clearTerminal() # NOQA
    for j in range(13):
        print()
    if(i % 2 == 0):
        print(Fore.RED)
    else:
        print(Fore.GREEN)
    printTitleScreen() # NOQA
    print(Fore.WHITE)
    sleep(0.5)

clearTerminal() # NOQA
gameHeight = 40
gameWidth = 150
layout = initializeLayout(gameHeight=gameHeight, gameWidth=gameWidth) # NOQA
getText = Get()

# castle structure
castleDesign = [" _   |~  _ ", "[_]--'--[_]", "|'|\"\"`\"\"|'|", r"| | /^\ | |", "|_|_|I|_|_|"] # NOQA
castleObject = Castle(100, 10, 20, castleDesign, 0)
castleObject2 = Castle(100, 7, 80, castleDesign, 1)

# townhall structure
townhallDesign = ["___", '/_\\', "| |", "|_|"]
townhallObject = TownHall(100, 17, 60, townhallDesign, 2)

# hut structure
hutDesign = ["  ___I_", " /\\-_--\\", "/  \\_-__\\", "|[]| [] |"]
hutObject = Hut(100, 30, 20, hutDesign, 3)
hutObject2 = Hut(100, 30, 60, hutDesign, 4)
hutObject3 = Hut(100, 20, 100, hutDesign, 5)

buildings = [castleObject, castleObject2, townhallObject, hutObject, hutObject2, hutObject3] # NOQA

for i in range(10):
    tempWall = Wall(100, 15 + i, 57, ["█"], len(buildings))
    buildings.append(tempWall)
    tempWall2 = Wall(100, 15 + i, 65, ["█"], len(buildings))
    buildings.append(tempWall2)
for j in range(8):
    tempWall = Wall(100, 15, 58 + j, ["█"], len(buildings))
    buildings.append(tempWall)
    tempWall2 = Wall(100, 24, 58 + j, ["█"], len(buildings))
    buildings.append(tempWall2)

characterDesign = [" !!!", "/o o\\", "|,,,|"]
characters = []
game = Game()

kingDesign = [" !_! ", " |_| ", "/ | \\", "_/ \\_"]
king = []

cannonDesign = ["  /\\  ", " /  \\ ", " |  | ", " |  | ", "/ == \\", "|/**\\|"]
cannonObject1 = Cannon(100, 20, 90, cannonDesign, len(buildings), 25)
buildings.append(cannonObject1)
cannonObject2 = Cannon(100, 20, 40, cannonDesign, len(buildings), 25)
buildings.append(cannonObject2)


iterationNumber = 0
fileName = "replays/" + available[int(selectedRep) - 1]
my_file = open(fileName, "r")
content = my_file.read().split("\n")
keyPresses = []
for i in range(len(content)-1):
    if i % 2 == 0:
        keyPresses.append([int(content[i]), (content[i+1])])

ptr = 0
while 1:
    clearTerminal() # NOQA
    iterationNumber += 1
    enteredText = ""
    if ptr < len(keyPresses):
        if keyPresses[ptr][0] == iterationNumber:
            enteredText = keyPresses[ptr][1]
            ptr += 1
    if buildings[2].health <= 0:
        game.thDestroyed = 1
    countDestroyed = 0
    countTotal = 0
    for building in buildings:
        if not building.isWall:
            if building.health <= 0:
                countDestroyed += 1
            countTotal += 1
    if countDestroyed == countTotal:
        game.isGameOver = True
    percentDamage = countDestroyed//countTotal
    percentDamage *= 100
    game.percentDamage = percentDamage
    layout = initializeLayout(gameHeight=gameHeight, gameWidth=gameWidth) # NOQA
    clearTerminal() # NOQA

    ############################################################################################################### # NOQA
    # checking key presses
    if enteredText == "z" and game.barbarians > 0:
        tempBarb = Barbarians(100, 10, 10, characterDesign) # NOQA
        characters.append(tempBarb)
        game.spawnBarbarians()

    if enteredText == "x" and game.barbarians > 0:
        tempBarb = Barbarians(100, 10, 110, characterDesign) # NOQA
        characters.append(tempBarb)
        game.spawnBarbarians()

    if enteredText == "c" and game.barbarians > 0:
        tempBarb = Barbarians(100, 30, 100, characterDesign) # NOQA
        characters.append(tempBarb)
        game.spawnBarbarians()

    if enteredText == "1" and game.king > 0:
        King = King(100, 10, 10, kingDesign, gameHeight, gameWidth) # NOQA
        king.append(King)
        characters.append(King)
        game.spawnKing()

    if enteredText == "2" and game.king > 0:
        King = King(100, 10, 110, kingDesign, gameHeight, gameWidth) # NOQA
        king.append(King)
        characters.append(King)
        game.spawnKing()

    if enteredText == "3" and game.king > 0:
        King = King(100, 30, 100, kingDesign, gameHeight, gameWidth) # NOQA
        king.append(King)
        characters.append(King)
        game.spawnKing()

    if enteredText == "w":
        for k in king:
            k.move(-1, 0, buildings)
            if game.rageSpell:
                k.move(-1, 0, buildings)
    elif enteredText == "d":
        for k in king:
            k.move(0, 1, buildings)
            if game.rageSpell:
                k.move(0, 1, buildings)
    elif enteredText == "a":
        for k in king:
            k.move(0, -1, buildings)
            if game.rageSpell:
                k.move(0, -1, buildings)
    elif enteredText == "s":
        for k in king:
            k.move(1, 0, buildings)
            if game.rageSpell:
                k.move(1, 0, buildings)

    if enteredText == "i":
        for k in king:
            k.attack(buildings, 0)
            if game.rageSpell:
                k.attack(buildings, 0)
    elif enteredText == "l":
        for k in king:
            k.attack(buildings, 3)
            if game.rageSpell:
                k.attack(buildings, 3)
    elif enteredText == "j":
        for k in king:
            k.attack(buildings, 2)
            if game.rageSpell:
                k.attack(buildings, 2)
    elif enteredText == "k":
        for k in king:
            k.attack(buildings, 1)
            if game.rageSpell:
                k.attack(buildings, 1)
    elif enteredText == "h":
        for character in characters:
            character.health = min(100, character.health*1.5)
    elif enteredText == "r":
        game.rageSpell = True
    ####################################################################################### # NOQA 

    if not cannonObject1.isDestroyed:
        cannonObject1.attack(characters)
    if not cannonObject2.isDestroyed:
        cannonObject2.attack(characters)

    for building in buildings:
        building.displayBuilding(layout)

    for character in characters:
        if not character.isKing and not character.isDestroyed:
            character.move(buildings)
            if game.rageSpell:
                character.move(buildings)
            character.displayCharacter(layout)

    for kingObject in king:
        if not kingObject.isDestroyed:
            kingObject.displayCharacter(layout)

    if not cannonObject1.isDestroyed:
        cannonObject1.displayBuilding(layout)

    if not cannonObject2.isDestroyed:
        cannonObject2.displayBuilding(layout)
    countAlive = 0
    for character in characters:
        if character.isDestroyed:
            countAlive += 1
    if countAlive == len(characters) and game.barbarians == 0 and game.king == 0: # NOQA
        game.isGameOver = True
    printGame(layout) # NOQA
    sleep(0.05)
    if(enteredText == 'q'):
        break

    if game.isGameOver:
        break

clearTerminal() # NOQA
for j in range(13):
    print()

if not game.thDestroyed and game.percentDamage < 50:
    displayDefeat() # NOQA
else:
    displayVictory() # NOQA
    stars = 0
    if game.thDestroyed:
        stars += 1
    if game.percentDamage == 100:
        stars += 2
    elif game.parcentDamage >= 50:
        stars += 1
    print("Stars:", stars)
