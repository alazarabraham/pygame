import pygame
background = pygame.image.load("Venus.jpg")

x = 50
y = 50
width = 40
height = 60
vel = 5
fps = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption("Venus")
clock = pygame.time.Clock()


run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= vel
    if key[pygame.K_RIGHT]:
        x += vel
    if key[pygame.K_UP]:
        y -= vel
    if key[pygame.K_DOWN]:
        y += vel
    screen.fill(BLACK)
    screen.blit(background, (0,0))
    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    pygame.display.update()
    
    pygame.display.flip()
pygame.QUIT

