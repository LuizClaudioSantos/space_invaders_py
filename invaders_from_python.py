import sys

import pygame 
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from settings import Settings

def run_game():
    pygame.init()
    infrompy_settings = Settings()
    screen = pygame.display.set_mode((infrompy_settings.screen_width, infrompy_settings.screen_height))
    pygame.display.set_caption("Invaders from python")

    alien = Alien(infrompy_settings, screen)

    ship = Ship(infrompy_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(infrompy_settings, screen, ship, aliens)

    while True:
        gf.check_events(infrompy_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(infrompy_settings, screen, ship, aliens, bullets)


run_game()
