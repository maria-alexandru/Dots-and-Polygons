import pygame
import sys
from button import Button

pygame.init()
pygame.mixer.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons")

# Background and fonts
BG = pygame.image.load("assets/fundal.jpg")
BASE_FONT_SIZE = 20

# Default settings
polygon_options = ["Square", "Triangle", "Mix"]
polygon_index = 0
grid_size = 7
opponent = "Player"

button_sound = pygame.mixer.Sound('assets/click-234708.mp3')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def draw_text(surface, text, pos, font, color="White"):
    """Helper function to draw text on the screen."""
    render = font.render(text, True, color)
    rect = render.get_rect(center=pos)
    surface.blit(render, rect)


def scale_image(image, scale_factor):
    """Redimensioneaza o imagine in functie de un factor de scalare."""
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))


def create_buttons(screen_width, screen_height):
    """Creeaza si returneaza butoanele pentru meniul principal."""
    scale_factor = min(screen_width / 1280, screen_height / 720)
    font_size = int(BASE_FONT_SIZE * scale_factor)
    font = get_font(font_size)

    original_image = pygame.image.load("assets/Play Rect.png")
    resized_image1 = pygame.transform.scale(original_image, (165, 75))
    resized_image2 = pygame.transform.scale(original_image, (360, 75))

    play_image = scale_image(resized_image1, scale_factor)
    opponent_image = scale_image(resized_image2, scale_factor)
    grid_image = scale_image(resized_image2, scale_factor)
    polygon_image = scale_image(resized_image2, scale_factor)
    menu_image = scale_image(resized_image2, scale_factor)

    title_button_spacing = int(screen_height * 0.25)
    

    grid_button = Button(
        image=grid_image,
        pos=(screen_width // 2, title_button_spacing + int(90 * scale_factor)),
        text_input=f"Grid Size: {grid_size}",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )

    polygon_button = Button(
        image=polygon_image,
        pos=(screen_width // 2, title_button_spacing + int(185 * scale_factor)),
        text_input=f"Polygon: {polygon_options[polygon_index]}",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    
    opponent_button = Button(
        image=opponent_image,
        pos=(screen_width // 2, title_button_spacing + int(280 * scale_factor)),
        text_input=f"Opponent: {opponent}",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )

    menu_button = Button(
        image=menu_image,
        pos=(screen_width // 2, title_button_spacing + int(375 * scale_factor)),
        text_input=f"BACK TO MENU",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    
    return [polygon_button, grid_button, opponent_button, menu_button]


def settings_menu():
    global SCREEN, polygon_index, grid_size, opponent, music_volume, theme_id

    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())

    while True:
        SCREEN.blit(pygame.transform.scale(BG, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw title
        draw_text(
            SCREEN,
            "GAME SETTINGS",
            (SCREEN.get_width() // 2, int(120 * (SCREEN.get_height() / 720))),
            get_font(int(70 * (SCREEN.get_width() / 1280))),
            "White",
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
                    button_sound.play()
                    polygon_index = (polygon_index + 1) % len(polygon_options)  # Next polygon option
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[1].checkForInput(MENU_MOUSE_POS):  # Grid button
                    button_sound.play()
                    grid_size = grid_size + 1 if grid_size < 10 else 7  # Increment grid size or reset
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[2].checkForInput(MENU_MOUSE_POS):  # Opponent button
                    button_sound.play()
                    opponent = "Computer" if opponent == "Player" else "Player"
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[3].checkForInput(MENU_MOUSE_POS):  # Back to Menu button
                    from menu import set_options
                    set_options(grid_size, polygon_index, opponent)
                    from menu import main_menu
                    main_menu()
        pygame.display.update()

def run_settings():
    settings_menu()

