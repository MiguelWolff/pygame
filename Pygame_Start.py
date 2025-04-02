import pygame

pygame.init()

largura = 500
altura = 400

janela = pygame.display.set_mode((500, 400))

pygame.display.set_caption('Exemplos Pygame - 01')

janela.fill("white")

#pygame.display.flip()
pygame.display.update()