import pygame
import os
from pygame.locals import QUIT


'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a penguin
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 9):
            img = pygame.image.load(os.path.join('Python-projects','Club Penguin','images', 'player' + str(i) + '.png')).convert()
            # img.convert_alpha()  # optimise alpha
            # img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


def main():

    # Set this before initializing pygame
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    info = pygame.display.Info()
    window_width, window_height = info.current_w - 10, info.current_h - 50
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Club Penguin")

    blockSize = 10  # Set the size of the grid block
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, (10, 10, 10,), rect, 1)

    player = Player()   # spawn player
    player.rect.x = 100   # go to x
    player.rect.y = 100   # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == QUIT:
                executando = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
