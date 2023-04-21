# How to use custom fonts in your pygame games!
import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font('./fonts/TetrisBlocks-P99g.ttf', 52)
font2 = pygame.font.Font('./fonts/Aviola Memories Demo.otf', 52)
font3 = pygame.font.Font('./fonts/Gareth.ttf', 52)
screen = pygame.display.set_mode([800, 500])

run = True
while run:
    clock.tick(fps)
    screen.fill('orange')
    my_text = font.render('Hello, World!', True, 'black')
    screen.blit(my_text, (100, 150))
    my_text2 = font2.render('Hello, World!', True, 'black')
    screen.blit(my_text2, (150, 250))
    my_text3 = font3.render('Hello, World!', True, 'black')
    screen.blit(my_text3, (200, 350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
