import pygame
from vector import Vector
from vectorVisual import vectorVisual as VV
from config import absoluteGoalVector, fieldVector, middle
from enum import Enum


class logicHandler:
    def __init__(self):

        self.position: Vector = Vector(x=0, y=0)
        self.logicalGoalVector = Vector(x=0, y=0)
        self.logicalPosition = Vector(x=0, y=0)

        self.hasBall: bool = False

    def update(self, x, y):
        self.position.x = x
        self.position.y = y

        self.logicalPosition = self.position - middle
        self.logicalGoalVector = absoluteGoalVector - self.position

    def draw(self, screen):
        k1,k2 = self.calculateKickPossibilities(self.logicalPosition, self.logicalGoalVector)
        VV.draw(self.position, k1, (0, 0, 0), screen)
        VV.draw(self.position, k2, (0, 0, 0), screen)

    def calculateKickPossibilities(self, position, goal):
        leftKick = Vector(x=0, y=0)
        leftKick.x = -fieldVector.x - position.x
        leftScale = leftKick.x / (-fieldVector.x)
        leftKick.y = goal.y / (leftScale + 1) * leftScale
        # v2 = (fieldvector.x; goal.y/(leftScale + 1))

        rightKick = Vector(x=0, y=0)
        rightKick.x = fieldVector.x - position.x
        rightScale = rightKick.x / fieldVector.x
        rightKick.y = goal.y / (rightScale + 1) * rightScale
        # v2 = (-fieldvector.x; goal.y/(leftScale + 1))
        return leftKick, rightKick


    def createRef(self, screen):
        kick1, kick2 = Vector(x=0, y=0), Vector(x=0, y=0)
        kick1.x = -fieldVector.x - self.logicalPosition.x
        print(kick1.x)
        kick2.x = fieldVector.x
        scale = kick1.x / (-kick2.x)
        kick2.y = self.logicalGoalVector.y / (scale + 1)
        kick1.y = kick2.y * scale

        VV.draw(self.position, kick1, (0, 0, 0), screen)
        VV.draw(self.position + kick1, kick2, (0, 0, 0), screen)

        return kick1, kick2
        # kick1, kick2 = Vector(x=0, y=0), Vector(x=0, y=0)
        # kick1.x = fieldVector.x - self.logicalPosition.x
        # kick2.x = -fieldVector.x
        # scale = kick1.x/(-kick2.x)
        # kick2.y = self.logicalGoalVector.y/(scale + 1)
        # kick1.y = kick2.y*scale
        #
        # VV.draw(self.position, kick1, (0, 0, 0), screen)
        # VV.draw(self.position+kick1, kick2, (0, 0, 0), screen)
        #
        #
        # return kick1, kick2




class Path:
    def __init__(self):
        self.ActionList: list[Action] = []
        self.startingPoint: Vector = Vector(x=0, y=0)
        self.score = 0
        a = Action(x=0, y=0)



class Action(Vector):
    def __init__(self, x,y,actionType):
        self.Vector = Vector(x=x,y=y)
        self.type = actionType


class ActionType(Enum):
    DRIVE = 0
    ROTATE = 1
    KICK = 2


if __name__ == "__main__":
    a = Action(1,1, actionType=ActionType.DRIVE)
    print(a.x, a.y, a.type)