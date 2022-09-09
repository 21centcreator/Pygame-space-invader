#change window title and icon, screen fill color
import pygame

pygame.init()

screen=pygame.display.set_mode((400,600))

icon=pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("My pygame")



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running= False

	screen.fill((255,0,0))
	pygame.display.update()