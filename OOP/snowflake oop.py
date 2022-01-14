import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
# Create the snow variables
x = [random.randint(0,700) for i in range(3)]
y = [random.randint(0,50) for i in range(3)]
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
class Snow():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.colour = None

    def update(self):
        self.y += 1
        if self.y > 500:
            self.y=0
            self.x=random.randint(0,700)

    def draw(self):
        self.update()
        pygame.draw.rect(screen, self.colour, [self.x,self.y,10,10])

class House():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.colour = BLUE

    def draw(self):
        pygame.draw.rect(screen, self.colour, [100,300,200,200])
        pygame.draw.rect(screen, BLACK, [110,410,50,90])
        
        
        
        
snowflakes = []
for i in range(50):
    snowflake = Snow()
    snowflake.x = random.randint(0,700)
    snowflake.y = random.randint(0,500)
    snowflake. colour = random.choice([RED, WHITE, GREEN])
    snowflakes.append(snowflake)

house1 = House()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

        
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
 
    # --- Drawing code should go here
    for snow in snowflakes:
        house1.draw()
        snow.draw()
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
