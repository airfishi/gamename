import pygame

class Level:
    def __init__(self):

        #get the display surface

        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprites.Group()

    def run(self):
        #update and draw the game
        pass