### SRC - This looks really good.
### I've made a small comment below...

import pygame, random, math
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Snow")


## -- Define the class snow which is a sprite
class snow(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed, snow_y_pos):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = snow_y_pos
        # Set sped
        self.speed = speed
    #End Procedure
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 480:
            ### SRC - I would also reset the x value to a random
            ### number to make the effect more random.
            self.rect.y = 0
#End Class

# -- Exit game flag set to false
done = False

# Create a list of the snow blocks
snow_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# Create the snowflakes
number_of_flakes = 50 # we are creating 50 snowflakes
snow_y_positions = random.sample(range(480),number_of_flakes) #no two adjacent snowflakes
for x in range(number_of_flakes):
    my_snow = snow(WHITE, 5, 5, 1, snow_y_positions[x]) # snowflakes are white with size 5 by 5 px
    snow_group.add(my_snow) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add (my_snow) # adds it to the group of all Sprites
#Next x
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
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill (BLACK)
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()
     # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

