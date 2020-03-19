#МОДУЛЬ PYGAME.IMAGE 
import pygame
pygame.init()

clock=pygame.time.Clock()
FPS=60

sc=pygame.display.set_mode((400,300))
sc.fill((100,150,200))
guy_surf=pygame.image.load('C:/Users/A/Desktop/F/test.bmp').convert()
guy_surf.set_colorkey((255,255,255))
guy_rect=guy_surf.get_rect(bottomright=(400,300))
sc.blit(guy_surf,guy_rect)

duck_surf=pygame.image.load('C:/Users/A/Desktop/F/duck.png').convert_alpha()
duck_rect=duck_surf.get_rect(bottomright=(150,300))
sc.blit(duck_surf,duck_rect)
pygame.display.update()
done=True
while done:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			done=False
			pygame.quit()

	pygame.display.update()
	clock.tick(FPS)
pygame.quit()