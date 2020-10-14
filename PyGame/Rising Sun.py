import pygame, time
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Rising Sun")
# -- Exit game flag set to false
done = False
sun_x = 0
sun_y = 100
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    # -- Game logic goes after this comment
    # -- Screen background is BLUE
    if 160<sun_x < 480:
        screen.fill((67, 126, 230))
    else:
        screen.fill((19, 59, 128))
        
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,330,200,150))
    pygame.draw.rect(screen, (189, 191, 187), (250,380,60,60))
    pygame.draw.rect(screen, (105, 88, 42), (340,380,50,100))
    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)
    pygame.draw.polygon(screen, BLACK, ((200,330),(320,250),(440,330)))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
    if sun_x > 640:
        time.sleep(3)
        sun_x=0
        sun_y=100
    else:
        sun_x = sun_x + 1
        sun_y = int((3/5120)*sun_x**2 - (3/8)*sun_x + 100)

#End While - End of game loop
pygame.quit()
