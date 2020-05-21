import pygame
from oop.blob import Blob

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

RED_BLOBS_COUNT = 20
GREEN_BLOBS_COUNT = 35
BLUE_BLOBS_COUNT = 27


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SIMPLE GAME")
clock = pygame.time.Clock()


def draw_environment(*blob_list):
    game_display.fill(WHITE)
    for blob_generation in blob_list:
        for _id, blob in blob_generation.items():
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
    pygame.display.update()


def main():
    red_blobs = dict(enumerate([Blob(RED, WIDTH, HEIGHT) for _ in range(RED_BLOBS_COUNT)]))
    green_blobs = dict(enumerate([Blob(GREEN, WIDTH, HEIGHT) for _ in range(GREEN_BLOBS_COUNT)]))
    blue_blobs = dict(enumerate([Blob(BLUE, WIDTH, HEIGHT) for _ in range(BLUE_BLOBS_COUNT)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(red_blobs, green_blobs, blue_blobs)
        clock.tick(60)


if __name__ == '__main__':
    main()

