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
        self.died = False
        self.portal_created = False

    def set_speedX(self, direction):
        self.speedX = 4 * direction

    def set_speedY(self, direction):
        self.speedY = 4 * direction

    def check_wall_collision(self):
        if pygame.sprite.spritecollide(player, wall_group, False):
            return True
        else:
            return False

    def check_enemy_collision(self):
        if pygame.sprite.spritecollide(player,enemy_group, True):
            player.health -= random.randint(17,30)
            self.keys += 1
            if player.health <= 0:
                self.health = 0
                self.died = True

    def check_portal_collision(self):
        if pygame.sprite.spritecollide(player, portal_group, False):
            game_state.level += 1
            self.keys = 0

    def make_portal(self):
        x_coordinate = (size[0] // 25) * 23
        y_coordinate = (size[1] // 25) * 23
        portal = Portal(x_coordinate,y_coordinate)
        all_sprites_group.add(portal)
        portal_group.add(portal)
        self.portal_created = True

     
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

        self.check_enemy_collision()

        if self.portal_created == True:
            self.check_portal_collision()
            
        if self.keys == 4 and self.portal_created == False:
            self.make_portal()

        

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

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([(size[0]//25),(size[0]//25)])
        self.image.fill(VIOLET)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Maps():
    def __init__(self):
        self.maps = ["level_1.txt","level_2.txt"]
        self.current_map = []

    def get_next_map(self):
        self.current_map = []
        file = open(self.maps[game_state.level - 1], "r")
        for line in file:
            self.current_map.append(line)
        file.close()
    
class GameState():
    def __init__(self):
        self.state = "main_game"
        self.done = False
        self.level = 1
        self.prev_level = 0

    def update_state(self):
        if self.level != self.prev_level:
            map_manager.get_next_map()
            setup(map_manager.current_map)
            self.prev_level = self.level
        if player.died == True:
            self.state = "game_over"

    def state_manager(self):
        self.update_state()
        if self.state == "main_game":
            self.main_game()
        elif self.state == "game_over":
            self.game_over()
            
    def main_game(self):  
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

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

        pygame.display.flip()
        
    def game_over(self):
        screen.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Game Over",True,WHITE)
        screen.blit(text, (0,0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        
    

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

player = Player(0,0,WHITE,24)

def setup(game_map):
    #Initialise Sprites and Add To Groups
    global all_sprites_group, wall_group, enemy_group, portal_group
    all_sprites_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()

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
    enemy_colour = random.choice([ORANGE, YELLOW, GREEN, BLUE, INDIGO])
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
                    player.rect.x = x_coordinate
                    player.rect.y = y_coordinate
                    all_sprites_group.add(player)

                elif game_map[y][x] == '+':
                    inner_wall = Wall(x_coordinate,y_coordinate,(size[0]//25))
                    all_sprites_group.add(inner_wall)
                    wall_group.add(inner_wall)
                    
                elif game_map[y][x] == 'E':
                    enemy = Enemy(x_coordinate,y_coordinate,24, 100, enemy_colour)
                    all_sprites_group.add(enemy)
                    enemy_group.add(enemy)

map_manager = Maps()

### -- Game Loop
game_state = GameState()

while not game_state.done:

        game_state.state_manager()
        
         # - The clock ticks over
        clock.tick(60)
    
#End While - End of game loop
    
pygame.quit()


