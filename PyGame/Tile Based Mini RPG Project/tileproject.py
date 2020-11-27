#MINI PROJECT

#IMPORTS
import pygame, random

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
        self.money = 0
        self.health = 100
        self.keys = 0
        self.score = 0

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, health, colour):
        super().__init__()
        self.image = pygame.Surface([width,width])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

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
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
INDIGO = (75,0,130)
VIOLET = (238, 130, 238)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (600,600)
screen_size = (size[0],size[1]+50)
screen = pygame.display.set_mode(screen_size)

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
            "#  +0+      +  +        #",
            "# +000+     +  +        #",
            "#  +0+      +  +        #",
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
            "#        +  +      +0+  #",
            "#        +  +     +000+ #",
            "#        +  +      +0+  #",
            "#        +  +       +   #",
            "#           +           #",
            "#########################",]
#0 represents a blank spot that should not be filled

#Initialise Sprites and Add To Groups
all_sprites_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

enemy_count = 0
while enemy_count < 4:
    i = random.randint(0,24)
    j = random.randint(0,24)
    if game_map[j][i] == ' ':
        temp = list(game_map[j])
        temp[i] = "E"
        game_map[j] = temp
        enemy_count += 1


#generate sprites and add to groups
enemy_colour = random.choice([ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET])
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
                player = Player(x_coordinate,y_coordinate,WHITE,24)
                all_sprites_group.add(player)

            elif game_map[y][x] == '+':
                inner_wall = Wall(x_coordinate,y_coordinate,(size[0]//25))
                all_sprites_group.add(inner_wall)
                wall_group.add(inner_wall)
                
            elif game_map[y][x] == 'E':
                enemy = Enemy(x_coordinate,y_coordinate,24, 100, enemy_colour)
                all_sprites_group.add(enemy)          

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
    
    # -- Screen background is BLACK, Draw on Screen
    screen.fill(BLACK)
    all_sprites_group.update()
    all_sprites_group.draw(screen)

    #Text
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(
        "Health: "+str(player.health)+"| Score: "+str(player.score)
        + " | Money: "+ str(player.money)+"| Keys:"+str(player.keys)
        ,True,WHITE)
    screen.blit(text, (0, size[1]+10))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
    
pygame.quit()

