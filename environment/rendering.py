import pygame

WIDTH, HEIGHT = 600, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def render_env(cars, light):
    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (70,70,70), (250,0,100,600))
    pygame.draw.rect(screen, (70,70,70), (0,250,600,100))

    for i in range(cars[0]):
        pygame.draw.rect(screen, (0,0,255), (270, 500 - i*20, 20, 10))

    for i in range(cars[1]):
        pygame.draw.rect(screen, (0,255,255), (310, 100 + i*20, 20, 10))

    for i in range(cars[2]):
        pygame.draw.rect(screen, (255,0,0), (100 + i*20, 270, 10, 20))

    for i in range(cars[3]):
        pygame.draw.rect(screen, (255,255,0), (500 - i*20, 310, 10, 20))

    if light == 0:
        pygame.draw.circle(screen, (0,255,0), (300, 200), 10)
    elif light == 1:
        pygame.draw.circle(screen, (255,0,0), (300, 200), 10)
    else:
        pygame.draw.circle(screen, (255,255,0), (300, 200), 10)

    pygame.display.flip()