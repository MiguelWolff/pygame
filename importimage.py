import pygame
pygame.init()

windows = pygame.display.set_mode((600, 600))

imagem = pygame.image.load("Image\download.png")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    windows.blit(imagem, (0,0))
    pygame.display.update()