import pygame

# pygame setup:
pygame.init()
SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
CLOCK = pygame.time.Clock()
running = True
FPS = 60
background_colour = "White"
SCREEN.fill(background_colour)
i = 0

#circle properties:
circle_centre_x = SCREEN_WIDTH // 2
circle_centre_y = SCREEN_HEIGHT // 2
if SCREEN_WIDTH > SCREEN_HEIGHT:
    INITIAL_CIRCLE_RADIUS = SCREEN_WIDTH // 2
else: 
    INITIAL_CIRCLE_RADIUS = SCREEN_HEIGHT // 2

circle_width = 8 # 0 for a filled circle

# circle colours:
circle_colour = (255, 255, 255)


while running:
    # pygame.QUIT event means the user clicked X to close your window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys_pressed = pygame.key.get_pressed()

    # fill the screen with background_colour to wipe away anything from last frame: 
    SCREEN.fill(background_colour)

    # render the circle:
    for j in range(i, (2 * SCREEN_WIDTH // circle_width), circle_width):
        if INITIAL_CIRCLE_RADIUS - (2 * j) > 0:
            pygame.draw.circle(SCREEN, "White", (circle_centre_x,circle_centre_y), INITIAL_CIRCLE_RADIUS - (2 * j), circle_width)
            pygame.draw.circle(SCREEN, "Black", (circle_centre_x,circle_centre_y), INITIAL_CIRCLE_RADIUS - ((2* j) + 1), circle_width)

    if i >= circle_width:
        i = 0
    else:
        i += 1

    pygame.display.flip() # flip() the display to put your work on screen

    CLOCK.tick(FPS)  # limits FPS to 60

pygame.quit()