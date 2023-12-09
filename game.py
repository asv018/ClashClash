from src.characters import Barbarians, Archer, Balloons  # NOQA
from src.kingClass import *  # NOQA
from src.building import Castle, TownHall, Hut, Wall, Cannon, WizardTower
from src.gameSetting import Game
from src.input import input_to, Get
from src.utilities import *  # NOQA
from src.init import *  # NOQA
from time import sleep
from colorama import init, Fore

# import subprocess
init(autoreset=False)


# proc = subprocess.Popen(["mpg123", "--loop", "10", "sounds/bgmGame.mp3"])

for i in range(5):
    clearTerminal()  # NOQA
    for j in range(13):
        print()
    if (i % 2 == 0):
        print(Fore.RED)
    else:
        print(Fore.GREEN)
    printTitleScreen()  # NOQA
    print(Fore.WHITE)
    # sleep(0.5)
# keyPresses = []

for levelNum in range(3):
    clearTerminal()  # NOQA
    heroType = -1
    while heroType < 1 or heroType > 2:
        print(Fore.WHITE)
        print("1. King")
        print("2. Queen")
        print(Fore.WHITE)
        inputString = input("Choose your hero:")
        heroType = -1
        if "1" in inputString:
            heroType = 1
        if "2" in inputString and heroType == -1:
            heroType = 2
        elif heroType == 1 and "2" in inputString:
            heroType = -1
        clearTerminal()  # NOQA
    gameHeight = 40
    gameWidth = 150
    layout = initializeLayout(gameHeight=gameHeight, gameWidth=gameWidth)  # NOQA
    getText = Get()

    # castle structure
    castleDesign = [" _   |~  _ ", "[_]--'--[_]", "|'|\"\"`\"\"|'|", r"| | /^\ | |", "|_|_|I|_|_|"]  # NOQA
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

    buildings = [castleObject, castleObject2, townhallObject, hutObject, hutObject2, hutObject3]  # NOQA

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
    queenDesign = ["|\\_/|", " |_| ", "/ | \\", "_/ \\_"]
    king = []

    balloonDesign = ["[B]"]
    archerDesign = ["[A]"]

    cannonDesign = ["  /\\  ", " /  \\ ", " |  | ", " |  | ", "/ == \\", "|/**\\|"]  # NOQA
    cannonObject1 = Cannon(100, 20, 90, cannonDesign, len(buildings), 25)
    buildings.append(cannonObject1)
    cannonObject2 = Cannon(100, 20, 40, cannonDesign, len(buildings), 25)
    buildings.append(cannonObject2)
    cannonObject3 = Cannon(100, 28, 40, cannonDesign, len(buildings), 25)
    cannonObject4 = Cannon(100, 28, 110, cannonDesign, len(buildings), 25)

    wizardDesign = ["...", ".W.", "..."]
    wizardObject1 = WizardTower(100, 10, 125, wizardDesign, len(buildings), 25)
    buildings.append(wizardObject1)
    wizardObject2 = WizardTower(100, 25, 20, wizardDesign, len(buildings), 25)
    buildings.append(wizardObject2)
    wizardObject3 = WizardTower(100, 15, 40, wizardDesign, len(buildings), 25)
    wizardObject4 = WizardTower(100, 20, 120, wizardDesign, len(buildings), 25)

    if levelNum >= 1:
        buildings.append(cannonObject3)
        buildings.append(wizardObject3)
    if levelNum >= 2:
        buildings.append(cannonObject4)
        buildings.append(wizardObject4)
    iterationNumber = 0
    lastSpecial = -1
    lastX = 0
    lastY = 0
    lastDir = 0
    lastH = 0
    lastW = 0
    lastDamage = 0
    while 1:
        # checking basics
        iterationNumber += 1
        enteredText = input_to(getch=getText)  # NOQA
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
        # if enteredText is not None:
        #     keyPresses.extend([iterationNumber, enteredText])
        percentDamage = countDestroyed//countTotal
        percentDamage *= 100
        game.percentDamage = percentDamage
        layout = initializeLayout(gameHeight=gameHeight, gameWidth=gameWidth)  # NOQA
        clearTerminal()  # NOQA

        # NOQA
        # checking key presses

        # Barbarians spawning
        if enteredText == "z" and game.barbarians > 0:
            tempBarb = Barbarians(100, 10, 10, characterDesign)  # NOQA
            characters.append(tempBarb)
            game.spawnBarbarians()

        if enteredText == "x" and game.barbarians > 0:
            tempBarb = Barbarians(100, 10, 110, characterDesign)  # NOQA
            characters.append(tempBarb)
            game.spawnBarbarians()

        if enteredText == "c" and game.barbarians > 0:
            tempBarb = Barbarians(100, 30, 100, characterDesign)  # NOQA
            characters.append(tempBarb)
            game.spawnBarbarians()

        # Archer spawning
        if enteredText == "v" and game.archers > 0:
            tempArcher = Archer(50, 10, 10, archerDesign, 20)  # NOQA
            characters.append(tempArcher)
            game.spawnArchers()

        if enteredText == "b" and game.archers > 0:
            tempArcher = Archer(50, 10, 110, archerDesign, 20)  # NOQA
            characters.append(tempArcher)
            game.spawnArchers()

        if enteredText == "n" and game.archers > 0:
            tempArcher = Archer(50, 30, 100, archerDesign, 20)  # NOQA
            characters.append(tempArcher)
            game.spawnArchers()

        # Balloons spawning
        if enteredText == "4" and game.balloons > 0:
            tempBalloon = Balloons(100, 10, 10, balloonDesign)  # NOQA
            characters.append(tempBalloon)
            game.spawnBalloons()

        if enteredText == "5" and game.balloons > 0:
            tempBalloon = Balloons(100, 10, 110, balloonDesign)  # NOQA
            characters.append(tempBalloon)
            game.spawnBalloons()

        if enteredText == "6" and game.balloons > 0:
            tempBalloon = Balloons(100, 30, 100, balloonDesign)  # NOQA
            characters.append(tempBalloon)
            game.spawnBalloons()

        # King Spawning
        if enteredText == "1" and game.king > 0:
            if heroType == 1:
                kingObject = King(400, 10, 10, kingDesign, gameHeight, gameWidth)  # NOQA
            else:
                kingObject = Queen(300, 10, 10, queenDesign, gameHeight, gameWidth)  # NOQA
            king.append(kingObject)
            characters.append(kingObject)
            game.spawnKing()

        if enteredText == "2" and game.king > 0:
            if heroType == 1:
                kingObject = King(400, 10, 110, kingDesign, gameHeight, gameWidth)  # NOQA
            else:
                kingObject = Queen(300, 10, 110, queenDesign, gameHeight, gameWidth)  # NOQA
            king.append(kingObject)
            characters.append(kingObject)
            game.spawnKing()

        if enteredText == "3" and game.king > 0:
            if heroType == 1:
                kingObject = King(400, 30, 100, kingDesign, gameHeight, gameWidth)  # NOQA
            else:
                kingObject = Queen(300, 10, 110, queenDesign, gameHeight, gameWidth)  # NOQA
            king.append(kingObject)
            characters.append(kingObject)
            game.spawnKing()

        if enteredText == "w":
            for k in king:
                k.move(-1, 0, buildings)
                if game.rageSpell:
                    k.move(-1, 0, buildings)
                if heroType == 2:
                    k.attackDirection = 0
        elif enteredText == "d":
            for k in king:
                k.move(0, 1, buildings)
                if game.rageSpell:
                    k.move(0, 1, buildings)
                if heroType == 2:
                    k.attackDirection = 3
        elif enteredText == "a":
            for k in king:
                k.move(0, -1, buildings)
                if game.rageSpell:
                    k.move(0, -1, buildings)
                if heroType == 2:
                    k.attackDirection = 2
        elif enteredText == "s":
            for k in king:
                k.move(1, 0, buildings)
                if game.rageSpell:
                    k.move(1, 0, buildings)
                if heroType == 2:
                    k.attackDirection = 1
        if heroType == 1:
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
        if heroType == 2:
            if enteredText == " ":
                for k in king:
                    k.attack(buildings)
                    if game.rageSpell:
                        k.attack(buildings)
            if enteredText == "m":
                if lastSpecial == -1:
                    lastSpecial = iterationNumber
                    for k in king:
                        lastX = k.startX
                        lastY = k.startY
                        lastDir = k.attackDirection
                        lastH = k.height
                        lastW = k.width
                        lastDamage = k.damage

        elif enteredText == "h":
            for character in characters:
                character.health = min(100, character.health*1.5)
        elif enteredText == "r":
            game.rageSpell = True
        # NOQA
        if heroType == 2 and lastSpecial + 30 == iterationNumber and lastSpecial != -1:  # NOQA
            for k in king:
                k.specialAttack(buildings, lastDir, lastX, lastY, lastH, lastW, lastDamage)  # NOQA
            lastSpecial = -1
        if not cannonObject1.isDestroyed:
            cannonObject1.attack(characters)
        if not cannonObject2.isDestroyed:
            cannonObject2.attack(characters)
        if levelNum >= 1 and not cannonObject3.isDestroyed:
            cannonObject3.attack(characters)
        if levelNum >= 2 and not cannonObject4.isDestroyed:
            cannonObject4.attack(characters)

        if not wizardObject1.isDestroyed:
            wizardObject1.attack(characters)
        if not wizardObject2.isDestroyed:
            wizardObject2.attack(characters)
        if levelNum >= 1 and not wizardObject3.isDestroyed:
            wizardObject3.attack(characters)
        if levelNum >= 2 and not wizardObject4.isDestroyed:
            wizardObject4.attack(characters)

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

        if not cannonObject3.isDestroyed and levelNum >= 1:
            cannonObject3.displayBuilding(layout)

        if not cannonObject4.isDestroyed and levelNum >= 2:
            cannonObject4.displayBuilding(layout)

        if not wizardObject1.isDestroyed:
            wizardObject1.displayBuilding(layout)

        if not wizardObject2.isDestroyed:
            wizardObject2.displayBuilding(layout)

        if not wizardObject3.isDestroyed and levelNum >= 1:
            wizardObject3.displayBuilding(layout)

        if not wizardObject4.isDestroyed and levelNum >= 2:
            wizardObject4.displayBuilding(layout)

        countAlive = 0
        for character in characters:
            if character.isDestroyed:
                countAlive += 1
            if not character.isKing and not character.isDestroyed:
                character.displayCharacter(layout)
        if countAlive == len(characters) and game.barbarians == 0 and game.king == 0 and game.archers == 0 and game.balloons == 0:  # NOQA
            game.isGameOver = True
        printGame(layout)  # NOQA
        sleep(0.02)
        if (enteredText == 'q'):
            break

        if game.isGameOver:
            break

    clearTerminal()  # NOQA
    for j in range(13):
        print()

    if not game.thDestroyed and game.percentDamage < 50:
        displayDefeat()  # NOQA
        print(Fore.WHITE)
        sleep(2)
        break
    else:
        displayVictory()  # NOQA
        stars = 0
        if game.thDestroyed:
            stars += 1
        if game.percentDamage == 100:
            stars += 2
        elif game.percentDamage >= 50:
            stars += 1
        print("Stars:", stars)
        print(Fore.WHITE)
        for c in characters:
            c.__del__()
        for b in buildings:
            b.__del__()
        sleep(2)

# currTime = datetime.now()
# fileName = "replays/" + str(currTime) + ".txt"
# with open(fileName, 'w') as f:
    # for keyPress in keyPresses:
    #     f.write("%s\n" % keyPress)
print(Fore.WHITE)

# proc.terminate()
