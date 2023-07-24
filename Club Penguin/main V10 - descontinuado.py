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
        # Verifica se o player colidiu com algum bloco
        collisions = pygame.sprite.spritecollide(self, block_list, False)

        if collisions:
            return True
        else:
            return False

# O rect permanece o mesmo, mesmo se a imagem aparenta estar rotacionada. Ou seja, as colisões estão sendo feitas no rect antigo
class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(ALPHA)

        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Rotate the image and update the rect
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        pass

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
            
    




player = Player()  # spawn player
player.rect.x = 700  # go to x
player.rect.y = 600  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

center = window.get_rect().center
#(self, width, height, surf, origin, pivot, angle):
Block1 = Block(400, 400, center[0]-200, center[1]-400, 20)
#Block2 = Block(400, 400, center[0] - 120, center[1] - 20, 61)
#Block3 = Block(400, 400, center[0] - 80, center[1] - 115, -155)
block_list = pygame.sprite.Group()
block_list.add(Block1)
#block_list.add(Block2)
#block_list.add(Block3)

# Inicialização de algumas variáveis
requiredPos = (0, 0)
steps = 10
moving = False
XorY = 0



    


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
        
    if (player.collideWithWall()):  # Lida com a colisão
        player.control(0, 0)
        moving = False


    now = datetime.datetime.now()

    window.fill(0)
    window.blit(backdrop, backdropbox)
    
    
    
    player.update()
    player_list.draw(window)
    block_list.draw(window)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
exit()