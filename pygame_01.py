import pygame

pygame.init()
screen = pygame.display.set_mode((1000,800))  
title = pygame.display.set_caption("Ping Pong Game")
done = False
is_start = True
Paddle_Width = 20
Paddle_Height = 100
Padding = 5
Padding_height = pygame.display.get_surface().get_height() / 2 - Paddle_Height / 2

player_pos_1 = 200
player_pos_2 = 100

circle_x = 5
circle_y = 5

circle_x_vel = 7.4
circle_y_vel = 7.4

score1 = 0

score2 = 0

font = pygame.font.SysFont(None, 30)

text_size = (400, 0)
text_size2 = (510, 0)

clock = pygame.time.Clock()
soundObj = pygame.mixer.Sound("Project1\\assets\\music.mp3")
soundObj.set_volume(0.1)
soundObj.play(0)
soundObj2 = pygame.mixer.Sound("Project1\\assets\\ping_pong_paddle.mp3")
soundObj2.set_volume(1)
# Padding2 = 975
BLACK = (0,0,0)
while not done:  
    
    text = font.render(f"Score: {score1}", True, (255, 255, 255), (0,0,0))
    text1 = font.render(f"Score: {score2}", True, (255, 255, 255), (0,0,0))
    fps = font.render(f"FPS: {clock.get_fps()//1}", True, (255, 255, 255), (0,0,0))
    clock.tick(70)
    circle_x += circle_x_vel
    circle_y += circle_y_vel
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
            
        if event.type == pygame.KEYDOWN and event.key == pygame.KEYUP:
            is_start = not is_start
    screen.fill(BLACK)
            
    if circle_x >= pygame.display.get_surface().get_width():
        circle_x_vel =- circle_x_vel
        
    if circle_y >= pygame.display.get_surface().get_height():
        circle_y_vel =- circle_y_vel
        
    if circle_x <= 0:
        circle_x_vel =- circle_x_vel
        
    if circle_y <= 0:
        circle_y_vel =- circle_y_vel
        
    # print(circle_x, circle_y)
            
    # pygame.draw.rect(screen, (4, 30, 228), pygame.Rect(5, 350, 20, 100))
    # pygame.draw.rect(screen, (4, 30, 228), pygame.Rect(500, 350, 20, 100))


    circle_1 = pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 15.5, 15)
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_w]:
        player_pos_1 -= 5.0
    if pressed[pygame.K_s]:
        player_pos_1 += 5.0
        
    # if player_pos_1 >= pygame.display.get_surface().get_height():
    #     player_pos_1 = +player_pos_1
    
    if player_pos_1 + Paddle_Height > pygame.display.get_surface().get_height():
        player_pos_1 = pygame.display.get_surface().get_height() - Paddle_Height
        
    if player_pos_1 < 0:
        player_pos_1 = 0
    
    player_1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(Padding, player_pos_1, Paddle_Width, Paddle_Height))
    # print(player_pos_1)
    # pygame.draw.rect(screen, (4, 30, 228), pygame.Rect(Padding2, pygame.display.get_surface().get_height() / 2 - Paddle_Height / 2, Paddle_Width, Paddle_Height))
    
    pressed1 = pygame.key.get_pressed()
    
    if pressed1[pygame.K_UP]:
        player_pos_2 -= 5.0
    if pressed1[pygame.K_DOWN]:
        player_pos_2 += 5.0
        
    if player_pos_2 + Paddle_Height > pygame.display.get_surface().get_height():
        player_pos_2 = pygame.display.get_surface().get_height() - Paddle_Height
        
    if player_pos_2 < 0:
        player_pos_2 = 0
        
        
    player_2 = pygame.draw.rect(screen, (241, 213, 0), pygame.Rect(pygame.display.get_surface().get_width() - Padding - Paddle_Width, player_pos_2, Paddle_Width, Paddle_Height))
    # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(500, 0, 10, 1000))    
    
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 800), 3)
    
    if circle_1.colliderect(player_1):
        soundObj2.play()
        circle_x = player_1.right + 15
        circle_x_vel = -circle_x_vel
        score1 += 1
        
    if circle_1.colliderect(player_2):
        soundObj2.play()
        circle_x = player_2.left - 15
        circle_x_vel = -circle_x_vel
        score2 += 1

    screen.blit(text, text_size)
    screen.blit(text1, text_size2)
    screen.blit(fps, (880,0))
        
    
    pygame.display.flip()
    # pygame.display.update()
    # print(pygame.display.get_surface().get_width() - Padding - Paddle_Width)