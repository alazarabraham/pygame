import pygame
background = pygame.image.load("Venus.jpg")

x = 50
y = 50
width = 40
height = 60
vel = 3
fps = 30
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
display = pygame.display.set_mode((1000,750))
pygame.display.set_caption("Venus")
time = pygame.time.Clock()


run = True
while run:
    time.tick(fps)
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
    display.fill(black)
    display.blit(background, (0,0))
    pygame.draw.rect(display,(255,0,0),(x,y,width,height))
    pygame.display.update()
    
    pygame.display.flip()
pygame.QUIT

