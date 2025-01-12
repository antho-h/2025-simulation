import pygame
from config import GAME_SCALE as SC

class Field:
    def __init__(self,x,y):

        self.image = pygame.image.load("img/field.png")
        self.carpet = pygame.Rect(x, y, 577, 764)

    def draw(self, screen):
        screen.blit(self.image, self.carpet)
        # pygame.draw.rect(screen, (255, 0, 0), self.carpet, 1)


