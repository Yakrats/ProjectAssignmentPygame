# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # Initialize Pygame
    pygame.init()

    # Create the display surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set game and title
    pygame.display.set_caption("Asteroids")

    # Player Object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialize the clock
    clock = pygame.time.Clock()

    # Initialize delta time (in seconds)
    dt = 0.0

    # Two groups intialized before loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add player to groups
    Player.containers = (updatable, drawable)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            # Checksum to make sure program is no longer running when quit
            if event.type == pygame.QUIT:
                running = False

        # Update player position
        for obj in updatable:
            obj.update(dt)

        # Calculate delta time and limiting FPS to 60 seconds
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        
        # Game logic goes here (e.g., update positions, handle collisions, etc.)

        # Clear the screen with a solid black color
        screen.fill("black")

        # Player Drawn
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()

    # Clean when done
    pygame.quit()

if __name__ == "__main__":
    main()