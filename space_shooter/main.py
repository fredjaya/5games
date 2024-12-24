# Example "game loop" from the https://pyga.me/docs/ quick start docs
import pygame
import random

# General setup
pygame.init()

# display surface is aka screen or window, but make explicit that this is the
# base surface that other surfaces and rects are drawn on
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") # Outside of the game loop

# plain surface
surf = pygame.Surface((100, 120))
surf.fill("orange")

"""
Images to surfaces
"""
IMG_PATH = "space_shooter/images"

player_surf = pygame.image.load(f"{IMG_PATH}/player.png").convert_alpha() # speeds up blitting 
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 10)) # using a rect let's you define start pos way easier
player_x = 100

star_surf = pygame.image.load(f"{IMG_PATH}/star.png").convert_alpha()

def rand_pos():
    x = random.uniform(0, WINDOW_WIDTH)
    y = random.uniform(0, WINDOW_HEIGHT)
    return (x, y)

star_pos = [rand_pos() for _ in range(20)]

"""
Event loop - each iteration is a frame.
For each frame, poll for events (key inputs etc.)
"""
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    display_surface.fill("darkgray")

    # star
    for start_coord in star_pos:
        display_surface.blit(star_surf, start_coord)

    # player
    player_rect.left += 0.1
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()