import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Убегай от наковален!!!")


background_image = pygame.image.load("d:/Игра python/background.png")
player_img = pygame.image.load("d:/Игра python/player_1.png")
fall_item_img = pygame.image.load("d:/Игра python/fall_items.png")


player = pygame.Rect(350, 500, 50, 50)
fall_items = []
speed = 7
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 24)
game_over = False


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if not game_over:


        keys = pygame.key.get_pressed()
        player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed

       
        player.x = max(0, min(player.x, 750))

       
        if random.random() < 0.05:
            fall_items.append(pygame.Rect(random.randint(0, 750), 0, 50, 50))


        for item in fall_items[:]:
            item.y += speed
            if item.y > 600:
                fall_items.remove(item)
                score += 1
            elif item.colliderect(player):
                game_over = True 

   
    screen.blit(background_image, (0, 0))
    screen.blit(player_img, player)
    for item in fall_items:
        screen.blit(fall_item_img, item)
    
    
    screen.blit(font.render(f"Количество очков: {score}", True, (235, 52, 152)), (10, 20))
    if game_over:
        screen.blit(font.render("Игра Закончена", True, (235, 52, 152)), (320, 180))
        pygame.display.flip()
        pygame.time.delay(2000)  
        running = False


    pygame.display.flip()
    clock.tick(60)


pygame.quit()