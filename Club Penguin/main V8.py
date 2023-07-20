import pygame
import sys
import os
from pygame.math import Vector2


'''
Variables
'''
worldx = 1500
worldy = 800
fps = 40  # frame rate
ani = 4  # animation cycles
world = pygame.display.set_mode([worldx, worldy])
player_width = 80
player_height = 100

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


class Predio(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))  # , pygame.SRCALPHA
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        '''if(angle!=0):
            rotated_image = pygame.transform.rotate(self.image, angle)
            rotated_image_center = rotated_image.get_rect().center
            rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
            world.blit(rotated_image, rotated_image_rect)'''

    def isInsideWall(x, y):
        # Verifica se o player colidiu com algum prédio
        for predio in predio_list:
            if predio.rect.collidepoint(x, y):
                return True
        return False


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
            img = pygame.image.load(os.path.join('Python-projects', 'Club Penguin', 'images', 'player' + str(i) + '.png')).convert()
            img = pygame.transform.scale(img, (player_width, player_height))  # Resize the image
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            
            origin = self.image.get_rect().midbottom # Centralizar o player não pela cabeça, mas pelos pés
            
            #pivot = self.image.get_rect(midbottom=(origin[0],origin[1]))
            

        

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

        if (x == 0 and y == 0):
            self.movex = 0
            self.movey = 0

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
            self.image = pygame.transform.flip(
                self.images[self.frame // ani], True, False)

        # moving animation sudeste
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving animation norte

        # moving animation sul

    def position(self):
        return self.rect.x, self.rect.y

    def setPosition(self, x, y):
        player.rect.x = x
        player.rect.y = y

    def collideWithWall(self):
        # Verifica se o player colidiu com algum prédio
        collisions = pygame.sprite.spritecollide(self, predio_list, False)

        if collisions:
            return True
        else:
            return False


'''
Setup
'''

backdrop = pygame.image.load(os.path.join(
    'Python-projects', 'Club Penguin', 'images', 'Downtown' + '.png'))
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

# Inicialização de algumas variáveis
requiredPos = (0, 0)
steps = 10
moving = False


XorY = 0


'''
DOWNTOWN MAP
'''
predio_list = pygame.sprite.Group()
predio1 = Predio(530, 290, 430, 50,0)  # spawn a building

predio_list.add(predio1)


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

        if (pygame.mouse.get_pressed()[0]):
            moving = True
            pos = pygame.mouse.get_pos()
            requiredPos = pos

            if (moving == True):
                player.control(0, 0)

            # se não teve mudança no eixo X (evitar erro de DIV/0)
            if (pos[0]-player.position()[0]) == 0:
                player.control(0, steps)

            else:
                # se não teve mudança no eixo Y (evitar erro de DIV/0)
                if (pos[1]-player.position()[1]) == 0:
                    player.control(steps, 0)
                else:

                    distXorY = abs(pos[0]-player.position()[0]) - \
                        abs(pos[1]-player.position()[1])
                    XorY = distXorY

                    stepsY = abs(
                        ((pos[1]-player.position()[1])/(pos[0]-player.position()[0]))*10)

                    stepsX = abs(
                        ((pos[0]-player.position()[0])/(pos[1]-player.position()[1]))*10)

                    # ESTÁ DANDO PROBLEMA PORQUE SE A STEPX OU STEPY TIVER VÍRGULA, ELE VAI DESCONSIDERAR

                    # Clicou pra nordeste
                    if ((pos[0] - player.position()[0]) > 0 and (pos[1] - player.position()[1]) > 0):
                        if (distXorY > 0):
                            # se o caminho de X for maior que o Y, o caminho de Y que será calculado
                            player.control(steps, stepsY)
                        else:
                            # se o caminho de Y for maior que o X, o caminho de X que será calculado
                            player.control(stepsX, steps)

                    # Clicou pra sudeste
                    if ((pos[0] - player.position()[0]) > 0 and (pos[1] - player.position()[1]) < 0):
                        if (distXorY > 0):
                            player.control(steps, -stepsY)
                        else:
                            player.control(stepsX, -steps)

                    # Clicou pra noroeste
                    if ((pos[0] - player.position()[0]) < 0 and (pos[1] - player.position()[1]) > 0):
                        if (distXorY > 0):
                            player.control(-steps, stepsY)
                        else:
                            player.control(-stepsX, steps)

                    # Clicou pra sudoeste
                    if ((pos[0] - player.position()[0]) < 0 and (pos[1] - player.position()[1]) < 0):
                        if (distXorY > 0):
                            player.control(-steps, -stepsY)
                        else:
                            player.control(-stepsX, -steps)

    # Função de parada do player
    if (XorY > 0 and (abs(requiredPos[0] - player.position()[0]) < 10 and (abs(requiredPos[0] - player.position()[0]) > -10))):
        player.control(0, 0)
        moving = False

    # Função de parada do player
    if (XorY < 0 and (abs(requiredPos[1] - player.position()[1]) < 10 and (abs(requiredPos[1] - player.position()[1]) > -10))):
        player.control(0, 0)
        moving = False

    if (player.collideWithWall()):  # Lida com a colisão
        player.control(0, 0)
        moving = False

        # jeito "fácil" de lidar com colisão, porém não é o melhor
        if ((Predio.isInsideWall(player.position()[0], player.position()[1]+11)) == False):
            player.setPosition(player.position()[0], player.position()[1]+11)
        if ((Predio.isInsideWall(player.position()[0]+11, player.position()[1])) == False):
            player.setPosition(player.position()[0]+11, player.position()[1])

        if ((Predio.isInsideWall(player.position()[0], player.position()[1]-11)) == False):
            player.setPosition(player.position()[0], player.position()[1]-11)
        if ((Predio.isInsideWall(player.position()[0]-11, player.position()[1])) == False):
            player.setPosition(player.position()[0]-11, player.position()[1])

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    predio_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
