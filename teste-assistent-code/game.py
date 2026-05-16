import pygame
import sys
from settings import *
from sprites import Player, Asteroid

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Atari Space Shooter")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player = Player(all_sprites, bullets)
    all_sprites.add(player)

    score = 0
    running = True
    game_over = False

    # Evento customizado para gerar asteroides
    SPAWN_ASTEROID = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ASTEROID, 1000) # Gerar um asteroide a cada 1 segundo (1000 ms)

    while running:
        clock.tick(FPS)

        # 1. Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                
                if event.type == SPAWN_ASTEROID:
                    asteroid = Asteroid()
                    all_sprites.add(asteroid)
                    asteroids.add(asteroid)

            else:
                # Se for Game Over, pressionar ENTER reinicia o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main()
                        return

        if not game_over:
            # 2. Update
            all_sprites.update()

            # 3. Colisões
            # Tiro acertou Asteroide
            hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
            for hit in hits:
                score += 10
            
            # Asteroide acertou a Nave
            hits = pygame.sprite.spritecollide(player, asteroids, False)
            if hits:
                game_over = True
            
            # Asteroide passou pelo fundo da tela
            for asteroid in asteroids:
                if asteroid.rect.top >= HEIGHT:
                    game_over = True

        # 4. Draw (Desenho)
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        # Pontuação
        draw_text(screen, f"Score: {score}", 30, 10, 10, WHITE)

        if game_over:
            draw_text(screen, "GAME OVER", 64, WIDTH // 2 - 150, HEIGHT // 2 - 50, RED)
            draw_text(screen, "Press ENTER to restart", 30, WIDTH // 2 - 140, HEIGHT // 2 + 30, WHITE)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
