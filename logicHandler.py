from vector import Vector
from enum import Enum
class logicHandler:
    def __init__(self):
        self.position: Vector = Vector(x=0,y=0)
        self.hasBall: bool = False


class Path:
    def __init__(self):
        self.ActionList: list[Action] = []
        self.startingPoint: Vector = Vector(x=0,y=0)
        a = Action(x=0,y=0)



class Action(Vector):
    def __init__(self):
        super()
        self.type = 1


class ActionType(Enum):
    DRIVE = 0
    ROTATE = 1
    KICK = 2