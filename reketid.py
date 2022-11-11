import pygame
from random import *
must = (0,0,0)
 
class Reket(pygame.sprite.Sprite):
    def __init__(self, color, pikkus, kõrgus):
        super().__init__()
        
        self.image = pygame.Surface([pikkus, kõrgus])
        self.image.fill(must)
        self.image.set_colorkey(must)
        pygame.draw.rect(self.image, color, [0, 0, pikkus, kõrgus])
        self.rect = self.image.get_rect()
    
    #reket liigub üles alla
    def liiguÜles(self, pikslid):
        self.rect.y -= pikslid
        if self.rect.y < 0:
            self.rect.y = 0

    def liiguAlla(self, pikslid):
        self.rect.y += pikslid
        if self.rect.y > 325:
            self.rect.y = 325