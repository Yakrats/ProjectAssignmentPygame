# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()

    # Create the display surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set game and title
    pygame.display.set_caption("Asteroids")

    # Initialize the clock
    clock = pygame.time.Clock()

    # Initialize delta time (in seconds)
    dt = 0.0

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            # Checksum to make sure program is no longer running when quit
            if event.type == pygame.QUIT:
                running = False

        # Calculate delta time and limiting FPS to 60 seconds
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        
        # Game logic goes here (e.g., update positions, handle collisions, etc.)

        # Clear the screen with a solid black color
        screen.fill("black")

        # Other drawing and rendering code goes here

        # Refresh the screen
        pygame.display.flip()

    # Clean when done
    pygame.quit()

if __name__ == "__main__":
    main()