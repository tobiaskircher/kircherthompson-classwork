#Pong
### SRC - this looks a good bit of code, but the ball disappears
### off the bottom or top sometimes and it could be faster!
import pygame,random
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)

#-- Random Bright Colour
def rand_colour():
    zero_value = random.randint(1,3)
    colour = []
    for i in range(1,4):
        if i == zero_value:
            colour.append(0)
        else:
            colour.append(random.randint(200,255))
        #endif
    #next i
    return colour

# -- Initialise PyGame
pygame.init()
# -- Blank Screen
x_screen_size = 640
y_screen_size = 480
size = (x_screen_size,y_screen_size)

# -- Variables
ball_width = 20
ball_colour = WHITE
ball_speed = 1.2
ball_speed_multiplier = 1.2
x_val = 320
y_val = 200

x_direction = 1
y_direction = 1
padd_length = 60
padd_width = 15
x_padd = 0
y_padd = 20

x_padd2 = 625
y_padd2 = 20
player1_score = 0
player2_score = 0


screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False
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
    
    keys = pygame.key.get_pressed()
    ## - PLAYER 2 the up key or down key has been pressed
    if keys[pygame.K_o] and y_padd2 >=0:
        y_padd2 -= 5
    if keys[pygame.K_l] and y_padd2 <= y_screen_size - padd_length:
        y_padd2 += 5
    #PLAYER 1
    if keys[pygame.K_w] and y_padd >=0:
        y_padd -= 5
    if keys[pygame.K_s] and y_padd <= y_screen_size - padd_length:
        y_padd += 5
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(str(player1_score)+":"+str(player2_score),True,WHITE)
    screen.blit(text, (300, 0))

    # -- Draw here
    pygame.draw.rect(screen,ball_colour,(x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen,WHITE,(x_padd,y_padd,padd_width,padd_length))
    pygame.draw.rect(screen,WHITE,(x_padd2,y_padd2,padd_width,padd_length))
    x_val += x_direction * ball_speed
    y_val += y_direction * ball_speed
    if y_val <= 0 or y_val >= y_screen_size - ball_width:
        y_direction *= -1
        ball_colour = rand_colour()
        
    # -- Collision with left paddle
    if (0 <= x_val <= padd_width) and (y_padd - ball_width < y_val < y_padd + padd_length):
        x_direction *= -1
        ball_colour = rand_colour()
        ball_speed *= ball_speed_multiplier

    if x_val <= 0:
        player2_score += 1
        x_val = 320
        y_val = random.randint(0,480)
        x_direction *= -1
        ball_speed = 1.2

    # -- Collision with right paddle
    if (x_screen_size - ball_width >= x_val >= x_screen_size - padd_width - ball_width) and (y_padd2 - ball_width < y_val < y_padd2 + padd_length):
        x_direction *= -1
        ball_colour = rand_colour()
        ball_speed *= ball_speed_multiplier

    if x_val >= x_screen_size:
        player1_score += 1
        x_val = 320
        y_val = random.randint(0,480)
        x_direction *= -1
        ball_speed = 1.2
        
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

