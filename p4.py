#key events
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
		if event.type == pygame.KEYDOWN:
			#print("A key has been pressed")
			if event.key == pygame.K_w:
				print("Key w has been pressed")
			if event.key == pygame.K_a:
				print("Key a has been pressed")
			if event.key == pygame.K_d:
				print("Key d has been pressed")
			if event.key == pygame.K_s:
				print("Key s has been pressed")
			
	           


	screen.fill((255,0,0))
	pygame.draw.rect(screen,(0,0,255),[100,100,400,100],0)
	#filled rectangle
	pygame.draw.rect(screen,(0,0,255),[100,100,400,100],2)
	#circle
	pygame.draw.circle(screen,(0,255,0),[300,300],100,3)
	#line
	pygame.draw.line(screen,(0,0,0),[100,400],[500,400],5)
	pygame.display.update()