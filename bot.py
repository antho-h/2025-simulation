import math
from vector import Vector
import pygame
from obstacle import ObstacleManager
from vectorVisual import vectorVisual as VV
from config import GAME_SCALE as SC
from logicHandler import logicHandler
class Bot:
    def __init__(self, name, x, y, radius, color):
        self.logic = logicHandler()
        self.name = name
        self.circle = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.front = pygame.Rect(0, 0, 20,20)

        self.angle = 0
        self.move(x, y)
        self.color = color

        self.isSelected = False
        self.hasBall = False

        font = pygame.font.SysFont(None, 24)
        self.label = font.render(name, True, (255, 0, 0))

    def move(self, x, y):
        angle = self.angle-90
        self.circle.centerx = x
        self.circle.centery = y
        self.front.centerx = x + self.circle.width / 2 * math.cos(angle/180*math.pi)
        self.front.centery = y + self.circle.height / 2 * math.sin(angle/180*math.pi)

    def draw(self, screen):
        self.logic.update(self.circle.centerx, self.circle.centery)
        self.logic.draw(screen)

        pygame.draw.ellipse(screen, self.color, self.circle)
        pygame.draw.ellipse(screen, self.color, self.front)
        label_rect = self.label.get_rect(center=(self.circle.centerx, self.circle.centery))
        screen.blit(self.label, label_rect)
        if self.isSelected:
            pygame.draw.ellipse(screen, (0, 200, 200), self.circle, 3)
        if self.hasBall:
            pygame.draw.ellipse(screen, (0, 100, 100), self.front)



    def handleEvent(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            self.isSelected = False
        if event.type == pygame.MOUSEMOTION:
            if self.isSelected:
                self.move(event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN and self.circle.collidepoint(event.pos):
            if event.button == 4:
                self.angle -= 5
                self.move(self.circle.centerx, self.circle.centery)
            if event.button == 5:
                self.angle += 5
                self.move(self.circle.centerx, self.circle.centery)





class BotManager:
    bot1, bot2 = None, None
    @staticmethod
    def init():
        BotManager.bot1 = Bot("1", 100, 100, 10 * SC, (0, 0, 0))
        BotManager.bot2 = Bot("2", 300, 100, 10 * SC, (0, 0, 0))
        BotManager.bot1.hasBall = True

    @staticmethod
    def draw(screen):
        BotManager.bot1.draw(screen)
        BotManager.bot2.draw(screen)

    @staticmethod
    def handleEvent(event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            BotManager.bot1.hasBall = not BotManager.bot1.hasBall
            BotManager.bot2.hasBall = not BotManager.bot2.hasBall
        if ObstacleManager.placeMode:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if BotManager.bot1.circle.collidepoint(event.pos):
                BotManager.bot1.isSelected = True
            elif BotManager.bot2.circle.collidepoint(event.pos) and event.button == 1:
                BotManager.bot2.isSelected = True




        BotManager.bot1.handleEvent(event)
        BotManager.bot2.handleEvent(event)








