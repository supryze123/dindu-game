import pygame
from random import randint
from sys import exit #za gore desno X

xvelocity = 7
yvelocity = 7

pygame.init() #pocetak
screen = pygame.display.set_mode((800,400)) #rezolucija
pygame.display.set_caption('Le dindu game') #window name
clock = pygame.time.Clock() #FPS limit

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = 1

test_surface = pygame.Surface((800,400))
test_surface.fill('Green')

society_surf = pygame.image.load('society.png').convert_alpha()
society_rect = society_surf.get_rect(bottomright = (800, 300))

player_surf = pygame.image.load('dindu.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

pygame.key.set_repeat(10, 10)
while 1: #window ostaje otvoren
    for event in pygame.event.get():         #PLAYER INPUT
        if event.type == pygame.QUIT: #exit da radi 
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and player_rect.top > 0 :
                    player_rect.y -= 5
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and player_rect.bottom <= 400:
                    player_rect.y += 5
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and player_rect.left > 0:
                    player_rect.x -= 5
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and player_rect.right <= 800:
                    player_rect.x += 5

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                society_rect.centerx = 400
                society_rect.centery = 200
                player_rect.bottom = 300
                player_rect.centerx = 80
                xvelocity = randint(5, 10)
                yvelocity = xvelocity

    if game_active:
        screen.fill('Black')
        society_rect.x -= xvelocity
        society_rect.y -= yvelocity

        if society_rect.left <= 0:
            xvelocity = -xvelocity
        if society_rect.right >= 800:
            xvelocity = -xvelocity
        if society_rect.top <=0:
            yvelocity = -yvelocity
        if society_rect.bottom >= 400:
            yvelocity = -yvelocity

        screen.blit(society_surf, society_rect)

        screen.blit(player_surf, player_rect)

        if society_rect.colliderect(player_rect):
            game_active = False


    else:
        screen.fill('Yellow')
        
    pygame.display.update() #window se updatuje
    clock.tick(60) #fps limit #2