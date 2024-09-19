#Tron Light Cycle restart_game

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Light Cycle")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Game settings
clock = pygame.time.Clock()
SPEED = 10

# Light cycle class
class LightCycle:
    def __init__(self, color, start_pos):
        self.color = color
        self.positions = [start_pos]
        self.direction = pygame.K_RIGHT
        self.alive = True

    def move(self):
        if self.direction == pygame.K_UP:
            new_pos = (self.positions[-1][0], self.positions[-1][1] - SPEED)
        elif self.direction == pygame.K_DOWN:
            new_pos = (self.positions[-1][0], self.positions[-1][1] + SPEED)
        elif self.direction == pygame.K_LEFT:
            new_pos = (self.positions[-1][0] - SPEED, self.positions[-1][1])
        elif self.direction == pygame.K_RIGHT:
            new_pos = (self.positions[-1][0] + SPEED, self.positions[-1][1])

        self.positions.append(new_pos)

    def draw(self, screen):
        for pos in self.positions:
            pygame.draw.rect(screen, self.color, (*pos, SPEED, SPEED))

    def check_collision(self):
        if self.positions[-1] in self.positions[:-1]:
            self.alive = False
        if not (0 <= self.positions[-1][0] < WIDTH and 0 <= self.positions[-1][1] < HEIGHT):
            self.alive = False

def computer_move(computer):
    directions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    new_direction = random.choice(directions)
    computer.direction = new_direction

def restart_game():
    player1.__init__(BLUE, (100, 100))
    player2.__init__(RED, (700, 500))

player1 = LightCycle(BLUE, (100, 100))
player2 = LightCycle(RED, (700, 500))

def main():
    global player1, player2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    player1.direction = event.key
                elif event.key == pygame.K_r:
                    restart_game()

        if player1.alive:
            player1.move()
            player1.check_collision()

        if player2.alive:
            computer_move(player2)
            player2.move()
            player2.check_collision()

        screen.fill(BLACK)
        player1.draw(screen)
        player2.draw(screen)

        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()
