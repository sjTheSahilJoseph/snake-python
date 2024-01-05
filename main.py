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

    ball = pygame.draw.circle(screen, "white", ball_pos, 10)
    player = pygame.draw.circle(screen, "white", player_pos, 10)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_k]:
        player_pos.y -= 500 * dt
    if keys[pygame.K_j]:
        player_pos.y += 500 * dt
    if keys[pygame.K_h]:
        player_pos.x -= 500 * dt
    if keys[pygame.K_l]:
        player_pos.x += 500 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
