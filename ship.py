import pygame

class Ship():

    def __init__(self, infrompy_settings, screen):

        self.screen = screen
        self.infrompy_settings = infrompy_settings

		# Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

		# Lecture_011: Store a decimal value for the center of the ship
        self.center = float(self.rect.centerx)

		# Movement Flag of Lecture_009
        self.moving_right = False

		# Lecture_010
        self.moving_left = False

       
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.infrompy_settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.infrompy_settings.ship_speed 
        self.rect.centerx = self.center           

    def blitme(self):
        print("Bliting ship Bottom, Top, right, left: " 
              + str(self.rect.bottom) 
              + ", " 
              + str(self.rect.top) 
              + ", " 
              + str(self.rect.right) 
              + ", " 
              + str(self.rect.left))
        self.screen.blit(self.image, self.rect)

