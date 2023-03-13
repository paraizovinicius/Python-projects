import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10,)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

pygame.init()
pygame.display.set_caption("Conway's game of life")

def update(screen, cells, size, regra, with_progress=False): 
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    #O método shape retorna uma tupla (x,y) com o i e o j da matriz A^ij
    # se for .shape[0] retorna i (linha) e .shape[1] retorna o j (coluna) 
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        
        if cells[row, col] == 1: #VIVA
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:  
                    color = COLOR_ALIVE_NEXT
            if regra == "B3S236" and alive == 6:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else: #MORTA
            if alive == 3: 
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    
    regra = input("Qual a regra a ser seguida? - B3S23 ou B3S236    ")
    
    A = "B3S23"
    B = "B3S236"
    if (regra == A) or (regra == B):
        
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        cells = np.zeros((60, 80)) #O conjunto inicial é esse grid inicializado com zeros
        screen.fill(COLOR_GRID)
        update(screen, cells, 10, regra)

        pygame.display.flip()
        pygame.display.update()

        running = False

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = not running
                        update(screen, cells, 10, regra)
                        pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    update(screen, cells, 10, regra)
                    pygame.display.update()

            screen.fill(COLOR_GRID)

            if running:
                cells = update(screen, cells, 10, regra, with_progress=True)
                pygame.display.update()

            time.sleep(0.001)
            
    else:        
        print("Regra não identificada")
        quit()        


if __name__ == "__main__":
    main()