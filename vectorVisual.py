from vector import Vector
from config import middle
import pygame

class vectorVisual:
    @staticmethod
    def draw(op: Vector,v: Vector,color,screen):
        pygame.draw.line(screen, color, (op.x, op.y), (op.x + v.x, op.y + v.y), 2)
        pygame.draw.circle(screen, color, (op.x + v.x, op.y + v.y), 5)

    @staticmethod
    def drawVector(v: Vector, color, screen):
        pygame.draw.line(screen, color, (0,0), (v.x,  v.y), 2)
        pygame.draw.circle(screen, color, (v.x, v.y), 5)