#drawing shapes

import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))

icon=pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("My pygame")



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running= False


	screen.fill((255,0,0))
	pygame.draw.rect(screen,(0,0,255),[100,100,400,100],3)
	#filled rectangle
	pygame.draw.rect(screen,(0,0,255),[150,150,200,50],2)
	#circle
	pygame.draw.circle(screen,(0,255,0),[300,300],100,0)
	#line
	pygame.draw.line(screen,(120,220,10),[100,400],[500,400],5)
	pygame.display.update()