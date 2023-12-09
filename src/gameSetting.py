class Game:
    def __init__(self):
        self.isGameOver = False
        self.barbarians = 5
        self.archers = 5
        self.balloons = 2
        self.queen = 1
        self.king = 1
        self.score = 0
        self.thDestroyed = 0
        self.percentDamage = 0
        self.rageSpell = False

    def spawnBarbarians(self):
        self.barbarians = self.barbarians - 1

    def spawnArchers(self):
        self.archers = self.archers - 1

    def spawnBalloons(self):
        self.balloons = self.balloons - 1

    def spawnQueen(self):
        self.queen = self.queen - 1

    def spawnKing(self):
        self.king = self.king - 1

    def increaseScore(self, points):
        self.score = self.score + points
