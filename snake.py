import pygame

pygame.init()
pygame.display.set_caption('Snake Game')
dis = pygame.display.set_mode((500, 400), pygame.FULLSCREEN)
pygame.display.update()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()