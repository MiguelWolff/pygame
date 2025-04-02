import pygame
pygame.init()

"""largura_tela = 630
altura_tela = 480
tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('Aplicação 01')
tela.fill("white")
pygame.display.flip()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

pygame.quit()"""


"""largura_tela = 630
altura_tela = 480
tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('Desenhando uma linha')
tela.fill("red")
pygame.display.flip()
run = True

while run:
    pygame.draw.line(tela, "blue", (0,240), (640,240), 50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

pygame.quit()"""

largura_tela = 630
altura_tela = 480
tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('Desenhando uma linha')
tela.fill("red")
pygame.display.flip()
run = True

while run:
    pygame.draw.rect(tela, "white", (50, 50, 100, 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

pygame.quit()