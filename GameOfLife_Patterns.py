import time
import pygame
import numpy as np

COR_BG = (15, 15, 15,)
CORGRID = (35, 35, 35)
COR_MORRER = (170, 170, 170)
COR_VIVER = (255, 255, 255)

pygame.init()
pygame.display.set_caption("jOGO DA VIDA DE CONWAY")

#essa é a função que vai dar vida às celulas, trazendo não somente as leis do funcionamento, mas também vai permitir que o tempo passado no time.sleep(0.0001) faça sentido
def update(tela, cells, size, regra, with_progress=False): 
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    #O método shape retorna uma tupla (x,y) com o i e o j da matriz A^ij
    # se for .shape[0] retorna i (linha) e .shape[1] retorna o j (coluna) 
    for row, col in np.ndindex(cells.shape):
        #usando esse método, row e col retornarão cada posição Aij possível numa matriz (i,j)
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        color = COR_BG if cells[row, col] == 0 else COR_VIVER
        
        
        #REGRAS --> B3S236
        #Se a célula VIVA estiver com nenhum ou 1 vizinho ou mais do que 3 vizinhos, morre
        #Se uma célula morta tiver 3 vizinhos ela nasce
        
        #Caso seja B36S23, a diferença é que se a celula morta tiver 3 ou 6 vizinhos, ela nasce
        
        if cells[row, col] == 1: #VIVA
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COR_MORRER
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:  
                    color = COR_VIVER
        else: #MORTA
            if alive == 3: 
                updated_cells[row, col] = 1
                if with_progress:
                    color = COR_VIVER

            if regra == '4' or regra == '5':#Condição para a regra B36S23
                if alive == 6: 
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COR_VIVER
            

        pygame.draw.rect(tela, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    
    regra = input("\nDigite a regra e o modelo:\nClique 1: B3S23 - modelo GLIDER\nClique 2: B3S23 - modelo PULSAR\nClique 3: B3S23 - modelo Gosper Glider Gun\nClique 4: B3S236 - modelo Replicator\nClique 5: B3S236 - modelo Bomber\n\nPara funcionar, clique na tela do jogo e aperte SPACEBAR\n\n")
    

    if regra == 1 or 2 or 3 or 4 or 5:

        pygame.init()
        tela = pygame.display.set_mode((800, 600))
        cells = np.zeros((60, 80)) #O conjunto inicial é esse grid inicializado com zeros
        tela.fill(CORGRID)
        update(tela, cells, 10, regra)

        pygame.display.flip()
        pygame.display.update()

        running = False

        while True: # Conjunto F #Loop infinito que vai permitir o jogo funcionar. Este loop vai chamar a função update centenas de vezes. Cada vez que essa função é executada, a tela muda e "dá vida" às células. Mas de fato, o maestro principal é a função update.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = not running
                        update(tela, cells, 10, regra)
                        pygame.display.update()
                if regra == '1' and pygame.mouse.get_pressed()[0]: ##GLIDER
                    pos = pygame.mouse.get_pos()
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    cells[(pos[1] + 10) // 10, (pos[0] + 10) // 10] = 1
                    cells[(pos[1] + 10) // 10, (pos[0] + 20) // 10] = 1
                    cells[(pos[1] + 20) // 10, (pos[0] + 0) // 10] = 1
                    cells[(pos[1] + 20) // 10, (pos[0] + 10) // 10] = 1
                    update(tela, cells, 10, regra)
                    pygame.display.update()
                
                if regra == '2' and pygame.mouse.get_pressed()[0]: ##PULSAR
                    pos = pygame.mouse.get_pos()
                    cells[(pos[1] - 60)// 10, (pos[0] + 20)// 10] = 1
                    cells[(pos[1] - 60)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] - 60)// 10, (pos[0] + 40)// 10] = 1
                    cells[(pos[1] - 60)// 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] - 60)// 10, (pos[0] - 30)// 10] = 1
                    cells[(pos[1] - 60)// 10, (pos[0] - 40)// 10] = 1
                    cells[(pos[1] + 60)// 10, (pos[0] + 20)// 10] = 1
                    cells[(pos[1] + 60)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] + 60)// 10, (pos[0] + 40)// 10] = 1
                    cells[(pos[1] + 60)// 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] + 60)// 10, (pos[0] - 30)// 10] = 1
                    cells[(pos[1] + 60)// 10, (pos[0] - 40)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] + 60)// 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] + 60)// 10] = 1
                    cells[(pos[1] + 40)// 10, (pos[0] + 60)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] + 40)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] - 40)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 60)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] + 60)// 10] = 1
                    cells[(pos[1] - 40)// 10, (pos[0] + 60)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] + 40)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] + 40)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] - 40)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] - 40)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] + 20)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] + 40)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] - 30)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] - 40)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] + 20)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] + 40)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 30)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 40)// 10] = 1
                    update(tela, cells, 10, regra)
                    pygame.display.update()

                if regra == '3' and pygame.mouse.get_pressed()[0]: ##GOSPER GLIDER GUN
                    pos = pygame.mouse.get_pos()
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    cells[pos[1] // 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] - 20)// 10] = 1
                    cells[pos[1]// 10, (pos[0] - 30)// 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] - 40)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] - 40)// 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] - 50)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] - 50)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] - 60)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] - 70)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 70)// 10] = 1
                    cells[pos[1]// 10, (pos[0] - 70)// 10] = 1
                    cells[pos[1]// 10, (pos[0] - 160)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 160)// 10] = 1
                    cells[pos[1]// 10, (pos[0] - 170)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 170)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] + 40)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 40)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] + 40)// 10] = 1
                    cells[pos[1]// 10, (pos[0] + 50)// 10] = 1
                    cells[(pos[1] - 40)// 10, (pos[0] + 50)// 10] = 1
                    cells[pos[1]// 10, (pos[0] + 70)// 10] = 1
                    cells[(pos[1] - 40)// 10, (pos[0] + 70)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] + 70)// 10] = 1
                    cells[(pos[1] - 50)// 10, (pos[0] + 70)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 170)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] + 170)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 180)// 10] = 1
                    cells[(pos[1] - 30)// 10, (pos[0] + 180)// 10] = 1
                    update(tela, cells, 10, regra)
                    pygame.display.update()

                if regra == '4' and pygame.mouse.get_pressed()[0]: ##REPLICATOR
                    pos = pygame.mouse.get_pos()
                    cells[(pos[1] + 20)// 10, pos[0]// 10] = 1
                    cells[(pos[1] - 20)// 10, pos[0]// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 10)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] - 20)// 10, (pos[0] + 20)// 10] = 1
                    cells[(pos[1] + 20)// 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] + 20)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] - 20)// 10] = 1
                    cells[pos[1] // 10, (pos[0] + 20)// 10] = 1
                    cells[pos[1] // 10, (pos[0] - 20)// 10] = 1
                    cells[(pos[1] - 10)// 10, (pos[0] - 10)// 10] = 1
                    cells[(pos[1] + 10)// 10, (pos[0] + 10)// 10] = 1
                    update(tela, cells, 10, regra)
                    pygame.display.update()

                if regra == '5' and pygame.mouse.get_pressed()[0]: ##BOMBER
                    pos = pygame.mouse.get_pos()
                    cells[pos[1] // 10, (pos[0] + 10)// 10] = 1
                    cells[pos[1] // 10, (pos[0] + 20)// 10] = 1
                    cells[pos[1] // 10, (pos[0] + 30)// 10] = 1
                    cells[(pos[1] + 10)// 10, pos[0] // 10] = 1
                    cells[(pos[1] + 20)// 10, pos[0] // 10] = 1
                    cells[(pos[1] + 30)// 10, pos[0] // 10] = 1
                    cells[(pos[1] + 30)// 10, (pos[0] + 90) // 10] = 1
                    cells[(pos[1] + 40)// 10, (pos[0] + 90) // 10] = 1
                    cells[(pos[1] + 50)// 10, (pos[0] + 90) // 10] = 1
                    update(tela, cells, 10, regra)
                    pygame.display.update()

            tela.fill(CORGRID)

            if running:
                cells = update(tela, cells, 10, regra, with_progress=True)
                pygame.display.update()

            time.sleep(0.001)
            
    else:        
        print("Digite um número válido de 1 até 5")
        quit()        


if __name__ == "__main__":
    main()









    