#Практическая работа (модуль pygame.font)
import pygame
pygame.init()
W=500
H=500
clock=pygame.time.Clock()
FPS=60
font=pygame.font.SysFont('arial',100)
sc=pygame.display.set_mode((W,H))
text=font.render('Hello!',1,(170,200,20))
surf1=pygame.Surface((50,50))
surf2=pygame.Surface((100,100))
rect=pygame.Rect(50,100,surf2.get_size()[0],surf2.get_size()[1])


pygame.display.update()
done=True
while done:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			done=False
			pygame.quit()
	sc.fill((153,217,234))
	surf2.fill((255,255,0))
	sc.blit(surf2,(50,100))
	pos=pygame.mouse.get_pos()
	if rect.collidepoint(pos):
		sc.blit(text,(H//3,W//2))
	pygame.display.update()
	clock.tick(FPS)






















