from .utilities import fillColors, checkCollision
from colorama import init, Fore
init(autoreset=True)


class Character:
    """Class to store the basic structure of all moving characters"""

    def __init__(self, health, startX, startY, design):
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
        self.isAttacking = -1
        self.isKing = False
        self.damage = 5
        self.isAir = False
        self.maxHealth = health

    def setDamage(self, damage):
        self.damage = damage

    def __del__(self):
        pass

    def displayCharacter(self, layout):
        if self.isDestroyed:
            return
        for i in range(self.height):
            for j in range(self.width):
                layout[self.startX + i][self.startY + j] = self.design[i][j]
        self.displayHealth(layout)

    def displayHealth(self, layout):
        if self.health < 0.25 * self.maxHealth:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.RED, layout) # NOQA
        elif self.health < 0.50 * self.maxHealth:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.YELLOW, layout) # NOQA
        elif self.health < 0.75 * self.maxHealth:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.CYAN, layout) # NOQA
        else:
            fillColors(self.startX, self.startY, self.height, self.width, Fore.GREEN, layout) # NOQA


class Barbarians(Character):
    def __init__(self, health, startX, startY, design):
        super().__init__(health, startX, startY, design)
        self.target = -1

    def findTarget(self, buildings, attackDefences=False):
        bestBuilding = -1
        closestDist = 24100*24100
        midPtX1 = self.startX + self.height // 2
        midPtY1 = self.startY + self.width // 2
        for i in range(len(buildings)):
            if attackDefences:
                if not buildings[i].isDefence:
                    continue
            if not buildings[i].isDestroyed and not buildings[i].isWall:
                midPtX2 = buildings[i].startX + buildings[i].height // 2
                midPtY2 = buildings[i].startY + buildings[i].width // 2
                dist = (midPtX1 - midPtX2)**2 + (midPtY1 - midPtY2)**2
                if dist < closestDist:
                    bestBuilding = i
                    closestDist = dist
        self.target = bestBuilding

    def move(self, buildings):
        if self.target == -1:
            self.findTarget(buildings=buildings)
        elif buildings[self.target].isDestroyed:
            self.target = -1
            self.findTarget(buildings=buildings)
        if self.target == -1:
            return
        newX = self.startX
        newY = self.startY
        if buildings[self.target].startX < self.startX:
            newX -= 1
        elif buildings[self.target].startX > self.startX:
            newX += 1
        if buildings[self.target].startY < self.startY:
            newY -= 1
        elif buildings[self.target].startY > self.startY:
            newY += 1

        for building in buildings:
            if not building.isDestroyed:
                if checkCollision(newX, newY, self.height, self.width, building.startX, building.startY, building.height, building.width): # NOQA
                    self.target = building._id
                    building.health -= self.damage
                    if building.health <= 0:
                        building.isDestroyed = True
                        self.target = -1
                    return
            if building.isDestroyed and building._id == self.target:
                self.target = -1
                self.findTarget(buildings=buildings)
        self.startX = newX
        self.startY = newY


class Archer(Barbarians):
    def __init__(self, health, startX, startY, design, range):
        super().__init__(health, startX, startY, design)
        self.range = range
        self.movementSpeed = 2
        self.damage = 2.5

    def move(self, buildings):
        for movements in range(self.movementSpeed):
            if self.target == -1:
                self.findTarget(buildings=buildings)
            elif buildings[self.target].isDestroyed:
                self.target = -1
                self.findTarget(buildings)
            if self.target == -1:
                return
            midPtX1 = self.startX + self.height // 2
            midPtY1 = self.startY + self.width // 2
            midPtX2 = buildings[self.target].startX + buildings[self.target].height // 2 # NOQA
            midPtY2 = buildings[self.target].startY + buildings[self.target].width // 2  # NOQA
            dist = (midPtX1 - midPtX2)**2 + (midPtY1 - midPtY2)**2
            if dist <= self.range**2:
                buildings[self.target].health -= self.damage
                if buildings[self.target].health <= 0:
                    buildings[self.target].isDestroyed = True
                    self.target = -1
                return

            newX = self.startX
            newY = self.startY
            if buildings[self.target].startX < self.startX:
                newX -= 1
            elif buildings[self.target].startX > self.startX:
                newX += 1
            if buildings[self.target].startY < self.startY:
                newY -= 1
            elif buildings[self.target].startY > self.startY:
                newY += 1

            for building in buildings:
                if not building.isDestroyed:
                    if checkCollision(newX, newY, self.height, self.width, building.startX, building.startY, building.height, building.width): # NOQA
                        self.target = building._id
                        building.health -= self.damage
                        if building.health <= 0:
                            building.isDestroyed = True
                            self.target = -1
                        return
                if building.isDestroyed and building._id == self.target:
                    self.target = -1
                    self.findTarget(buildings=buildings)
            self.startX = newX
            self.startY = newY


class Balloons(Barbarians):
    def __init__(self, health, startX, startY, design):
        super().__init__(health, startX, startY, design)
        self.isAir = True
        self.movementSpeed = 2
        self.damage = 10

    def move(self, buildings):
        for movements in range(self.movementSpeed):
            if self.target == -1:
                self.findTarget(buildings=buildings, attackDefences=True)
            elif buildings[self.target].isDestroyed:
                self.target = -1
                self.findTarget(buildings=buildings, attackDefences=True)
            if self.target == -1:
                self.findTarget(buildings=buildings, attackDefences=False)
            if self.target == -1:
                return

            newX = self.startX
            newY = self.startY
            if buildings[self.target].startX < self.startX:
                newX -= 1
            elif buildings[self.target].startX > self.startX:
                newX += 1
            if buildings[self.target].startY < self.startY:
                newY -= 1
            elif buildings[self.target].startY > self.startY:
                newY += 1
            if checkCollision(newX, newY, self.height, self.width, buildings[self.target].startX, buildings[self.target].startY, buildings[self.target].height, buildings[self.target].width): # NOQA
                buildings[self.target].health -= self.damage
                if buildings[self.target].health <= 0:
                    buildings[self.target].isDestroyed = True
                    self.target = -1
            self.startX = newX
            self.startY = newY
            return
