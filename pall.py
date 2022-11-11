import pygame
from random import randint
must = (0,0,0)
class Pall(pygame.sprite.Sprite):
    
    def __init__(self, color, pikkus, kõrgus):
        super().__init__()

        self.image = pygame.Surface([pikkus, kõrgus])
        self.image.fill(must)
        self.image.set_colorkey(must)

        pygame.draw.rect(self.image, color, [0, 0, pikkus, kõrgus])
        self.velocity = [randint(4,8), 0]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def põrge(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)