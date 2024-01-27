# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    ball = pygame.draw.circle(screen, "purple", ball_pos, 10)
    player = pygame.draw.circle(screen, "blue", player_pos, 10)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_k] or keys[pygame.K_UP]:
        player_pos.y -= 500 * dt
        ball_pos.y -= player_pos.y * dt
    if keys[pygame.K_j] or keys[pygame.K_DOWN]:
        player_pos.y += 500 * dt
        ball_pos.y += player_pos.y * dt
    if keys[pygame.K_h] or keys[pygame.K_LEFT]:
        player_pos.x -= 500 * dt
        ball_pos.x -= player_pos.x * dt
    if keys[pygame.K_l] or keys[pygame.K_RIGHT]:
        player_pos.x += 500 * dt
        ball_pos.x += player_pos.x * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
