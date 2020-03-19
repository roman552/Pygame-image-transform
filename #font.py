#font
#1 пример
import pygame
pygame.init()
sc = pygame.display.set_mode((300,200))
sc.fill((255, 255, 255))
f1 = pygame.font.Font(None, 36)
text1 = f1.render('Hello Привет', 1, (180, 0, 0))
f2 = pygame.font.SysFont('serif', 48)
text2 = f2.render("World Мир", 0, (0, 180, 0))
sc.blit(text1, (10, 50))
sc.blit(text2, (10, 100))
pygame.display.update()
done = True
while done:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			done = False
			pygame.quit()

#2 пример
import pygame
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill((200, 255, 200))
font = pygame.font.Font(None, 72)
text = font.render("Hello Wold", 1, (0, 100, 0))
place = text.get_rect(center = (200, 150))
sc.blit(text, place)
pygame.display.update()
done = True
while done:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			done = False
	
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_LEFT]:
		place.x -= 1
	elif pressed[pygame.K_RIGHT]:
		place.x += 1
	sc.fill((200, 255, 200))
	sc.blit(text, place)
	pygame.display.update()
	pygame.time.delay(20)
pygame.quit()









































