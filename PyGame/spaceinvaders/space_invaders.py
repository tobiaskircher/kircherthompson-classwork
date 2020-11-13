### SRC - This looks really good.
### I've made a small comment below...

import pygame, random, math
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)


# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)

screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")


## -- Define the class invader which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for invader
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
    # Define the constructor for player
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 321 
        self.rect.y = size[1] - height
        # Set speed
        self.speed = 0
        #set lives
        self.lives = 5
        #bullets
        self.bullet_count = 50
        #score
        self.score = 0
    #End Procedure

    def bullet_fired(self):
        self.bullet_count -= 1

    def player_set_speed(self,val):
        self.speed = val

    def update(self):
        if 0 <=(self.rect.x + self.speed)<= (size[0]-10):
            self.rect.x = self.rect.x + self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([2,2])
        self.image.fill(RED)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate 
        self.rect.y = y_coordinate
        # Set speed
        self.speed = 2

    def update(self):
        self.rect.y -= self.speed
        
#endclass
    
# -- Exit game flag set to false
done = False

# Create groups
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# Create the invaders
number_of_invaders = 10 # we are creating 50 invaders
for x in range(number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1) # invaders are blue with size 10 by 10 px
    invader_group.add(my_invader) # adds the new invader to the group of invaders
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
                
            elif event.key == pygame.K_UP: # - if the up key pressed
                if player.bullet_count > 0:
                    player.bullet_fired() # remove 1 from bullet count
                    new_bullet = Bullet((player.rect.x + 5),player.rect.y)
                    bullet_group.add(new_bullet)
                    all_sprites_group.add(new_bullet)
                
        elif event.type == pygame.KEYUP: # - a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0) # speed set to 0

    # -- Game logic goes after this comment
    
    # -- remove life when player is hit
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for bullet in bullet_group:
        bullet_hit_group = pygame.sprite.spritecollide(bullet,invader_group,True)
        for foo in bullet_hit_group:
            player.score+=5
        
    all_sprites_group.update()

    for foo in player_hit_group:
        player.lives -= 1

        
    # -- Screen background is BLACK
    screen.fill (BLACK)
    all_sprites_group.draw(screen)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 20, True, False)
    livestext = font.render("Lives: "+str(player.lives),True,WHITE)
    screen.blit(livestext, (0, 0))
    scoretext = font.render("Score: "+str(player.score),True,WHITE)
    screen.blit(scoretext, (0, 20))
    bullettext = font.render("Bullets: "+str(player.bullet_count),True,WHITE)
    screen.blit(bullettext, (0, 40))
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
     # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

