import random
import pygame


pygame.init()

win = pygame.display.set_mode((300,300))

pygame.display.set_caption("Color Ball")

# Attributes of Circle
cir_x = 150
cir_y = 150

rad = 15
vel = 5

r = 255
b = 255
g = 255

#Attributes of Dot
dot_x = random.randint(15,285)
dot_y = random.randint(15,285)

r1 = random.randint(0,255)
b1 = random.randint(0,255)
g1 = random.randint(0,255)

beep = pygame.mixer.Sound("beep.wav")


run = True

while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and (cir_x - rad > 0):
        cir_x -= vel
    
    if keys[pygame.K_RIGHT] and (cir_x + rad < 300):
        cir_x += vel
        
    
    if keys[pygame.K_UP] and (cir_y - rad > 0):
        cir_y -= vel
    if keys[pygame.K_DOWN] and (cir_y + rad < 300):
        cir_y += vel
        
    win.fill((0,0,0))
    pygame.draw.circle(win,(r,b,g),(cir_x,cir_y),rad)
    
    
    pygame.draw.circle(win,(r1,b1,g1),(dot_x,dot_y),10)
    
    dif_x = dot_x - cir_x
    dif_y = dot_y - cir_y
    
    if (dif_x < rad and dif_x > -rad) and (dif_y < rad and dif_y > -rad):
        
        pygame.mixer.Sound.play(beep)
        
        r = r1
        b = b1
        g = g1
        
        r1 = random.randint(0,255)
        b1 = random.randint(0,255)
        g1 = random.randint(0,255)
    
        dot_x = random.randint(15,285)
        dot_y = random.randint(15,285)
    
    pygame.display.update()
    
pygame.quit()
            
            

