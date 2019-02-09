import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, infrompy_settings, screen, ship):

        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, infrompy_settings.bullet_width, infrompy_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = infrompy_settings.bullet_color
        self.speed = infrompy_settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y


    def draw_bullet(self):
        print("Drawing bullet Bottom, Top, right, left: " 
              + str(self.rect.bottom) 
              + ", " 
              + str(self.rect.top) 
              + ", " 
              + str(self.rect.right) 
              + ", " 
              + str(self.rect.left))
              
        pygame.draw.rect(self.screen, self.color, self.rect)




