#MINI PROJECT

#IMPORTS
import pygame, random

#CLASSES & FUNCTIONS
class PlayerAnimations():
    def __init__(self, size):
        #Images & Animation Attributes
        self.idle = pygame.transform.scale(pygame.image.load("idle.jpg").convert(), (size,size))
        self.run1 = pygame.transform.scale(pygame.image.load("run1.jpg").convert(), (size,size))
        self.run2 = pygame.transform.scale(pygame.image.load("run2.jpg").convert(), (size,size))
        self.run3 = pygame.transform.scale(pygame.image.load("run3.jpg").convert(), (size,size))
        self.run4 = pygame.transform.scale(pygame.image.load("run4.jpg").convert(), (size,size))
        self.run5 = pygame.transform.scale(pygame.image.load("run5.jpg").convert(), (size,size))
        self.run6 = pygame.transform.scale(pygame.image.load("run6.jpg").convert(), (size,size))
        self.run7 = pygame.transform.scale(pygame.image.load("run7.jpg").convert(), (size,size))
        self.run8 = pygame.transform.scale(pygame.image.load("run8.jpg").convert(), (size,size))
        self.current_animation = self.idle
        self.run_noX = -1
        self.run_animationsX = [self.run1, self.run2, self.run3, self.run4, self.run5, self.run6]
        self.run_noY = -1
        self.run_animationsY = [self.idle, self.run7, self.idle, self.run8]
    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colour, width):
        super().__init__()
        PlayerAnimations.__init__(self, width)

        #Attributes
        self.image = pygame.Surface([width,width])
        self.image = self.current_animation
        self.rect = self.image.get_rect()
        self.width = width
        self.rect.x = x
        self.rect.y = y
        self.speedX = 0
        self.speedY = 0
        self.health = 100
        self.keys = 0
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
            player.health -= random.randint(1,15)
            self.keys += 1
            if player.health <= 0:
                self.health = 0
                self.died = True

    def check_portal_collision(self):
        if pygame.sprite.spritecollide(player, portal_group, False):
            game_state.level += 1
            self.keys = 0
            self.portal_created = False

    def make_portal(self):
        x_coordinate = (size[0] // 25) * 23
        y_coordinate = (size[1] // 25) * 23
        portal = Portal(x_coordinate,y_coordinate)
        all_sprites_group.add(portal)
        portal_group.add(portal)
        self.portal_created = True

     
    def update(self):   
        #Animation
        if self.speedX != 0:
            self.run_noX += 1
            if self.run_noX == 12:
                self.run_noX = 0
            self.current_animation = self.run_animationsX[self.run_noX//2]
            #12 and //2 to make animation slower ie 2 moves before animation update
            if self.speedX < 0:
                self.current_animation = pygame.transform.flip(self.current_animation, True, False)
  
        elif self.speedY != 0:
            self.run_noY += 1
            if self.run_noY == 15:
                self.run_noY = 0
                
            self.current_animation = self.run_animationsY[self.run_noY//4]
            
        elif self.speedX == 0:
            player.current_animation = player.idle
            player.run_noX = -1

        elif self.speedY == 0:
            player.current_animation = player.idle
            player.run_noY = -1

        self.image = self.current_animation

        #Movement
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

        #Enemies
        self.check_enemy_collision()

        #Portal 
        if self.portal_created == True:
            self.check_portal_collision()
            
        if self.keys == 4 and self.portal_created == False:
            self.make_portal()

        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,direction):
        #1= up, 2=right, 3=down, 4=left
        super().__init__() 
        self.image = pygame.Surface([5,5])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if direction == 1 or direction == 4:
            self.speed = -4
        else:
            self.speed = 4
        if direction == 1 or direction == 3:
            self.axis = "y"
        else:
            self.axis = "x"
            
     
    def update(self):
        if self.axis == "x":
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed
        if pygame.sprite.spritecollide(player,bullet_group, True):
            player.died = True
        
        
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__() 
        self.image = pygame.Surface([width,width])
        self.image = pygame.transform.scale(pygame.image.load("enemy_idle.jpg").convert(), (size[0]//25,size[0]//25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bulletsX = 1
        self.bulletsY = 1

    def update(self):
        if self.rect.center[0] == player.rect.center[0] or self.rect.center[1] == player.rect.center[1]:
            line = (self.rect.center, player.rect.center)
            self.shoot = True
            for wall in wall_group:
                if wall.rect.clipline(line):
                    self.shoot = False
            if self.rect.center[0] == player.rect.center[0]:        
                if self.shoot == True & self.bulletsY > 0:
                    self.bulletsY -= 1
                    if self.rect.center[1] > player.rect.center[1]:
                        bullet = Bullet(self.rect.center[0],self.rect.center[1],1)
                    else:
                        bullet = Bullet(self.rect.center[0],self.rect.center[1],3)
                        
                    all_sprites_group.add(bullet)
                    bullet_group.add(bullet)
            else:
                if self.shoot == True & self.bulletsX > 0:
                    self.bulletsX -= 1
                    if self.rect.center[0] > player.rect.center[0]:
                        bullet = Bullet(self.rect.center[0],self.rect.center[1],4)
                    else:
                        bullet = Bullet(self.rect.center[0],self.rect.center[1],2)
                        
                    all_sprites_group.add(bullet)
                    bullet_group.add(bullet)
                


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface([width,width])
        self.image = pygame.transform.scale(pygame.image.load("outer_wall.jpg").convert(), (size[0]//25,size[0]//25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if pygame.sprite.spritecollide(self,bullet_group, True):
            pass
        

class InnerWall(Wall):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("inner_wall.jpg").convert(), (size[0]//25,size[0]//25))

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([(size[0]//25),(size[0]//25)])
        self.image = pygame.transform.scale(pygame.image.load("portal.jpg").convert(), (tilesize,tilesize))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Maps():
    def __init__(self):
        self.current_map = []

    def next_map(self):
        self.current_map = []
        try:
            self.file_name = "level_" + str(game_state.level) + ".txt"
            file = open(self.file_name, "r")
            for line in file:
                self.current_map.append(line)
            file.close()
            setup(map_manager.current_map)
        except:
            game_state.is_game_completed = True

class UI():
    def draw_text(self,font_text,font_size,x,y):
        #Centered Text
        font = pygame.font.SysFont('Calibri', font_size, True, False)
        text = font.render(font_text,True,WHITE)
        text_rect = text.get_rect(center=(size[0]/2, y+ text.get_rect().height / 2))
        screen.blit(text, text_rect)

    def draw_image(self, file_name, size_x, size_y, x, y):
        self.image = pygame.Surface([size_x,size_y])
        self.image = pygame.transform.scale(pygame.image.load(file_name).convert(), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2
        screen.blit(self.image, (self.rect.x, self.rect.y))

class MenuAnim(pygame.sprite.Sprite):
    def __init__(self, file_name, size_x, size_y, x, y):
        super().__init__()
        PlayerAnimations.__init__(self,size_x)
        self.image = pygame.Surface([size_x,size_y])
        self.image = pygame.transform.scale(pygame.image.load(file_name).convert(), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2

    def draw(self):
        self.run_noX += 1
        if self.run_noX == 24:
            self.run_noX = 0
        self.image = self.run_animationsX[self.run_noX//4]
            
        screen.blit(self.image, (self.rect.x, self.rect.y))

    
        
class GameState():
    def __init__(self):
        self.state = "game_menu"
        self.done = False
        self.level = 1
        self.prev_level = 0
        self.is_game_completed = False
        self.menu_player = MenuAnim("idle.jpg",300,300,320,320)
        self.ku, self.kd, self.kr, self.kl = 0,0,0,0

    def update_state(self):
        if self.level != self.prev_level:
            map_manager.next_map()            
            self.prev_level = self.level
        if player.died:
            self.state = "game_over"
        elif self.is_game_completed:
            self.state = "game_completed"

    def state_manager(self):
        self.update_state()
        if self.state == "main_game":
            self.main_game()
        elif self.state == "game_over":
            self.game_over()
        elif self.state == "game_completed":
            self.game_completed()
        elif self.state == "game_menu":
            self.menu()

    def menu(self):
        screen.fill(BLACK)
        ui.draw_text("Stickman Escape",50,0,0)
        ui.draw_text("Click Anywhere To Start!",25,0,size[1])
        
        self.menu_player.draw()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
                
    def main_game(self):  
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True                    
            #End If
        #Next event
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]) or (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            player.set_speedX(0)
        elif keys[pygame.K_LEFT]:
             player.set_speedX(-1)
        elif keys[pygame.K_RIGHT]:
             player.set_speedX(1)
             
        if (keys[pygame.K_UP] and keys[pygame.K_DOWN]) or (not keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
            player.set_speedY(0)
        elif keys[pygame.K_UP]:
             player.set_speedY(-1)
        elif keys[pygame.K_DOWN]:
             player.set_speedY(1)

                
        # -- Game logic goes after this comment
        
        # -- Screen background is BLACK, Draw on Screen
        screen.fill(BLACK)
        all_sprites_group.update()
        all_sprites_group.draw(screen)

        #Text
        ui.draw_text("Health: "+str(player.health)+
                     "| Keys: "+str(player.keys) +" | Level: " +
                     str(game_state.level),25,0,size[1]+10)

        pygame.display.flip()
        
    def game_over(self):
        screen.fill(BLACK)
        ui.draw_text("Game Over",50,0,0)
        ui.draw_text("Click Anywhere To Restart!",25,0,size[1]+10)
        ui.draw_image("player_lose.jpg",300,300,320,320)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
                player.health = 100
                player.keys = 0
                self.level = 1
                self.prev_level = 0
                self.is_game_completed = False
                player.speedX = 0
                player.speedY = 0
                player.died = False
                

    def game_completed(self):
        screen.fill(BLACK)
        ui.draw_text("Game Completed",50,0,0)
        ui.draw_text("Click Anywhere To Play Again!",25,0,size[1]+10)
        ui.draw_image("player_win.jpg",300,300,320,320)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
                player.health = 100
                player.keys = 0
                self.level = 1
                self.prev_level = 0
                self.is_game_completed = False
                player.speedX = 0
                player.speedY = 0

        
    
def setup(game_map):
    #Initialise Sprites and Add To Groups
    global all_sprites_group, wall_group, enemy_group, portal_group, bullet_group
    all_sprites_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

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
                    enemy = Enemy(x_coordinate,y_coordinate,24)
                    all_sprites_group.add(enemy)
                    enemy_group.add(enemy)




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
screen_size = (size[0],size[1]+40)
screen = pygame.display.set_mode(screen_size)

# -- Title of new window/screen
pygame.display.set_caption("Stickman Escape")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

player = Player(0,0,WHITE,24)


### -- Game Loop
game_state = GameState()
map_manager = Maps()
ui = UI()
tilesize = size[0]//25

while not game_state.done:
        game_state.state_manager() 
         # - The clock ticks over
        clock.tick(60)
    
#End While - End of game loop
    
pygame.quit()


