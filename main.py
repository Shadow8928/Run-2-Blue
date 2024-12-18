import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
s = 0
score = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 5
    if keys[pygame.K_s]:
        player_pos.y += 5
    if keys[pygame.K_a]:
        player_pos.x -= 5
    if keys[pygame.K_d]:
        player_pos.x += 5
    if player_pos.x < 40:
        player_pos.x = 40
    if player_pos.x > 1240:
        player_pos.x = 1240
    if player_pos.y < 40:
        player_pos.y = 40
    if player_pos.y > 680:
        player_pos.y = 680
    if s == 0:
        oppx = random.randint(40, 1230)
        oppy = random.randint(40, 680)
        s = 201
        score += 1
    elif s == 1:
        print(score)
        running = False
    else:
        s -= 1
    if oppx-80<player_pos.x<oppx+80 and oppy-80<player_pos.y<oppy+80:
        s = 0
    pygame.draw.circle(screen, "blue", (oppx, oppy), 40)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
