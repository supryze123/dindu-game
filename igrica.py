import pygame
from random import randint
from sys import exit #za gore desno X

def display_score():
    current_time = int((pygame.time.get_ticks())/1000 - start_time)
    score_surf = test_font.render(f'Score: {current_time}' , False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
#    return current_time

#def display_HighScore(current_time):
#    #current_time = int((pygame.time.get_ticks())/1000 - start_time)
#    score_surf = test_font.render(f'Your score: {current_time}' , False, (64, 64, 64))
#    score_rect = score_surf.get_rect(center = (400, 50))
#    screen.blit(score_surf, score_rect)
#   Highscore_surf = test_font.render(f'Score: {current_time}' , False, (0, 0, 0))
#    Highscore_rect = Highscore_surf.get_rect(center = (500, 250))
#    screen.blit(Highscore_surf, Highscore_rect)

xvelocity = 7
yvelocity = xvelocity 

xDimensionOfTheScreen = 800
yDimensionOfTheScreen = 480
min = 0

test_font = pygame.font.init()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
start_time = 0

pygame.init() 
screen = pygame.display.set_mode((xDimensionOfTheScreen, yDimensionOfTheScreen)) #randint(5, 10)
pygame.display.set_caption('igrica') 
clock = pygame.time.Clock() 

game_active = 1

test_surface = pygame.Surface((800,480))

krofna_surf = pygame.image.load('krofna.png').convert_alpha()
society_surf = pygame.image.load('bluebird-facingright.png').convert_alpha()
birdie_surf = pygame.image.load('bluebird-facingleft.png').convert_alpha()
society_rect = society_surf.get_rect(center = (400, 240))
#for i in range(20):
if 1:
    society1_rect = society_surf.get_rect(bottomright = (0, yDimensionOfTheScreen))
    society2_rect = society_surf.get_rect(bottomright = (0-1*34, yDimensionOfTheScreen-24*1))
    society3_rect = society_surf.get_rect(bottomright = (0-2*34, yDimensionOfTheScreen-24*2))
    society4_rect = society_surf.get_rect(bottomright = (0-3*34, 480-24*3))
    society5_rect = society_surf.get_rect(bottomright = (0-4*34, 480-24*4))
    society6_rect = society_surf.get_rect(bottomright = (0-5*34, 480-24*5))
    society7_rect = society_surf.get_rect(bottomright = (0-6*34, 480-24*6))
    society8_rect = society_surf.get_rect(bottomright = (0-7*34, 480-24*7))
    society9_rect = society_surf.get_rect(bottomright = (0-8*34, 480-24*8))
    society10_rect = society_surf.get_rect(bottomright = (0-9*34, 480-24*9))
    society11_rect = society_surf.get_rect(bottomright = (0-10*34, 480-24*10))
    society12_rect = society_surf.get_rect(bottomright = (0-11*34, 480-24*11))
    society13_rect = society_surf.get_rect(bottomright = (0-12*34, 480-24*12))
    society14_rect = society_surf.get_rect(bottomright = (0-13*34, 480-24*13))
    society15_rect = society_surf.get_rect(bottomright = (0-14*34, 480-24*14))
    society16_rect = society_surf.get_rect(bottomright = (0-15*34, 480-24*15))
    society17_rect = society_surf.get_rect(bottomright = (0-16*34, 480-24*16))
    society18_rect = society_surf.get_rect(bottomright = (0-17*34, 480-24*17))

    birdie1_rect = birdie_surf.get_rect(topleft= (800, 480))
    birdie2_rect = birdie_surf.get_rect(topleft= (800+1*34, 480+1*24))
    birdie3_rect = birdie_surf.get_rect(topleft= (800+2*34, 480+2*24))
    birdie4_rect = birdie_surf.get_rect(topleft= (800+3*34, 480+3*24))
    birdie5_rect = birdie_surf.get_rect(topleft= (800+4*34, 480+4*24))
    birdie6_rect = birdie_surf.get_rect(topleft= (800+5*34, 480+5*24))
    birdie7_rect = birdie_surf.get_rect(topleft= (800+6*34, 480+6*24))
    birdie8_rect = birdie_surf.get_rect(topleft= (800+7*34, 480+7*24))
    birdie9_rect = birdie_surf.get_rect(topleft= (800+8*34, 480+8*24))
    birdie10_rect = birdie_surf.get_rect(topleft= (800+9*34, 480+9*24))
    birdie11_rect = birdie_surf.get_rect(topleft= (800+10*34, 480+10*24))
    birdie12_rect = birdie_surf.get_rect(topleft= (800+11*34, 480+11*24))
    birdie13_rect = birdie_surf.get_rect(topleft= (800+12*34, 480+12*24))
    birdie14_rect = birdie_surf.get_rect(topleft= (800+13*34, 480+13*24))
    birdie15_rect = birdie_surf.get_rect(topleft= (800+14*34, 480+14*24))
    birdie16_rect = birdie_surf.get_rect(topleft= (800+15*34, 480+15*24))
    birdie17_rect = birdie_surf.get_rect(topleft= (800+16*34, 480+16*24))
    birdie18_rect = birdie_surf.get_rect(topleft= (800+17*34, 480+17*24))

krofna_rect = krofna_surf.get_rect(midbottom= (0, 240))
krofna_velocity = 3
player_surf = pygame.image.load('yellowbird-midflap.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

def flyInFromTheRight():
    #print("FUNCTION FLYINFROMTHERIGHT RUNNING")
    society1_rect.centerx = 0-34
    society1_rect.centery = 480-12

    society2_rect.centerx = 0-2*34
    society2_rect.centery = 480-24-12
                
    society3_rect.centerx = 0-3*34
    society3_rect.centery = 480-2*24-12

    society4_rect.centerx = 0-4*34
    society4_rect.centery = 480-3*24-12

    society5_rect.centerx = 0-5*34
    society5_rect.centery = 480-4*24-12

    society6_rect.centerx = 0-6*34
    society6_rect.centery = 480-5*24-12

    society7_rect.centerx = 0-7*34
    society7_rect.centery = 480-6*24-12

    society8_rect.centerx = 0-8*34
    society8_rect.centery = 480-7*24-12

    society9_rect.centerx = 0-9*34
    society9_rect.centery = 480-8*24-12

    society10_rect.centerx = 0-10*34
    society10_rect.centery = 480-9*24-12

    society11_rect.centerx = 0-11*34
    society11_rect.centery = 480-10*24-12

    society12_rect.centerx = 0-12*34
    society12_rect.centery = 480-11*24-12

    society13_rect.centerx = 0-13*34
    society13_rect.centery = 480-12*24-12

    society14_rect.centerx = 0-14*34
    society14_rect.centery = 480-13*24-12

    society15_rect.centerx = 0-15*34
    society15_rect.centery = 480-14*24-12

    society16_rect.centerx = 0-16*34
    society16_rect.centery = 480-15*24-12

    society17_rect.centerx = 0-17*34
    society17_rect.centery = 480-16*24-12

    society18_rect.centerx = 0-18*34
    society18_rect.centery = 480 - 17*24 -12

def flyInFromTheLeft():
    #print('FUNCTION FLYINFROMTHELEFT RUNNING')
    birdie1_rect.centerx = 800 + 1*34
    birdie1_rect.centery = 0 + 12

    birdie2_rect.centerx = 800 + 2*34
    birdie2_rect.centery = 0 + 1*24 + 12

    birdie3_rect.centerx = 800 + 3*34
    birdie3_rect.centery = 0 + 2*24 + 12

    birdie4_rect.centerx = 800 + 4*34
    birdie4_rect.centery = 0 + 3*24 + 12

    birdie5_rect.centerx = 800 + 5*34
    birdie5_rect.centery = 0 + 4*24 + 12

    birdie6_rect.centerx = 800 + 6*34
    birdie6_rect.centery = 0 + 5*24 + 12

    birdie7_rect.centerx = 800 + 7*34
    birdie7_rect.centery = 0 + 6*24 + 12

    birdie8_rect.centerx = 800 + 8*34
    birdie8_rect.centery = 0 + 7*24 + 12

    birdie9_rect.centerx = 800 + 9*34
    birdie9_rect.centery = 0 + 8*24 + 12

    birdie10_rect.centerx = 800 + 10*34
    birdie10_rect.centery = 0 + 9*24 + 12

    birdie11_rect.centerx = 800 + 11*34
    birdie11_rect.centery = 0 + 10*24 + 12

    birdie12_rect.centerx = 800 + 12*34
    birdie12_rect.centery = 0 + 11*24 + 12

    birdie13_rect.centerx = 800 + 13*34
    birdie13_rect.centery = 0 + 12*24 + 12

    birdie14_rect.centerx = 800 + 14*34
    birdie14_rect.centery = 0 + 13*24 + 12

    birdie15_rect.centerx = 800 + 15*34
    birdie15_rect.centery = 0 + 14*24 + 12

    birdie16_rect.centerx = 800 + 16*34
    birdie16_rect.centery = 0 + 15*24 + 12

    birdie17_rect.centerx = 800 + 17*34
    birdie17_rect.centery = 0 + 16*24 + 12

    birdie18_rect.centerx = 800 + 18*34
    birdie18_rect.centery = 0 + 17*24 + 12

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
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and player_rect.bottom <= 480:
                    player_rect.y += 5
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and player_rect.left > 0:
                    player_rect.x -= 5
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and player_rect.right <= 800:
                    player_rect.x += 5
                #if (event.key == pygame.K_w and event.key == pygame.K_a) and player_rect.top > 0 and player_rect.left >0:
                #    player_rect.y -= 5
                #    player_rect.x -= 5

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                start_time = int(pygame.time.get_ticks()/1000)
                society_rect.centerx = 480
                society_rect.centery = 200
                player_rect.bottom = 300
                player_rect.centerx = 80

                flyInFromTheRight()
                #flyInFromTheLeft()
                
                birdie1_rect.centerx = 800 + 1*34 + 500
                birdie1_rect.centery = 0 + 12

                birdie2_rect.centerx = 800 + 2*34 + 500
                birdie2_rect.centery = 0 + 1*24 + 12

                birdie3_rect.centerx = 800 + 3*34 + 500
                birdie3_rect.centery = 0 + 2*24 + 12

                birdie4_rect.centerx = 800 + 4*34 + 500
                birdie4_rect.centery = 0 + 3*24 + 12

                birdie5_rect.centerx = 800 + 5*34 + 500
                birdie5_rect.centery = 0 + 4*24 + 12

                birdie6_rect.centerx = 800 + 6*34 + 500
                birdie6_rect.centery = 0 + 5*24 + 12

                birdie7_rect.centerx = 800 + 7*34 + 500
                birdie7_rect.centery = 0 + 6*24 + 12

                birdie8_rect.centerx = 800 + 8*34 + 500
                birdie8_rect.centery = 0 + 7*24 + 12

                birdie9_rect.centerx = 800 + 9*34 + 500
                birdie9_rect.centery = 0 + 8*24 + 12

                birdie10_rect.centerx = 800 + 10*34 + 500
                birdie10_rect.centery = 0 + 9*24 + 12

                birdie11_rect.centerx = 800 + 11*34 + 500
                birdie11_rect.centery = 0 + 10*24 + 12

                birdie12_rect.centerx = 800 + 12*34 + 500
                birdie12_rect.centery = 0 + 11*24 + 12

                birdie13_rect.centerx = 800 + 13*34 + 500
                birdie13_rect.centery = 0 + 12*24 + 12

                birdie14_rect.centerx = 800 + 14*34 + 500
                birdie14_rect.centery = 0 + 13*24 + 12

                birdie15_rect.centerx = 800 + 15*34 + 500
                birdie15_rect.centery = 0 + 14*24 + 12

                birdie16_rect.centerx = 800 + 16*34 + 500
                birdie16_rect.centery = 0 + 15*24 + 12

                birdie17_rect.centerx = 800 + 17*34 + 500
                birdie17_rect.centery = 0 + 16*24 + 12

                birdie18_rect.centerx = 800 + 18*34 + 500
                birdie18_rect.centery = 0 + 17*24 + 12

                xvelocity = randint(5, 10)
                yvelocity = xvelocity
                game_active = True

    if game_active:
        screen.fill('Black')
        display_score()
        society_rect.x -= xvelocity
        society_rect.y -= yvelocity
        krofna_rect.x += krofna_velocity

        flyInVelocity = 6
        society1_rect.x += flyInVelocity
        society2_rect.x += flyInVelocity
        society3_rect.x += flyInVelocity
        society4_rect.x += flyInVelocity
        society5_rect.x += flyInVelocity
        society6_rect.x += flyInVelocity
        society7_rect.x += flyInVelocity
        society8_rect.x += flyInVelocity
        society9_rect.x += flyInVelocity
        society10_rect.x += flyInVelocity
        society11_rect.x += flyInVelocity
        society12_rect.x += flyInVelocity
        society13_rect.x += flyInVelocity
        society14_rect.x += flyInVelocity
        society15_rect.x += flyInVelocity
        society16_rect.x += flyInVelocity
        society17_rect.x += flyInVelocity
        society18_rect.x += flyInVelocity

        birdie1_rect.x -= flyInVelocity
        birdie2_rect.x -= flyInVelocity
        birdie3_rect.x -= flyInVelocity
        birdie4_rect.x -= flyInVelocity
        birdie5_rect.x -= flyInVelocity
        birdie6_rect.x -= flyInVelocity
        birdie7_rect.x -= flyInVelocity
        birdie8_rect.x -= flyInVelocity
        birdie9_rect.x -= flyInVelocity
        birdie10_rect.x -= flyInVelocity
        birdie11_rect.x -= flyInVelocity
        birdie12_rect.x -= flyInVelocity
        birdie13_rect.x -= flyInVelocity
        birdie14_rect.x -= flyInVelocity
        birdie15_rect.x -= flyInVelocity
        birdie16_rect.x -= flyInVelocity
        birdie17_rect.x -= flyInVelocity
        birdie18_rect.x -= flyInVelocity

        if society_rect.left <= 0:
            xvelocity += 1
            xvelocity = -xvelocity
            #xvelocity = -randint(5,10)
            
        if society_rect.right >= 800:
            xvelocity -= 1
            xvelocity = -xvelocity
            #xvelocity = randint(5,10)

        if society_rect.top <=0:
            yvelocity += 1
            yvelocity = -yvelocity
            #yvelocity = -randint(5,10)

        if society_rect.bottom >= 480:
            yvelocity -= 1
            yvelocity = -yvelocity
            #yvelocity = randint(5,10)

        screen.blit(society_surf, society_rect)

        screen.blit(player_surf, player_rect)

        screen.blit(krofna_surf, krofna_rect)

        if society18_rect.x >= 800+flyInVelocity*60*randint(1, 5):
            flyInFromTheRight()
        if birdie18_rect.x <= 0-flyInVelocity*60*3:
            flyInFromTheLeft()
        
        screen.blit(society_surf, society1_rect)
        screen.blit(society_surf, society2_rect)
        screen.blit(society_surf, society3_rect)
        screen.blit(society_surf, society4_rect)
        screen.blit(society_surf, society5_rect)
        screen.blit(society_surf, society6_rect)
        screen.blit(society_surf, society7_rect)
        screen.blit(society_surf, society8_rect)
        screen.blit(society_surf, society9_rect)
        screen.blit(society_surf, society10_rect)
        screen.blit(society_surf, society11_rect)
        screen.blit(society_surf, society12_rect)
        screen.blit(society_surf, society13_rect)
        screen.blit(society_surf, society14_rect)
        screen.blit(society_surf, society15_rect)
        screen.blit(society_surf, society16_rect)
        screen.blit(society_surf, society17_rect)
        screen.blit(society_surf, society18_rect)

        screen.blit(birdie_surf, birdie1_rect)
        screen.blit(birdie_surf, birdie2_rect)
        screen.blit(birdie_surf, birdie3_rect)
        screen.blit(birdie_surf, birdie4_rect)
        screen.blit(birdie_surf, birdie5_rect)
        screen.blit(birdie_surf, birdie6_rect)
        screen.blit(birdie_surf, birdie7_rect)
        screen.blit(birdie_surf, birdie8_rect)
        screen.blit(birdie_surf, birdie9_rect)
        screen.blit(birdie_surf, birdie10_rect)
        screen.blit(birdie_surf, birdie11_rect)
        screen.blit(birdie_surf, birdie12_rect)
        screen.blit(birdie_surf, birdie13_rect)
        screen.blit(birdie_surf, birdie14_rect)
        screen.blit(birdie_surf, birdie15_rect)
        screen.blit(birdie_surf, birdie16_rect)
        screen.blit(birdie_surf, birdie17_rect)
        screen.blit(birdie_surf, birdie18_rect)


        #
        
        if krofna_rect.colliderect(player_rect):
        #    print("KROFNA KOLIZIJA")
        #    print('xvel je ', xvelocity)
        #    print('yvel je ', yvelocity)

            if xvelocity > 10:
                xvelocity = 5

            if yvelocity > 10:
                yvelocity = 5

            if xvelocity < -10:
                xvelocity = -5

            if yvelocity < -10:
                yvelocity = -5
            krofna_rect.centerx = -180
        
        if krofna_rect.centerx >= 800:
            krofna_rect.centerx = -180
#            krofna_rect.centerx = xDimensionOfTheScreen + 50
#            krofna_rect.centery = yDimensionOfTheScreen + 50
#
#        if not(KrofnaOnScreen) == 1:
#            KrofnaSpeedRed()

        if society_rect.colliderect(player_rect) or society1_rect.colliderect(player_rect) or society2_rect.colliderect(player_rect) or society3_rect.colliderect(player_rect) or society4_rect.colliderect(player_rect) or society5_rect.colliderect(player_rect) or society6_rect.colliderect(player_rect) or society7_rect.colliderect(player_rect) or society8_rect.colliderect(player_rect) or society9_rect.colliderect(player_rect) or society10_rect.colliderect(player_rect) or society11_rect.colliderect(player_rect) or society12_rect.colliderect(player_rect) or society13_rect.colliderect(player_rect) or society14_rect.colliderect(player_rect) or society15_rect.colliderect(player_rect) or society16_rect.colliderect(player_rect) or society17_rect.colliderect(player_rect) or society18_rect.colliderect(player_rect) or birdie1_rect.colliderect(player_rect) or birdie2_rect.colliderect(player_rect) or birdie3_rect.colliderect(player_rect) or birdie4_rect.colliderect(player_rect) or birdie5_rect.colliderect(player_rect) or birdie6_rect.colliderect(player_rect) or birdie7_rect.colliderect(player_rect) or birdie8_rect.colliderect(player_rect) or birdie9_rect.colliderect(player_rect) or birdie10_rect.colliderect(player_rect) or birdie11_rect.colliderect(player_rect) or birdie12_rect.colliderect(player_rect) or birdie13_rect.colliderect(player_rect) or birdie14_rect.colliderect(player_rect) or birdie15_rect.colliderect(player_rect) or birdie16_rect.colliderect(player_rect) or birdie17_rect.colliderect(player_rect) or birdie18_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Blue')
        #display_HighScore(display_score)

    pygame.display.update() #window se updatuje
    clock.tick(60) #fps limit #2
