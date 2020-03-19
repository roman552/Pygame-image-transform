#МОДУЛЬ PYGAME.TRANSFORM
import pygame
pygame.init()

clock=pygame.time.Clock()
FPS=60

sc=pygame.display.set_mode((400,300))
sc.fill((100,150,200))


duck_surf=pygame.image.load('C:/Users/A/Desktop/F/duck.png').convert_alpha()
duck_rect=duck_surf.get_rect(bottomright=(150,300))
sc.blit(duck_surf,duck_rect)
pygame.display.update()

pygame.time.wait(1000)
scale=pygame.transform.scale(duck_surf,(duck_surf.get_width()//2,duck_surf.get_height()//2))
scale_rect=scale.get_rect(center=(200,150))
sc.blit(scale,scale_rect)

pygame.display.update(duck_rect)
pygame.time.wait(1000)

sc.fill((100,150,200))

rot=pygame.transform.rotate(duck_surf,90)
rot_rect=rot.get_rect(center=(200,150))
sc.blit(rot,rot_rect)
pygame.display.update()
done=True
while done:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			done=False
			pygame.quit()
		elif i.type == pygame.KEYUP and i.key == pygame.K_f:

 			flip = pygame.transform.flip(duck_surf, 1, 0)
 			sc.fill((100, 150, 200))
 			sc.blit(flip, duck_rect)
 			pygame.display.update(duck_rect)

	pygame.display.update()
	clock.tick(FPS)
pygame.quit()