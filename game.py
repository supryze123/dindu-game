import pygame
from random import randint
from sys import exit #za gore desno X
import pyautogui

WIDTH = pyautogui.size()[0]
HEIGHT = pyautogui.size()[1] - 50

NUMBER_OF_THE_COLOR_FOR_THE_TEXT_SAYING_SCORE = 64

def display_score():
    current_time = int((pygame.time.get_ticks())/1000 - start_time)
    font_for_the_score = test_font.render(f'Score: {current_time}' , False, (NUMBER_OF_THE_COLOR_FOR_THE_TEXT_SAYING_SCORE, NUMBER_OF_THE_COLOR_FOR_THE_TEXT_SAYING_SCORE, NUMBER_OF_THE_COLOR_FOR_THE_TEXT_SAYING_SCORE))
    score_rect = font_for_the_score.get_rect(center = (WIDTH/2, HEIGHT/10))
    screen.blit(font_for_the_score, score_rect)

velocity_on_the_x_axis_of_the_alternating_bird = 7        # xvelocity
velocity_on_the_y_axis_of_the_alternating_bird = velocity_on_the_x_axis_of_the_alternating_bird 

test_font = pygame.font.init()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
start_time = 0

pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('igrica') 
clock = pygame.time.Clock() 

game_active = 1

test_surface = pygame.Surface((WIDTH, HEIGHT))

the_pick_up_formerly_known_as_donut_texture = pygame.image.load('krofna.png').convert_alpha()      
bird_facing_right_texture = pygame.image.load('bluebird-facingright.png').convert_alpha() ############## 34 x 24 
bird_facing_left_texture = pygame.image.load('bluebird-facingleft.png').convert_alpha() ################ 34 x 24 

alternating_bird_rectangle = bird_facing_right_texture.get_rect(center = (WIDTH, HEIGHT))

if 1:          
    society_rects = {}  #dictionary containing the birds flying from left to right
    number_of_vertical_birds_based_on_the_screen_resolution = round(HEIGHT/24) - 3
    for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):
        x_position = 0 - (iterator+1) * 34
        y_position = HEIGHT - 24 * (iterator+1)
        
        #dynamic variable name creation
        variable_name = f"society_{iterator}_rect"
        
        #storing the rect in the dict
        society_rect = bird_facing_right_texture.get_rect(bottomright=(x_position, y_position))
        society_rects[variable_name] = society_rect

    birdie_rects = {}
    
    for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):
        x_position = WIDTH + iterator * 34
        y_position = HEIGHT + iterator * 24
    
        variable_name = f"birdie_{iterator}_rect"
        
        birdie_rect = bird_facing_left_texture.get_rect(bottomright=(x_position, y_position))
        birdie_rects[variable_name] = birdie_rect

krofna_rect = the_pick_up_formerly_known_as_donut_texture.get_rect(midbottom= (0, HEIGHT/2))
krofna_velocity = 3
player_surf = pygame.image.load('yellowbird-midflap.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

def flyInFromTheRight():
    print("FUNCTION FLYINFROMTHERIGHT RUNNING")
    for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):  # Assuming you have 18 society_rects in total
            society_rects[f"society_{iterator}_rect"].x = 0 - (iterator+1) * 34
            society_rects[f"society_{iterator}_rect"].y = HEIGHT - 24/2 - iterator * 24 ######### 24/2 

def flyInFromTheLeft():
    print('FUNCTION FLYINFROMTHELEFT RUNNING')
    for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):  # Assuming you have 18 society_rects in total
            birdie_rects[f"birdie_{iterator}_rect"].x = WIDTH + (iterator+1) * 34
            birdie_rects[f"birdie_{iterator}_rect"].y = 24/2 + 24 * (iterator+1) ######### 24/2

pygame.key.set_repeat(10, 10)
while True: 
    for event in pygame.event.get():         #PLAYER INPUT
        if event.type == pygame.QUIT: #exit da radi 
            pygame.quit()
            exit()
            
        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and player_rect.top > 0 :
                    player_rect.y -= 5
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and player_rect.bottom <= HEIGHT:
                    player_rect.y += 5
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and player_rect.left > 0:
                    player_rect.x -= 5
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and player_rect.right <= WIDTH:
                    player_rect.x += 5

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                
                start_time = int(pygame.time.get_ticks()/1000)
                alternating_bird_rectangle.centerx = HEIGHT
                alternating_bird_rectangle.centery = WIDTH/4
                player_rect.bottom = 300
                player_rect.centerx = 80

                flyInFromTheRight()
                
                for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):  # Assuming you have 18 society_rects in total
                    birdie_rects[f"birdie_{iterator}_rect"].centerx = WIDTH + (iterator+1) * 34 + 500
                    birdie_rects[f"birdie_{iterator}_rect"].centery = 0 + (2*iterator+1) * 24/2 ######### 24/2
 
                velocity_on_the_x_axis_of_the_alternating_bird = randint(5, 20)
                yvelocity = velocity_on_the_x_axis_of_the_alternating_bird
                game_active = True

    if game_active:
        screen.fill('Black')
        display_score()
        alternating_bird_rectangle.x -= velocity_on_the_x_axis_of_the_alternating_bird
        alternating_bird_rectangle.y -= velocity_on_the_y_axis_of_the_alternating_bird
        krofna_rect.x += krofna_velocity

        velocity_at_which_vertical_birds_fly_into_the_screen = 15

        for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):  # Assuming you have 18 society_rects in total
            society_rects[f"society_{iterator}_rect"].x += velocity_at_which_vertical_birds_fly_into_the_screen

        for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):
            birdie_rects[f"birdie_{iterator}_rect"].x -= velocity_at_which_vertical_birds_fly_into_the_screen

        if alternating_bird_rectangle.left <= 0:
            velocity_on_the_x_axis_of_the_alternating_bird += randint(5,10) #3 
            velocity_on_the_x_axis_of_the_alternating_bird = -velocity_on_the_x_axis_of_the_alternating_bird
            
        if alternating_bird_rectangle.right >= WIDTH:
            velocity_on_the_x_axis_of_the_alternating_bird -= randint(5,10)#3
            velocity_on_the_x_axis_of_the_alternating_bird = -velocity_on_the_x_axis_of_the_alternating_bird

        if alternating_bird_rectangle.top <=0:
            velocity_on_the_y_axis_of_the_alternating_bird += randint(5, 10)#3
            velocity_on_the_y_axis_of_the_alternating_bird = -velocity_on_the_y_axis_of_the_alternating_bird

        if alternating_bird_rectangle.bottom >= HEIGHT:
            velocity_on_the_y_axis_of_the_alternating_bird -= randint(5, 10)#3
            velocity_on_the_y_axis_of_the_alternating_bird = -velocity_on_the_y_axis_of_the_alternating_bird

        screen.blit(bird_facing_right_texture, alternating_bird_rectangle)  #PTICA KOJA RANDOM
        screen.blit(player_surf, player_rect)    #PLAYER
        screen.blit(the_pick_up_formerly_known_as_donut_texture, krofna_rect)    #KROFNA

        if society_rects[f"society_{number_of_vertical_birds_based_on_the_screen_resolution-2}_rect"].x >= WIDTH + velocity_at_which_vertical_birds_fly_into_the_screen*60*randint(1, 5):
            flyInFromTheRight()
        if birdie_rects[f"birdie_{number_of_vertical_birds_based_on_the_screen_resolution-2}_rect"].x <= 0 - velocity_at_which_vertical_birds_fly_into_the_screen*60*3:
            flyInFromTheLeft()
        
        for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):
            screen.blit(bird_facing_right_texture, society_rects[f"society_{iterator}_rect"])

        for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution):
            screen.blit(bird_facing_left_texture, birdie_rects[f"birdie_{iterator}_rect"])

        if krofna_rect.colliderect(player_rect):

            if velocity_on_the_x_axis_of_the_alternating_bird > 15:
                velocity_on_the_x_axis_of_the_alternating_bird = 5

            if velocity_on_the_y_axis_of_the_alternating_bird > 15:
                velocity_on_the_y_axis_of_the_alternating_bird = 5

            if velocity_on_the_x_axis_of_the_alternating_bird < -15:
                velocity_on_the_x_axis_of_the_alternating_bird = -5

            if velocity_on_the_y_axis_of_the_alternating_bird < -15:
                velocity_on_the_y_axis_of_the_alternating_bird = -5
            krofna_rect.centerx = -180
        
        if krofna_rect.centerx >= WIDTH:
            krofna_rect.centerx = -180
    
        colliders = [society_rects[f"society_{iterator}_rect"] for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution)] + [birdie_rects[f"birdie_{iterator}_rect"] for iterator in range(number_of_vertical_birds_based_on_the_screen_resolution)]

        if any(rect.colliderect(player_rect) for rect in colliders):
            game_active = False
        
    else:
        screen.fill('Blue')

    pygame.display.update() 
    clock.tick(60) #fps limit 
