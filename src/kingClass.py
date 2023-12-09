from .characters import Character
from .utilities import checkCollision


def kingAttackDamage(x, y, buildings, damage):
    for i in range(len(buildings)):
        if not buildings[i].isDestroyed:
            if checkCollision(x, y, 1, 1, buildings[i].startX, buildings[i].startY, buildings[i].height, buildings[i].width): # NOQA
                buildings[i].health -= damage
                if buildings[i].health <= 0:
                    buildings[i].isDestroyed = True
                    return True


def queenAttackDamage(x, y, buildings, damage, field):
    for i in range(len(buildings)):
        if not buildings[i].isDestroyed:
            if checkCollision(x, y, field, field, buildings[i].startX, buildings[i].startY, buildings[i].height, buildings[i].width): # NOQA
                buildings[i].health -= damage
                if buildings[i].health <= 0:
                    buildings[i].isDestroyed = True


class King(Character):
    def __init__(self, health, startX, startY, design, maxHeight, maxWidth):
        super().__init__(health, startX, startY, design)
        self.target = -1
        self.isKing = True
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        self.damage = 12

    def move(self, deltaX, deltaY, buildings):
        newX = self.startX + deltaX
        newY = self.startY + deltaY
        newX = max(1, min(newX, self.maxHeight - 1 - self.height))
        newY = max(1, min(newY, self.maxWidth - 1 - self.width))
        for building in buildings:
            if not building.isDestroyed:
                if checkCollision(newX, newY, self.height, self.width, building.startX, building.startY, building.height, building.width): # NOQA
                    return
        self.startX = newX
        self.startY = newY

    def attack(self, buildings, attackDirection):
        # up
        if attackDirection == 0:
            kingAttackDamage(self.startX - 1, self.startY + 3, buildings, self.damage) # NOQA
        # down
        elif attackDirection == 1:
            kingAttackDamage(self.startX + self.height, self.startY + 3, buildings, self.damage) # NOQA
        # left
        elif attackDirection == 2:
            kingAttackDamage(self.startX + 2, self.startY - 1, buildings, self.damage) # NOQA
        # right
        elif attackDirection == 3:
            kingAttackDamage(self.startX + 2, self.startY + self.width, buildings, self.damage) # NOQA


class Queen(Character):
    def __init__(self, health, startX, startY, design, maxHeight, maxWidth):
        super().__init__(health, startX, startY, design)
        self.target = -1
        self.isKing = True
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        self.attackDirection = 3
        self.movementSpeed = 2
        self.damage = 10

    def move(self, deltaX, deltaY, buildings):
        for movements in range(self.movementSpeed):
            newX = self.startX + deltaX
            newY = self.startY + deltaY
            newX = max(1, min(newX, self.maxHeight - 1 - self.height))
            newY = max(1, min(newY, self.maxWidth - 1 - self.width))
            for building in buildings:
                if not building.isDestroyed:
                    if checkCollision(newX, newY, self.height, self.width, building.startX, building.startY, building.height, building.width): # NOQA
                        return
            self.startX = newX
            self.startY = newY

    def attack(self, buildings):
        attackDirection = self.attackDirection
        centreX = self.startX + self.height // 2
        centreY = self.startY + self.width // 2
        # up
        if attackDirection == 0:
            queenAttackDamage(self.startX - 10, centreY - 2, buildings, self.damage, 5) # NOQA
        # down
        elif attackDirection == 1:
            queenAttackDamage(self.startX + self.height + 6, centreY - 2, buildings, self.damage, 5) # NOQA
        # left
        elif attackDirection == 2:
            queenAttackDamage(centreX - 2, self.startY - 10, buildings, self.damage, 5) # NOQA
        # right
        elif attackDirection == 3:
            queenAttackDamage(centreX - 2, self.startY + self.width + 6, buildings, self.damage, 5) # NOQA

    def specialAttack(self, buildings, attackDirection, startX, startY, height, width, damage): # NOQA
        attackDirection = attackDirection
        centreX = startX + height // 2
        centreY = startY + width // 2
        damage = 1.5 * damage
        # up
        if attackDirection == 0:
            queenAttackDamage(startX - 20, centreY - 4, buildings, damage, 9) # NOQA
        # down
        elif attackDirection == 1:
            queenAttackDamage(startX + height + 12, centreY - 4, buildings, damage, 9) # NOQA
        # left
        elif attackDirection == 2:
            queenAttackDamage(centreX - 4, startY - 20, buildings, damage, 9) # NOQA
        # right
        elif attackDirection == 3:
            queenAttackDamage(centreX - 4, startY + width + 12, buildings, damage, 9) # NOQA