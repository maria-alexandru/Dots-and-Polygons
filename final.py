import pygame
import sys
from button import Button
import game_manager

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dots and Polygons")

# Background and fonts
BG = pygame.image.load("assets/fundal.jpg")
BASE_FONT_SIZE = 20

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

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
    #font = pygame.font.SysFont("Arial", font_size)
    font = get_font(font_size)

    original_image = pygame.image.load("assets/Play Rect.png")
    resized_image1 = pygame.transform.scale(original_image, (165, 75))
    resized_image2 = pygame.transform.scale(original_image, (360, 75))

    quit_image = scale_image(resized_image1, scale_factor)
    menu_image = scale_image(resized_image2, scale_factor)
   

    title_button_spacing = int(screen_height * 0.25)

    quit_button = Button(
        image=quit_image,
        pos=(screen_width // 2, title_button_spacing + int(150 * scale_factor)),
        text_input="QUIT",
        font=font,
        base_color="White",
        hovering_color="#eae3ff",
    )
    
    
    menu_button = Button(
        image=menu_image,
        pos=(screen_width // 2, title_button_spacing + int(280 * scale_factor)),
        text_input=f"BACK TO MENU",
        font=font,
        base_color="White",
        hovering_color="#d7fcd4",
    )
    return [quit_button, menu_button]


def main_menu():
    global SCREEN, polygon_index, grid_size, opponent, music_volume
    buttons = create_buttons(SCREEN_WIDTH, SCREEN_HEIGHT)

    while True:
        SCREEN.blit(pygame.transform.scale(BG, (SCREEN.get_width(), SCREEN.get_height())), (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw title
        draw_text(
            SCREEN,
            "GAME OVER",
            (SCREEN.get_width() // 2, int(200 * (SCREEN.get_height() / 720))),
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
                if buttons[0].checkForInput(MENU_MOUSE_POS):  # Quit button
                    pygame.quit()
                    sys.exit()
                if buttons[1].checkForInput(MENU_MOUSE_POS):  # Back to Menu button
                    pygame.quit()
                    sys.exit()
                            
        pygame.display.update()


main_menu()
