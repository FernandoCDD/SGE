import pygame

from player import Player

pygame.init()

ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Proyecto Robot 8-bit")

player = Player()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.up = True
            elif event.key == pygame.K_DOWN:
                player.down = True
            elif event.key == pygame.K_RIGHT:
                player.right = True
            elif event.key == pygame.K_LEFT:
                player.left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.up = False
            elif event.key == pygame.K_DOWN:
                player.down = False
            elif event.key == pygame.K_RIGHT:
                player.right = False
            elif event.key == pygame.K_LEFT:
                player.left = False

    player.movement()

    ventana.fill((255, 255, 255))  # Rellena la pantalla con un color blanco
    ventana.blit(player.image, player.position)

    pygame.display.update()
    clock.tick(30)
