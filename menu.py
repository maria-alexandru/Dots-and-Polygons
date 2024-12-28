import pygame
import sys
from button import Button

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons Menu")

# Background and fonts
BG = pygame.image.load("assets/fundal.jpg")
BASE_FONT_SIZE = 40

# Default settings
polygon_options = ["Square", "Triangle", "Mix"]
polygon_index = 0
grid_size = 5
opponent = "Player"
music_volume = 0


def draw_text(surface, text, pos, font, color="White"):
    """Helper function to draw text on the screen."""
    render = font.render(text, True, color)
    rect = render.get_rect(center=pos)
    surface.blit(render, rect)


def scale_image(image, scale_factor):
    """Redimensionează o imagine în funcție de un factor de scalare."""
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))


def create_buttons(screen_width, screen_height):
    """Creează și returnează butoanele pentru meniul principal."""
    scale_factor = min(screen_width / 1280, screen_height / 720)
    font_size = int(BASE_FONT_SIZE * scale_factor)
    font = pygame.font.SysFont("Arial", font_size)

    play_image = scale_image(pygame.image.load("assets/Play Rect.png"), scale_factor)

    polygon_button = Button(
        image=None,
        pos=(screen_width // 2, 100 + screen_height // 7),
        text_input=f"Polygon: {polygon_options[polygon_index]}",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    grid_button = Button(
        image=None,
        pos=(screen_width // 2, 100 + screen_height // 7 + int(70 * scale_factor)),
        text_input=f"Grid Size: {grid_size}",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    opponent_button = Button(
        image=None,
        pos=(screen_width // 2,100 + screen_height // 7 + int(140 * scale_factor)),
        text_input=f"Opponent: {opponent}",
        font=font,
        base_color="White",
        hovering_color="#cce378",
    )
    music_button = Button(
        image=None,
        pos=(screen_width // 2, 100 + screen_height // 7 + int(210 * scale_factor)),
        text_input=f"Music Volume: {music_volume}%",
        font=font,
        base_color="White",
        hovering_color="#cce378",
    )
    play_button = Button(
        image=play_image,
        pos=(screen_width // 2, 100 + screen_height // 7 + int(310 * scale_factor)),
        text_input="PLAY",
        font=font,
        base_color="White",
        hovering_color="#cce378",
    )
    quit_button = Button(
        image=None,
        pos=(screen_width // 2, 100 + screen_height // 7 + int(380 * scale_factor)),
        text_input="QUIT",
        font=font,
        base_color="White",
        hovering_color="#fc6f7d",
    )
    return [polygon_button, grid_button, opponent_button, music_button, play_button, quit_button]


def main_menu():
    global SCREEN, polygon_index, grid_size, opponent, music_volume
    buttons = create_buttons(SCREEN_WIDTH, SCREEN_HEIGHT)

    while True:
        SCREEN.blit(pygame.transform.scale(BG, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw title
        draw_text(
            SCREEN,
            "MAIN MENU",
            (SCREEN.get_width() // 2, int(50 * (SCREEN.get_height() / 720))),
            pygame.font.SysFont("Arial", int(70 * (SCREEN.get_width() / 1280))),
            "#b68f40",
        )

        
        # Update buttons
        for button in buttons:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                buttons = create_buttons(event.w, event.h)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].checkForInput(MENU_MOUSE_POS):  # Polygon button
                    polygon_index = (polygon_index + 1) % len(polygon_options)  # Next polygon option
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[1].checkForInput(MENU_MOUSE_POS):  # Grid button
                    grid_size = grid_size + 1 if grid_size < 10 else 5  # Increment grid size or reset
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[2].checkForInput(MENU_MOUSE_POS):  # Opponent button
                    opponent = "Computer" if opponent == "Player" else "Player"
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[3].checkForInput(MENU_MOUSE_POS):  # Music button
                    music_volume = (music_volume + 10) % 110  # Increment volume or reset
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[4].checkForInput(MENU_MOUSE_POS):  # Play button
                    print("Starting Game with Settings:")
                    print(f"Polygon: {polygon_options[polygon_index]}, Grid: {grid_size}, Opponent: {opponent}")
                    print(f"Music Volume: {music_volume}%")
                    return
                if buttons[5].checkForInput(MENU_MOUSE_POS):  # Quit button
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
