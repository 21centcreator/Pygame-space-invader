#Drawing design using arrow keys in PyGame
'''
Left arrow key: Decrement in x co-ordinate
Right arrow key: Increment in x co-ordinate
Up arrow key: Decrement in y co-ordinate
Down arrow key: Increment in y co-ordinate
'''

import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

icon=pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("My pygame")
x=200
y=200

width=20
height=20
vel=10

running = True
while running:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running= False
		
	keys=pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x>0:
		x-=vel

	if keys[pygame.K_RIGHT] and x<500 - width:
		x+=vel

	if keys[pygame.K_UP] and y>0:
		y-=vel

	if keys[pygame.K_DOWN] and y<500 - height:
		y+=vel

	pygame.draw.rect(screen,(255,0,0),(x,y,width,height))

	pygame.display.update()

pygame.quit()



			
	           


	
	