import pygame
from config import GAME_SCALE as SC

class Obstacle:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y), 10*SC)

    def checkCollision(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class ObstacleManager:
    def __init__(self):
        self.placeMode = False
        self.obstacles = []

    def addObstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            self.placeMode = not self.placeMode
        if not self.placeMode:
            return
        if not event.type == pygame.MOUSEBUTTONDOWN:
            return
        removedObstacle = False

        for i in range(0, len(self.obstacles)   ):
            if self.obstacles[i].checkCollision(event):
                removedObstacle = True
                self.obstacles.pop(i)
                break
        if not removedObstacle:
            self.addObstacle(Obstacle(event.pos[0], event.pos[1], 50, 50, (0, 0, 0)))