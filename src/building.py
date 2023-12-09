from .utilities import checkCollision, fillColors
from colorama import init, Fore
init(autoreset=True)


class Building:
    """Class to store the basic structure of all buildings"""

    def __init__(self, health, startX, startY, design, buildingNumber):
        maxWidth = 0
        for x in design:
            if len(x) > maxWidth:
                maxWidth = len(x)
        maxWidth += 1
        for i in range(len(design)):
            design[i] = design[i].ljust(maxWidth)
        self.health = health
        self.startX = startX
        self.startY = startY
        self.height = len(design)
        self.width = maxWidth
        self.design = design
        self.isDestroyed = False
        self.isWall = False
        self._id = buildingNumber
        self.isDefence = False

    def __del__(self):
        pass

    def displayBuilding(self, layout):
        if self.health == 0:
            self.isDestroyed = True
        if self.isDestroyed:
            return
        for i in range(self.height):
            for j in range(self.width):
                layout[self.startX + i][self.startY + j] = self.design[i][j]
        self.displayHealth(layout)

    def displayHealth(self, layout):
        if self.health < 25:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.RED, layout) # NOQA
        elif self.health < 50:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.YELLOW, layout) # NOQA
        elif self.health < 75:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.CYAN, layout) # NOQA
        elif self.health <= 100:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.GREEN, layout) # NOQA


class Castle(Building):
    def __init__(self, health, startX, startY, castleDesign, buildingNumber):
        super().__init__(health, startX, startY, castleDesign, buildingNumber) # NOQA


class TownHall(Building):
    def __init__(self, health, startX, startY, townHallDesign, buildingNumber):
        super().__init__(health, startX, startY, townHallDesign, buildingNumber) # NOQA


class Hut(Building):
    def __init__(self, health, startX, startY, townHallDesign, buildingNumber):
        super().__init__(health, startX, startY, townHallDesign, buildingNumber) # NOQA


class Wall(Building):
    def __init__(self, health, startX, startY, wallDesign, buildingNumber):
        super().__init__(health, startX, startY, wallDesign, buildingNumber) # NOQA
        self.isWall = True


class Cannon(Building):
    def __init__(self, health, startX, startY, cannonDesign, buildingNumber, range): # NOQA
        super().__init__(health, startX, startY, cannonDesign, buildingNumber) # NOQA
        self.targetObject = -1
        self.range = range
        self.damage = 2
        self.isDefence = True
        self.attackAir = False

    def setDamage(self, damage):
        self.damage = damage

    def attack(self, character):
        if self.isDestroyed:
            return
        if self.targetObject != -1:
            if character[self.targetObject].isDestroyed:
                self.targetObject = -1
            if (character[self.targetObject].startX - self.startX)**2 + (character[self.targetObject].startY - self.startY)**2 > self.range**2: # NOQA
                self.targetObject = -1
        if self.targetObject == -1:
            for i in range(len(character)):
                if not character[i].isDestroyed:
                    if not self.attackAir and character[i].isAir:
                        continue
                    if (character[i].startX - self.startX)**2 + (character[i].startY - self.startY)**2 <= self.range**2: # NOQA
                        self.targetObject = i
                        break
        if self.targetObject == -1:
            return
        character[self.targetObject].health -= self.damage
        if character[self.targetObject].health <= 0:
            character[self.targetObject].isDestroyed = True
            self.targetObject = -1


class WizardTower(Cannon):
    def __init__(self, health, startX, startY, cannonDesign, buildingNumber, range): # NOQA
        super().__init__(health, startX, startY, cannonDesign, buildingNumber, range) # NOQA
        self.attackAir = True

    def attack(self, character):
        if self.isDestroyed:
            return
        if self.targetObject != -1:
            if character[self.targetObject].isDestroyed:
                self.targetObject = -1
            if (character[self.targetObject].startX - self.startX)**2 + (character[self.targetObject].startY - self.startY)**2 > self.range**2: # NOQA
                self.targetObject = -1
        if self.targetObject == -1:
            for i in range(len(character)):
                if not character[i].isDestroyed:
                    if not self.attackAir and character[i].isAir:
                        continue
                    if (character[i].startX - self.startX)**2 + (character[i].startY - self.startY)**2 <= self.range**2: # NOQA
                        self.targetObject = i
                        break
        if self.targetObject == -1:
            return

        for i in range(len(character)):
            if not character[i].isDestroyed:
                if character[self.targetObject].isAir and not character[i].isAir: # NOQA
                    continue
                if not character[self.targetObject].isAir and character[i].isAir: # NOQA
                    continue
                centerX = character[self.targetObject].startX + character[self.targetObject].height // 2 # NOQA
                centerY = character[self.targetObject].startY + character[self.targetObject].width // 2 # NOQA
                if checkCollision(centerX - 1, centerY - 1, 3, 3, character[i].startX, character[i].startY, character[i].height, character[i].width): # NOQA
                    character[i].health -= self.damage
                    if character[i].health <= 0:
                        character[i].isDestroyed = True

        character[self.targetObject].health -= self.damage
        if character[self.targetObject].health <= 0:
            character[self.targetObject].isDestroyed = True
            self.targetObject = -1
