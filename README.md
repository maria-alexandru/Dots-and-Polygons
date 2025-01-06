# Dots and Polygons
- Name: Alexandru Maria-Mihaela, Badea Andreea-Bianca, Ciupitu Alexandra-Isabela,
Ion Cristina-Gabriela
- Group: 321CC

![image](https://github.com/user-attachments/assets/9d0d6fbe-1a5d-4388-99b4-17a4ecc1ff71)


# Description
- This project is a game developed using Python, based on the Pygame library, designed
to provide a relaxing and engaging experience for users of all ages. It features a
graphical user interface designed to provide an intuitive and visually appealing experience.
- The game is centered around a geometric challenge on a customizable grid and players take
turns drawing lines between dots to form squares, triangles or a mix of both, depending on
their settings. Each completed shape awards points and players retain their turn if they
successfully form a shape. The game ends when the grid is full and the player with the most
points wins.


# Technologies used
- Python: Programming language used to develop the game
- Pygame: Library used for creating the graphical user interface (GUI) and handling game interactions
- Git: Version control system for tracking changes and collaborating


# How to Run / Use:
## Install dependencies
``` pip install pygame ```

## Run the Game:
``` make ```

## How to play
1. **Start screen:**
- If you select the 'Play' option a new game will start and if you press the 'Quit'
option the game will immediately close
- If you enter the settings submenu, you will be able to choose the grid size from
(5x5) to (10x10), select the desired polygon type (square, triangle or mix) and the
opponent (another player or the computer)

![image](https://github.com/user-attachments/assets/59d33c10-f0e0-4466-b95c-ea6967591670)

- By clicking the 'Color Theme' button you can modify the appearance of the
game by choosing the desired theme.

2. **Gameplay**
- In Dots and Polygons, players take turns drawing lines between adjacent dots on a
grid, with the goal of completing polygons
- Players alternate turns to draw a line between two adjacent dots. The line can either
be horizontal, vertical or diagonal depending on the chosen game mode

![image](https://github.com/user-attachments/assets/48d2935b-4183-4e4b-b3e4-2bdb10595207)

- The goal is to complete the sides of the polygon
- When a player completes a polygon by drawing the final side, the shape is filled with
the player's color and they get another turn
- The game ends when all the polygons are completed and the player with the most boxes wins the game

![image](https://github.com/user-attachments/assets/5861c7a1-b1cd-4d56-8631-3e346537a5e1)

![image](https://github.com/user-attachments/assets/14ff3458-5583-4885-ba38-2c709adb25fe)

# Team Contributions:
- Alexandru Maria-Mihaela:
   - Worked on the game board layout 
   - Developed the function for resizing the window and ensuring the game board is redrawn properly
  when the window size changes
   - Implemented the logic for managing user input, ensuring that clicks on the board are handled
  correctly
- Badea Andreea-Bianca:
   - Designed the graphical user interface for menus and buttons, ensuring that they were user-friendly and intuitive
   - Added visual feedback when users interact with buttons (color changes when mouse is over)
   - Connecting the menus and options and created the final screen
- Ciupitu Alexandra-Isabela:
   - Implemented the box completion check
   - Developed the logic for computer moves, allowing the game to be played against the computer
   - Implemented the function to check if all polygons have been claimed
- Ion Cristina-Gabriela:
   - Implemented the turn-based system
   - Update the score and visually show the filled polygons
   - Added background music and sound effects to enhance the user experience, integrating Pygame's
  audio handling functions

# Challenges Encountered
- Resizing the game window, adjusting the grid size and gameplay elements to the size of the window
   - The biggest difficulty was that when the window was resized, the positions of the dots, the lines,
and the boxes didn’t automatically adjust. This caused the game elements to either overlap or get misaligned,
resulting in a grid where lines and boxes were not positioned correctly in relation to each other
    - To solve this, we used a scalable design where the grid’s dimensions and the positions of the lines
were dynamically calculated based on the new window size. Instead of using fixed values for the positioning
of the dots and lines, we used proportional calculations that adjusted based on the window’s width and height,
ensuring that everything stayed aligned


# Screenshots
## Color Themes
![image](https://github.com/user-attachments/assets/c7e4e29a-d1aa-4ba9-89c3-2c3c8d359126)
![image](https://github.com/user-attachments/assets/cfe53f79-77a3-4716-839a-6e61844efa0b)
![image](https://github.com/user-attachments/assets/d3716e0c-4bb5-4251-b9ab-5334481b4093)

## Game Over
![image](https://github.com/user-attachments/assets/4fa863fc-2496-44cf-8d41-e1bf16ad8db4)

![image](https://github.com/user-attachments/assets/bd09f88a-73b6-49d0-91cb-e9939e7e38ce)

