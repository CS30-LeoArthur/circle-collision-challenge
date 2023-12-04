import pygame
import random
import math


# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def mouse_position():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    return mouse_x, mouse_y

def check_collision(player):
    for i in range(len(random_circles)):
        if rectCollide(player, random_circles[i]):
            return i
    
    return -1

def rectCollide(rect1, rect2):
    return rect1.x < rect2.x + rect2.width and rect1.y < rect2.y + rect2.height and rect1.x + rect1.width > rect2.x and rect1.y + rect1.height > rect2.y

def distance_calc(player):
    run = mouse_position()[0] - (player.x + player.width / 2)
    rise = mouse_position()[1] - (player.y + player.height / 2) 
    distance = math.sqrt(rise**2 + run**2)
    
    dy = rise * 3 / distance
    dx = run * 3 / distance
    return dx, dy


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
    def __init__(self, x, y, width, height, change_x, change_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.change_x = change_x
        self.change_y = change_y
    
    def draw_player(self, screen):
        pygame.draw.ellipse(screen, GREY, [self.x, self.y, self.width, self.height])
        pygame.draw.ellipse(screen, BLUE, [self.x, self.y, self.width, self.height], 2)
    
    def update(self):
        self.change_x, self.change_y = distance_calc(self)
        self.y = self.y + self.change_y
        self.x = self.x + self.change_x
        


# Program Variables
player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2, 20, 20, 0, 0)
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