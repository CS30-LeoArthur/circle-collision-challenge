import pygame
import random


# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def mouse_position_x():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    return mouse_x

def mouse_position_y():
    pos = pygame.mouse.get_pos()
    mouse_y = pos[1]
    return mouse_y

def check_collision(player):
    for i in range(len(random_circles)):
        if rectCollide(player, random_circles[i]):
            return i
    
    return -1

def rectCollide(rect1, rect2):
    return rect1.x < rect2.x + rect2.width and rect1.y < rect2.y + rect2.height and rect1.x + rect1.width > rect2.x and rect1.y + rect1.height > rect2.y

class Circle():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw_circle(self, screen):
        pygame.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height])

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_player(self, screen):
        pygame.draw.ellipse(screen, GREY, [self.x, self.y, self.width, self.height])
        pygame.draw.ellipse(screen, BLUE, [self.x, self.y, self.width, self.height], 2)
    
    def update(self):
        self.x = mouse_position_x() - (self.width / 2)
        self.y = mouse_position_y() - (self.height / 2)


# Program Variables
player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2, 20, 20)
random_circles = []

def main():
    # Initialize pygame
    pygame.init()

    # Screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    frameCount = 1

    clock = pygame.time.Clock()
    # Loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # Game logic
        # Update player
        player.update()
        # Create random circle food
        random_colour = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        circle_width = random.randrange(20, 40)
        circle_height = circle_width
        if frameCount % 60 == 0:
            random_circles.append(Circle(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT), circle_width, circle_height, random_colour))

        if check_collision(player) != -1:
            player.width = player.width + (random_circles[check_collision(player)].width / 8)
            player.height = player.height + (random_circles[check_collision(player)].height / 8)
            random_circles.pop(check_collision(player))
    
        # Drawing
        screen.fill(WHITE)
        player.draw_player(screen)
        for i in range(len(random_circles)):
            random_circles[i].draw_circle(screen)

        # Manage how fast the screen updates
        frameCount += 1
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()