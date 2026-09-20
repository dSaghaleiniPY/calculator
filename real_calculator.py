import pygame
import math
pygame.init()

# VARIABLES <--------------------------------------------------------------
# setup
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 800
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 108

X_NUMKEYS = [180, 50, 180, 310, 440, 50, 180, 310, 440, 50]
X_AC = 310
X_DIVIDE = 440
X_MULTIPLY = 50
X_SUBTRACT = 50
X_ADD = 180

Y_NUMKEYS = [504, 208, 208, 208, 208, 356, 356, 356, 356, 504]
Y_AC = 504
Y_MULTIPLY = 504
Y_DIVIDE = 504
Y_SUBTRACT = 652
Y_ADD = 652

current_number = ""
operation = None

# images
IMAGE_NUMKEYS = []
for i in range(10):
    IMAGE_NUMKEYS.append(pygame.image.load(f"number_{i}.png"))

IMAGE_AC = pygame.image.load("clear_ac.png")
IMAGE_DIVIDE = pygame.image.load("divide.png")
IMAGE_MULTIPLY = pygame.image.load("multiplication.png")
IMAGE_ADD = pygame.image.load("add.png")
IMAGE_SUBTRACT = pygame.image.load("subtract.png")

# pygame assets (fonts)
NUMBER_FONT = pygame.font.SysFont("Arial", 35)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



clock = pygame.time.Clock()
# WHILE RUNNING <----------------------------------------------------------
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("#1f1e21") 

    # show images
    for i in range(10):
        screen.blit(IMAGE_NUMKEYS[i], (X_NUMKEYS[i], Y_NUMKEYS[i]))

    screen.blit(IMAGE_DIVIDE, (X_DIVIDE, Y_DIVIDE))
    screen.blit(IMAGE_MULTIPLY, (X_MULTIPLY, Y_MULTIPLY))
    screen.blit(IMAGE_AC, (X_AC, Y_AC))
    screen.blit(IMAGE_SUBTRACT, (X_SUBTRACT, Y_SUBTRACT))
    screen.blit(IMAGE_ADD, (X_ADD, Y_ADD))

    # display the text
    number_image = NUMBER_FONT.render(current_number, True, "white")
    screen.blit(number_image, (50, 40))
    # making the buttons work
    mouse_clicked = pygame.mouse.get_pressed()[0]
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_clicked:
        # number keys
        for i in range(10):
            if (mouse_x > X_NUMKEYS[i] and
                mouse_x < X_NUMKEYS[i] + BUTTON_WIDTH and
                mouse_y > Y_NUMKEYS[i] and
                mouse_y < Y_NUMKEYS[i] + BUTTON_HEIGHT
            ):
                current_number += str(i)
     
        # AC
        if (mouse_x > X_AC and
            mouse_x < X_AC + BUTTON_WIDTH and 
            mouse_y < Y_AC + BUTTON_HEIGHT and 
            mouse_y > Y_AC): 
            current_number = ""
            operation = None

        # Plus
        if (mouse_x > X_ADD and
            mouse_x < X_ADD + BUTTON_WIDTH and
            mouse_y < Y_ADD + BUTTON_HEIGHT and
            mouse_y > Y_ADD
            ):
            operation = " + "

        # Multiply
        if (mouse_x > X_MULTIPLY and
            mouse_x < X_MULTIPLY + BUTTON_WIDTH and
            mouse_y < Y_MULTIPLY + BUTTON_HEIGHT and
            mouse_y > Y_MULTIPLY
            ):
            operation = " * "

        # Subtract
        if (mouse_x > X_SUBTRACT and
            mouse_x < X_SUBTRACT + BUTTON_WIDTH and
            mouse_y < Y_SUBTRACT + BUTTON_HEIGHT and
            mouse_y > Y_SUBTRACT
            ):
            operation = " - "

        # Divide
        if (mouse_x > X_DIVIDE and
            mouse_x < X_DIVIDE + BUTTON_WIDTH and
            mouse_y < Y_DIVIDE + BUTTON_HEIGHT and
            mouse_y > Y_DIVIDE
            ):
            operation = " / "

        print(current_number)

    pygame.display.flip() 
    clock.tick(6)         