import math

import pygame

class Bot:
    def __init__(self, name, x, y, radius, color):
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

        pygame.draw.ellipse(screen, self.color, self.circle)
        pygame.draw.ellipse(screen, self.color, self.front)
        label_rect = self.label.get_rect(center=(self.circle.centerx, self.circle.centery))
        screen.blit(self.label, label_rect)
        if self.isSelected:
            pygame.draw.ellipse(screen, (0, 200, 200), self.circle, 3)
        if self.hasBall:
            pygame.draw.ellipse(screen, (0, 100, 100), self.front)

    def handleEvent(self, event):
        if not self.isSelected:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2: # middle click
                self.angle = 0
                self.isSelected = False

            if event.button == 4: # scroll up
                self.angle -= 5
            if event.button == 5: # scroll down
                self.angle += 5
            if event.button == 3: # right click
                dx = event.pos[0] - self.circle.centerx
                dy = event.pos[1] - self.circle.centery
                self.angle = math.atan2(dy,dx) * 180 / math.pi + 90
                self.isSelected = False

            self.move(self.circle.centerx, self.circle.centery)

            if event.button == 1: # left click
                self.move(event.pos[0], event.pos[1])
                self.isSelected = False











