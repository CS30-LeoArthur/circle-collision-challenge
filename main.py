import pygame
import random

# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

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
        self.x = self.x + self.change_x
        self.y = self.y + self.change_y
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20, 20, 0, 0)
def main():
    # Initialize pygame
    pygame.init()

    # Screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    # Loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # Game logic

        # Drawing
        screen.fill(WHITE)
        player.draw_player(screen)

        # Manage how fast the screen updates
        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()