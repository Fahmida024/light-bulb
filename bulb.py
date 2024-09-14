import pygame
import time
pygame.init()
playing=True
screen=pygame.display.set_mode([500,600])
img1=pygame.image.load('img1.jpg')
img2=pygame.image.load('img2.jpg')



while playing:
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
            playing=False
         if event.type==pygame.MOUSEBUTTONDOWN:
             screen.blit(img1,(0,0))
             pygame.display.update()
         if event.type==pygame.MOUSEBUTTONUP:
             screen.blit(img2,(0,0))
             pygame.display.update()
         

             
        

