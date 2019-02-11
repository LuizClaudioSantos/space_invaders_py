import os

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, infrompy_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(infrompy_settings, screen, ship)      
        bullets.add(new_bullet) 

def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False    

def check_events(infrompy_settings, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(1)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, infrompy_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)   

def update_screen(infrompy_settings, screen, ship, aliens, bullets ):

    screen.fill(infrompy_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def update_bullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(infrompy_settings, screen, ship, aliens):
    alien = Alien(infrompy_settings, screen)
    number_aliens_x = get_number_aliens_x(infrompy_settings, alien.rect.width)
    number_rows = get_number_rows(infrompy_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(infrompy_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(infrompy_settings, alien_width):
    available_space_x = infrompy_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return  number_aliens_x 

def create_alien(infrompy_settings, screen, aliens, alien_number, row_number):
    alien = Alien(infrompy_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(infrompy_settings, ship_height, alien_height):
    available_space_y = (infrompy_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows
