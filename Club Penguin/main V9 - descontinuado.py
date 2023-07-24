import pygame
import os
import datetime

pygame.init()
worldx = 1500
worldy = 800
window = pygame.display.set_mode((worldx, worldy))
clock = pygame.time.Clock()
backdrop = pygame.image.load(os.path.join(
    'Python-projects', 'Club Penguin', 'images', 'Downtown' + '.png'))
backdrop = pygame.transform.scale(backdrop, (worldx, worldy))
backdropbox = window.get_rect()



fps = 40  # frame rate
ani = 4  # animation cycles
player_width = 80
player_height = 100

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


        
        
'''
DOWNTOWN MAP
'''
Block1 = pygame.Surface((400, 400), pygame.SRCALPHA)
Block1.fill(BLUE)
Block2 = pygame.Surface((400, 400), pygame.SRCALPHA)
Block2.fill(BLUE)
Block3 = pygame.Surface((400, 400), pygame.SRCALPHA)
Block3.fill(BLUE)





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


def blitRotate(surf, image, origin, pivot, angle):

    # offset from pivot to center
    image_rect = image.get_rect(
        topleft=(origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center

    # rotated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # rotated image center
    rotated_image_center = (
        origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

    


start_time = pygame.time.get_ticks()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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


    now = datetime.datetime.now()
    center = window.get_rect().center
    
    window.fill(0)
    window.blit(backdrop, backdropbox)
    
    blitRotate(window, Block1, center, (170, 450), 0) 
    blitRotate(window, Block2, center, (-120, -20), 61)  
    blitRotate(window, Block3, center, (-80, -115), -155) 
    
    player.update()
    player_list.draw(window)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
exit()