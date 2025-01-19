from vector import Vector
import pygame

class vectorVisual:
    @staticmethod
    def draw(op: Vector,v: Vector,color,screen):
        pygame.draw.line(screen, color, (op.x, op.y), (op.x + v.x, op.y + v.y), 2)
        pygame.draw.circle(screen, color, (op.x + v.x, op.y + v.y), 5)