import pygame

class Button:
    def __init__(self, x, y, w, h,label):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0,0,0)

        font = pygame.font.SysFont(None, 15)
        self.label = font.render(label, True, (0, 0, 0))
        self.func = None

    def setFunc(self, func):
        self.func = func


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        label_rect = self.label.get_rect(center=self.rect.center)
        screen.blit(self.label, label_rect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            if self.rect.collidepoint(event.pos):
                self.color = (80, 80, 80)
                self.func()
                return True
            else:
                self.color = (0xB4,0xB4,0xB4)
        if event.type == pygame.MOUSEBUTTONUP:
            self.color = (0xB4,0xB4,0xB4)
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = (114,114,114)
            else:
                self.color = (0xB4,0xB4,0xB4)


class Switch:
    def __init__(self, x, y, w, h, label):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0xB4,0xB4,0xB4)

        font = pygame.font.SysFont(None, 15)
        self.label = font.render(label, True, (0, 0, 0))
        self.state = False



    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        label_rect = self.label.get_rect(center=self.rect.center)
        screen.blit(self.label, label_rect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            if self.rect.collidepoint(event.pos):
                self.state = not self.state
                self.color = (80, 80, 80) if self.state else (0xB4,0xB4,0xB4)
                return True

class Slider:
    def __init__(self, x, y, w):
        self.color = (0xB4,0xB4,0xB4)
        self.head = pygame.Rect(x-7, y-7, 14, 14)
        self.bar = pygame.Rect(x, y-1, w, 2)
        self.dragging = False
        self.a = 0
        self.b = 100

    def draw(self, screen):
        pygame.draw.rect(screen, (10,10,10), self.bar)
        pygame.draw.circle(screen, self.color, self.head.center, 7)

    def setScale(self,startValue, endValue):
        self.a = startValue
        self.b = endValue

    def getValue(self):
        return (self.head.centerx - self.bar.x) / self.bar.width * (self.b - self.a) + self.a


    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.head.collidepoint(event.pos):
                    self.color = (80, 80, 80)
                    self.dragging = True
        elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.head.centerx = max(self.bar.x, min(self.bar.x + self.bar.width, event.pos[0]))
        elif event.type == pygame.MOUSEBUTTONUP:
            self.color = (0xB4,0xB4,0xB4)
            self.dragging = False

