
import pygame
import math
import colorsys

pygame.init()

# Window
WIDTH = 600
HEIGHT = 600

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Rainbow ASCII Art")

clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)

# Settings
spacing = 8
interaction_radius = 80
repulsion_speed = 4
return_speed = 2

# Create rainbow points
points = []

for y in range(0, HEIGHT, spacing):
    for x in range(0, WIDTH, spacing):

        hue = x / WIDTH
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

        color = (
            int(r * 255),
            int(g * 255),
            int(b * 255)
        )

        character = font.render(".", True, color)

        points.append({
            "home_x": x,
            "home_y": y,
            "x": float(x),
            "y": float(y),
            "character": character
        })

# Main loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill(BLACK)

    for point in points:

        dx = mouse_x - point["x"]
        dy = mouse_y - point["y"]

        dis = math.sqrt(dx**2 + dy**2)

        # Mouse repulsion
        if 0 < dis <= interaction_radius:

            ux = dx / dis
            uy = dy / dis

            point["x"] -= ux * repulsion_speed
            point["y"] -= uy * repulsion_speed

        # Return to home
        else:

            home_dx = point["home_x"] - point["x"]
            home_dy = point["home_y"] - point["y"]

            home_dis = math.sqrt(home_dx**2 + home_dy**2)

            if home_dis > 0:

                home_ux = home_dx / home_dis
                home_uy = home_dy / home_dis

                step = min(return_speed, home_dis)

                point["x"] += home_ux * step
                point["y"] += home_uy * step

        # Draw each point
        character = point["character"]

        rect = character.get_rect(
            center=(int(point["x"]), int(point["y"]))
        )

        screen.blit(character, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
