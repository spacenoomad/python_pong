import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode([800, 500])

running = True
executable = True

player_y = 200
enemy_y = 200

direction = 1
ball_x = 400
ball_y = 250
ball_speed_x = 2
ball_speed_y = 4

from time import time, sleep
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((0, 0, 0))
	
	while executable == True:
		pick = random.randint(0, 1)
		if pick == 0:
			direction = 1
		else:
			direction = -1
		ball_speed_x *= direction
		executable = False
	
	pygame.draw.rect(screen, (255, 255, 255), (30, player_y, 15, 100))
	pygame.draw.rect(screen, (255, 255, 255), (755, enemy_y, 15, 100))
	
	pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 7)
	
	
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_w:
			if player_y > 0:
				player_y -= 3
		elif event.key == pygame.K_s:
			if player_y < 400:
				player_y += 3
	
	if ball_y > 490:
		ball_speed_y = -1
		ball_speed_x = random.randint(-4, 4)
	elif ball_y < 0:
		ball_speed_y = 1
		ball_speed_x = random.randint(-4, 4)
		
	if ball_x < 0 or ball_x > 800:
		running = False
	
	if ball_x < 42 and ball_y > player_y and ball_y < player_y + 100:
		ball_speed_x = 1
		ball_speed_y = random.randint(-4, 4)
		
	if ball_x > 753 and ball_y > enemy_y and ball_y < enemy_y + 100:
		ball_speed_x = -1
		ball_speed_y = random.randint(-4, 4)
		
	if ball_x > 400:
		if ball_y > enemy_y:
			enemy_y += 5
		if ball_y < enemy_y + 100:
			enemy_y -= 5
		
	
	
	pygame.display.flip()
	
	
	sleep(0.01 - time() % 0.01)
	ball_x += ball_speed_x
	ball_y += ball_speed_y
	
	
pygame.quit()
