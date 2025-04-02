import pygame
pygame.init()

largura_tela = 640
altura_tela = 480

windows= pygame.display.set_mode((largura_tela, altura_tela))
run = True

while run:
    posicao = pygame.mouse.get_pos()
    print(f"Posição X e Y do mouse:",posicao)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.QUIT()
