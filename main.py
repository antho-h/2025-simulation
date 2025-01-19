import pygame
from bot import BotManager
from field import Field as Field
from config import GAME_SCALE as SC
from buttons import Button, Switch, Slider
from obstacle import Obstacle, ObstacleManager


def handleBotSelection(event ):
    pass


def loop():
    global running
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handleBotSelection(event)
        BotManager.handleEvent(event)
        ObstacleManager.handleEvent(event)

    screen.fill((255, 255, 255))

    field.draw(screen)
    BotManager.draw(screen)
    ObstacleManager.draw(screen)


    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 900))



    field = Field(100,0)
    BotManager.init()




    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        loop()

    pygame.quit()