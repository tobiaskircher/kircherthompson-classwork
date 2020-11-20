#MINI PROJECT

#IMPORTS
import pygame

#CLASSES

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colour, width):
        super().__init__()
        self.image = pygame.Surface([width,width])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.width = width
        self.rect.x = x
        self.rect.y = y
        self.speedX = 0
        self.speedY = 0

    def set_speedX(self, direction):
        self.speedX = 4 * direction

    def set_speedY(self, direction):
        self.speedY = 4 * direction

    def check_wall_collision(self):
        if pygame.sprite.spritecollide(player, wall_group, False):
            return True
        else:
            return False
     
    def update(self):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        
        self.rect.x = self.rect.x + self.speedX
        if self.check_wall_collision() == True:
            self.rect.x = self.prev_x
            self.speedX = 0
        
        self.rect.y = self. rect.y + self.speedY
        if self.check_wall_collision() == True:
            self.rect.y = self.prev_y
            self.speedY = 0

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface([width,width])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class InnerWall(Wall):
    pass
                    
# COLOURS
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Tile Game")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#MAP 1
#Array of 25 strings, each containing 25 chars 
game_map = ["#########################",
            "#           +           #",
            "#   +       +  +        #",
            "#  + +      +  +        #",
            "# +   +     +  +        #",
            "#  + +      +  +        #",
            "#   +       +  +        #",
            "#           +  +        #",
            "#           +  +        #",
            "#           ++++        #",
            "#        +     +        #",
            "#        +     +        #",
            "#        +  P  +        #",
            "#        +     +        #",
            "#        +     +        #",
            "#        ++++           #",
            "#        +  +           #",
            "#        +  +           #",
            "#        +  +       +   #",
            "#        +  +      + +  #",
            "#        +  +     +   + #",
            "#        +  +      + +  #",
            "#        +  +       +   #",
            "#           +           #",
            "#########################",]

#Initialise Sprites and Add To Groups
all_sprites_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()


for y in range(len(game_map)):
    for x in range(len(game_map[y])):
        if game_map[y][x] != ' ':
            x_coordinate = (size[0] // 25) * x
            y_coordinate = (size[1] // 25) * y
            
            if game_map[y][x] == '#':
                wall = Wall(x_coordinate,y_coordinate,(size[0]//25))
                all_sprites_group.add(wall)
                wall_group.add(wall)
                
            elif game_map[y][x] == "P":
                player = Player(x_coordinate,y_coordinate,WHITE,20)
                all_sprites_group.add(player)

            elif game_map[y][x] == '+':
                inner_wall = Wall(x_coordinate,y_coordinate,(size[0]//25))
                all_sprites_group.add(inner_wall)
                wall_group.add(inner_wall)
            

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.set_speedX(-1)
            elif event.key == pygame.K_RIGHT:
                player.set_speedX(1)
            elif event.key == pygame.K_UP:
                player.set_speedY(-1)
            elif event.key == pygame.K_DOWN:
                player.set_speedY(1)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.set_speedX(0)
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.set_speedY(0)
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    '''if pygame.sprite.spritecollide(player, wall_group, False):
        if player.rect.x < (size[0] // 25):
            player.rect.x = (size[0] // 25) 
            player.set_speedX(0)
            
        elif player.rect.x + player.width > (size[0] // 25) * 24:
            player.rect.x = (size[0] // 25) * 24 - player.width
            player.set_speedX(0)

        elif player.rect.y < (size[1] // 25):
            player.rect.y = (size[1] // 25) 
            player.set_speedY(0)
            
        elif player.rect.y + player.width > (size[1] // 25) * 24:
            player.rect.y = (size[1] // 25) * 24 - player.width
            player.set_speedY(0)         
        

    prev_x = player.rect.x
    prev_y = player.rect.y'''
    # -- Screen background is BLACK
    screen.fill(BLACK)
    all_sprites_group.update()
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
    
pygame.quit()

