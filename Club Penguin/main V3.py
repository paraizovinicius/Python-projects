from typing import Tuple

import pygame
import sys
import os
    
    
'''
Variables
'''
worldx = 1500
worldy = 820
fps = 20  # frame rate
ani = 4  # animation cycles
world = pygame.display.set_mode([worldx, worldy])
player_width = 80
player_height = 100

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)
    
    
    
class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 8):
            img = pygame.image.load(os.path.join('Python-projects','Club Penguin','images', 'player' + str(i) + '.png')).convert()
            img = pygame.transform.scale(img, (player_width, player_height))  # Resize the image
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            
    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
        
    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        
        # moving animation leste
        
        # moving animation oeste

        # moving animation sudoeste
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving animation sudeste
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
            
        # moving animation norte
        
        #moving animation sul
        

    
'''
Setup
'''

backdrop = pygame.image.load(os.path.join('Python-projects','Club Penguin','images', 'Downtown' + '.png'))
backdrop = pygame.transform.scale(backdrop, (worldx, worldy))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

blockSize = 10  # Set the size of the grid block
for x in range(0, worldx, blockSize):
    for y in range(0, worldy, blockSize):
        rect = pygame.Rect(x, y, blockSize, blockSize)
        pygame.draw.rect(world, (10, 10, 10,), rect, 1)

player = Player()  # spawn player
player.rect.x = 700  # go to x
player.rect.y = 600  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10






'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('z'):
                pygame.quit()
                
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
                
                
        if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                #player.move_towards_point(pos[0], pos[1])
                
                
    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)