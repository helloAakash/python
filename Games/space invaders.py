

import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Space Invaders')

player_x = 100
player_y = 200
p_width = 50
p_height = 30
speed = 5

enemy_x = random.randint(0,450)
enemy_y = random.randint(0,100)
e_width = 40
e_height = 20
e_pos_x = 3
e_pos_y = 30

bullet_x = 100
bullet_y = 100
b_width = 5
b_height = 15
b_pos_x = 0
b_pos_y = 7
is_fire = 'ready'


def player(x,y,w,h):
    pygame.draw.rect(screen,(0,150,200),(x,y,w,h))

def enemy(x,y,w,h):
    pygame.draw.rect(screen,(200,0,0),(x,y,w,h))

def bullet(x,y,w,h):
    global is_fire
    is_fire = 'fire'
    pygame.draw.rect(screen,(255,255,0),(x,y,w,h))

run = True

while run:
    pygame.time.delay(10)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player_x<450:
        player_x+=speed
    if keys[pygame.K_LEFT] and player_x>0:
        player_x-=speed
    if keys[pygame.K_UP] and player_y>0:
        player_y-=speed
    if keys[pygame.K_DOWN] and player_y<470:
        player_y+=speed

    if keys[pygame.K_SPACE]:
        if is_fire is 'ready':
            bullet_x = player_x + 23
            bullet_y = player_y
            bullet(bullet_x,bullet_y,b_width,b_height)

    #enemy movement
    enemy_x+=e_pos_x
    
    if enemy_x>=463:
        e_pos_x=-3
        enemy_y+=e_pos_y
    elif enemy_x<=0:
        e_pos_x=3
        enemy_y+=e_pos_y

    if is_fire is 'fire':
        bullet(bullet_x,bullet_y,b_width,b_height)
        bullet_y -= b_pos_y


    if bullet_y<=0:
        is_fire = 'ready'


    player(player_x,player_y,p_width,p_height)
    enemy(enemy_x,enemy_y,e_width,e_height)
    pygame.display.update()