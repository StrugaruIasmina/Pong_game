import pygame
import sys
import random

pygame.init()


font = pygame.font.SysFont("Calibrate",60)
font_score = pygame.font.SysFont("Calibrate",20)
score = 0
height = 600
width = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

paleta_size = [80,20]
paleta_pos = [280,570]
dx,dy = 0,0

pong_size = [50,50]
pong_pos = [10,10]

imagine = pygame.image.load("poza.jpg").convert_alpha()
imagine = pygame.transform.scale(imagine, (50,50))

x,y = 20,14
ok = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            ok = 1
            if event.key == pygame.K_LEFT:
                dx,dy = -20,0
            if event.key == pygame.K_RIGHT:
                dx,dy = 20,0
        
    paleta_pos[0] +=dx
    paleta_pos[1] +=dy

    if paleta_pos[0] < 0:
        paleta_pos[0] = 0
    if paleta_pos[0] + paleta_size[0] > width:
        paleta_pos[0] = width - paleta_size[0]

    if ok == 1:
        pong_pos[0] +=x
        pong_pos[1] +=y

    if pong_pos[0] <= 0 or pong_pos[0] + pong_size[0] >=width:
        x = -x
    if pong_pos[1] <= 0:
        y = -y
    if pong_pos[1] + pong_size[1] >= paleta_pos[1] and pong_pos[0] + pong_size[0] >= paleta_pos[0] and pong_pos[0] <= paleta_pos[0] + paleta_size[0]:
        y = - y
        score +=1
    if pong_pos[1] + pong_size[1] >=height:
        running = False


    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,255,255),(paleta_pos[0],paleta_pos[1],paleta_size[0],paleta_size[1]))
    obiect = pygame.Rect(pong_pos[0],pong_pos[1],pong_size[0],pong_size[1])
    
    text = font_score.render(f"Score: {score}",False,(255,0,0))
    screen.blit(imagine,obiect)
    screen.blit(text,[20,20])
    pygame.display.flip()
    
    clock.tick(15 + score)

if running == False:
    screen.fill((0,0,0))
    final_text = font.render("GAME OVER",False,(255,0,0))
    screen.blit(final_text,[180,300])
    pygame.display.flip()
    pygame.time.delay(3000)

pygame.quit()
sys.exit()