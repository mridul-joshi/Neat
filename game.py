import pygame
import neat
import time
import os
import random
pygame.font.init()

WIN_WIDTH = 1200
WIN_HEIGHT = 600

# importing images of dino
DINO_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "dino0.jpg"))),
             pygame.transform.scale2x(pygame.image.load(
                 os.path.join("images", "dino1.jpg"))),
             pygame.transform.scale2x(pygame.image.load(
                 os.path.join("images", "dino2.jpg"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("images", "dino3.jpg")))]

# importing Obstacles
OBSTACLE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "cactus0.jpg"))),
                 pygame.transform.scale2x(pygame.image.load(
                     os.path.join("images", "cactus1.jpg"))),
                 pygame.transform.scale2x(pygame.image.load(
                     os.path.join("images", "cactus3.jpg"))),
                 pygame.transform.scale2x(pygame.image.load(os.path.join("images", "cactus4.jpg")))]

# importing Background
BG_IMG = pygame.transform.scale2x(pygame.image.load(
    os.path.join("images", "background.jpg")))

# importing ground
BASE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "ground0.jpg"))),
            pygame.transform.scale2x(pygame.image.load(
                os.path.join("images", "ground2.jpg"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("images", "ground2.jpg")))]

# STATS fonts style
STAT_FONT = pygame.font.SysFont('comicsans', 50)


class Dino:

    IMGS = DINO_IMGS
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.tick_count = 0
        self.img_count = 0
        self.img = self.IMGS[0]

    # movement mechanism of dino
    def move(self):
        self.tick_count += 1

        # displacement

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[1]

        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[2]

        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[1]

        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[2]

        elif self.img_count < self.ANIMATION_TIME*4+1:
            self.img = self.IMGS[1]
            self.img_count = 0

        final = self.img
        new_rect = final.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(final, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Obstacle:
    # space between obstacle
    # velocity
    VEL = 5

    def __init__(self, x):
        self.x = x

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        self.obstacle = OBSTACLE_IMGS[1]
        win.blit(self.obstacle, (self.x, 400))


def draw_window(win, dino, obstacles):
    win.blit(BG_IMG, (0, 0))
    for obstacle in obstacles:
        obstacle.draw(win)
    dino.draw(win)

    pygame.display.update()


def main():
    dino = Dino(120, 400)
    obstacles = [Obstacle(1250)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        for obstacle in obstacles:
            x = random.randint(0, 3)
            obstacle.move()

        draw_window(win, dino, obstacles)


main()
