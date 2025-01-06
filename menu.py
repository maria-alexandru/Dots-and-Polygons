import pygame
import sys
from button import Button
import game_manager

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
grid_size = 5
opponent = "Player"
music_volume = 20
theme_options = ["1", "2", "3"]
theme_id = 0

# Load and play background music
pygame.mixer.music.load("assets/Two Gong Fire - Ryan McCaffrey_Go By Ocean.mp3")
pygame.mixer.music.set_volume(music_volume / 100)
pygame.mixer.music.play(-1)

button_sound = pygame.mixer.Sound('assets/click-234708.mp3')

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def draw_text(surface, text, pos, font, color="White"):
    render = font.render(text, True, color)
    rect = render.get_rect(center=pos)
    surface.blit(render, rect)

# resize an image according to a scale factor
def scale_image(image, scale_factor):
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))


def create_buttons(screen_width, screen_height):
    scale_factor = min(screen_width / 1280, screen_height / 720)
    font_size = int(BASE_FONT_SIZE * scale_factor)
    font = get_font(font_size)

    original_image = pygame.image.load("assets/Play Rect.png")
    resized_image1 = pygame.transform.scale(original_image, (165, 75))
    resized_image2 = pygame.transform.scale(original_image, (360, 75))

    play_image = scale_image(resized_image1, scale_factor)
    music_image = scale_image(resized_image2, scale_factor)
    grid_image = scale_image(resized_image2, scale_factor)
    polygon_image = scale_image(resized_image2, scale_factor)

    title_button_spacing = int(screen_height * 0.25)
    button_spacing_horizontal = int(30 * scale_factor)

    play_button = Button(
        image=play_image,
        pos=(screen_width // 2 - play_image.get_width() // 2 - button_spacing_horizontal // 2,
             title_button_spacing + int(30 * scale_factor)),
        text_input="PLAY",
        font=font,
        base_color="White",
        hovering_color="#eae3ff",
    )
    quit_button = Button(
        image=play_image,
        pos=(screen_width // 2 + play_image.get_width() // 2 + button_spacing_horizontal // 2,
             title_button_spacing + int(30 * scale_factor)),
        text_input="QUIT",
        font=font,
        base_color="White",
        hovering_color="#eae3ff",
    )

    settings_button = Button(
        image=grid_image,
        pos=(screen_width // 2, title_button_spacing + int(120 * scale_factor)),
        text_input=f"Game Settings",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )

    music_button = Button(
        image=music_image,
        pos=(screen_width // 2, title_button_spacing + int(310 * scale_factor)),
        text_input=f"Music Volume: {music_volume}%",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    theme_button = Button(
        image=polygon_image,
        pos=(screen_width // 2, title_button_spacing + int(215 * scale_factor)),
        text_input=f"Color Theme: {theme_options[theme_id]}",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    return [music_button, play_button, quit_button, theme_button, settings_button]


def main_menu():
    global SCREEN, polygon_index, grid_size, opponent, music_volume, theme_id
    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
    gameManager = game_manager.GameManager()
    gameManager.__setattr__("grid_size", grid_size)
    gameManager.__setattr__("selected_mode", polygon_options[polygon_index])
    gameManager.__setattr__("opponent", opponent)
    gameManager.__setattr__("theme_id", theme_id)

    while True:
        SCREEN.blit(pygame.transform.scale(BG, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw title
        draw_text(
            SCREEN,
            "MAIN MENU",
            (SCREEN.get_width() // 2, int(75 * (SCREEN.get_height() / 720))),
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
                buttons = create_buttons(event.w, event.h)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].checkForInput(MENU_MOUSE_POS):  # Music button
                    button_sound.play()
                    music_volume = (music_volume + 10) % 110  # Increment volume or reset
                    pygame.mixer.music.set_volume(music_volume / 100)  # Update music volume
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[1].checkForInput(MENU_MOUSE_POS):  # Play button
                    button_sound.play()
                    gameManager.__setattr__("grid_size", grid_size)
                    gameManager.__setattr__("selected_mode", polygon_options[polygon_index])
                    gameManager.__setattr__("opponent", opponent)
                    gameManager.__setattr__("theme_id", theme_id)
                    gameManager.run()
                if buttons[2].checkForInput(MENU_MOUSE_POS):  # Quit button
                    button_sound.play()
                    pygame.quit()
                    sys.exit()
                if buttons[3].checkForInput(MENU_MOUSE_POS):  # Theme button
                    button_sound.play()
                    theme_id = (theme_id + 1) % len(theme_options)  # Next theme option
                    buttons = create_buttons(SCREEN.get_width(), SCREEN.get_height())
                if buttons[4].checkForInput(MENU_MOUSE_POS):  # Settings button
                    button_sound.play()
                    from settings import settings_menu
                    settings_menu()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def set_options(size, index, opp):
    global grid_size, polygon_index, opponent
    grid_size = size
    polygon_index = index
    opponent = opp

def main():
    main_menu()

if __name__ == "__main__":
    main()
