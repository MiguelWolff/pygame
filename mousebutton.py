import pygame
pygame.init()

largura_tela = 800
altura_tela = 600

windows= pygame.display.set_mode((largura_tela, altura_tela))
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicou o botão do mouse")
            print(event)
            pygame.draw.rect(windows,"red", (50, 50, 100, 50))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            print("Soltou o botão do mouse")
            print(event)
            pygame.draw.rect(windows, "green", (50, 50, 100, 50))
            pygame.display.flip()

pygame.quit()