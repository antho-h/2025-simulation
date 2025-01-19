import pygame
from config import GAME_SCALE as SC

class Obstacle:
    def __init__(self, x, y, r, color):
        self.color = color
        self.circle = pygame.Rect(x - r, y - r, 2*r, 2*r)


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.circle.center, self.circle.width//2)

    def checkCollision(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.circle.collidepoint(event.pos):
                return True
        return False

class ObstacleManager:
    obstacles = []
    placeMode = False

    @staticmethod
    def addObstacle(obstacle : Obstacle):
        ObstacleManager.obstacles.append(obstacle)

    @staticmethod
    def draw( screen):
        for obstacle in ObstacleManager.obstacles:
            obstacle.draw(screen)

    @staticmethod
    def handleEvent( event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            ObstacleManager.placeMode = not ObstacleManager.placeMode
        if not ObstacleManager.placeMode:
            return
        if not event.type == pygame.MOUSEBUTTONDOWN or not event.button == 1:
            return

        removedObstacle = False
        i = 0
        while i < len(ObstacleManager.obstacles):
            if ObstacleManager.obstacles[i].checkCollision(event):
                ObstacleManager.obstacles.pop(i)
                removedObstacle = True
            else:
                i += 1

        if not removedObstacle:
            ObstacleManager.addObstacle(Obstacle(event.pos[0], event.pos[1], 10*SC, (0, 0, 0)))