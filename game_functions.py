import os

import pygame

from bullet import Bullet

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

def update_screen(infrompy_settings, screen, ship, alien, bullets ):

    screen.fill(infrompy_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()

    pygame.display.flip()

def update_bullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)