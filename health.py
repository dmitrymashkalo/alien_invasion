import pygame
from pygame.sprite import Sprite


class Health(Sprite):
    """ Class for helth displaying"""

    def __init__(self):
        super().__init__()
        
        # Load and transform image
        self.image = pygame.image.load('images/health.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
