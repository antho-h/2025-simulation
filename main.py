import pygame
from bot import Bot
from field import Field as Field
from config import GAME_SCALE as SC
from buttons import Button, Switch, Slider

def handleBotSelection(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        bot1.isSelected = False
        bot2.isSelected = False

    if bot1.isSelected or bot2.isSelected:
        return

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        if bot1.circle.collidepoint(event.pos):
            bot1.isSelected = True
            return
        if bot2.circle.collidepoint(event.pos):
            bot2.isSelected = True


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 900))



    field = Field(100,0)
    bot1 = Bot("1", 100, 100, 10 * SC, (0,0,0))
    bot2 = Bot("2", 300, 100, 10 * SC, (0,0,0))
    bot1.hasBall = True
    s = Slider(800, 100, 100)
    s.setScale(-100, 1000)


    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                bot1.hasBall = not bot1.hasBall
                bot2.hasBall = not bot2.hasBall
            handleBotSelection(event)
            bot1.handleEvent(event)
            bot2.handleEvent(event)
            s.handleEvent(event)


        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Draw the bots
        field.draw(screen)
        bot1.draw(screen)
        bot2.draw(screen)
        s.draw(screen)
        print(s.getValue())


        # Update the display
        pygame.display.flip()

    pygame.quit()