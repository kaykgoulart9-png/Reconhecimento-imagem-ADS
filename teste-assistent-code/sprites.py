# sprites.py
import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        # Posicionamento inicial
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        
        self.all_sprites = all_sprites
        self.bullets = bullets

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speedx = PLAYER_SPEED
            
        self.rect.x += self.speedx
        
        # Manter o player dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(BULLET_COLOR)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = BULLET_SPEED

    def update(self):
        self.rect.y += self.speedy
        # Destruir o sprite se sair da tela pelo topo
        if self.rect.bottom < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ASTEROID_WIDTH, ASTEROID_HEIGHT))
        self.image.fill(ASTEROID_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - ASTEROID_WIDTH)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)

    def update(self):
        self.rect.y += self.speedy
        # Não matamos o sprite se ele sair pelo fundo aqui,
        # pois precisamos verificar isso no loop principal para dar Game Over.
