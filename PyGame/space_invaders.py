### SRC - This looks really good.
### I've made a small comment below...

import pygame, random, math
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Snow")


## -- Define the class invader which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randint(-50,0)
        # Set speed
        self.speed = speed
    #End Procedure
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed

#End Class

class Player(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = size[0]//2
        self.rect.y = size[1] - height
        # Set speed
        self.speed = 0
    #End Procedure

    def player_set_speed(self,val):
        self.speed = val

    def update(self):
        if 0 <(self.rect.x + self.speed)< (size[0]-10):
            self.rect.x = self.rect.x + self.speed

# -- Exit game flag set to false
done = False

# Create a list of the snow blocks
invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# Create the snow
number_of_invaders = 10 # we are creating 50 invaders
for x in range(number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
    invader_group.add(my_invader) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add(my_invader) # adds it to the group of all Sprites
#Next x

player = Player(YELLOW,10,10)
all_sprites_group.add(player)
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
        elif event.type == pygame.KEYDOWN: # - a key is down
            if event.key == pygame.K_LEFT: # - if the left key pressed
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
        elif event.type == pygame.KEYUP: # - a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0) # speed set to 0

    # -- Game logic goes after this comment
    # -- when invader hits the player add 5 to score.
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)

    
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

