import pygame
import sys

# Initialize Pygame
pygame.init()

# ----- Configuration Settings -----
# Game map dimensions (the real-world coordinates that the image represents)
GAME_MAP_WIDTH = 15000
GAME_MAP_HEIGHT = 15000

# ----- Image Loading -----
# Load the image from the current directory
image = pygame.image.load('image.png')
image_width = image.get_width()
image_height = image.get_height()

# Set up the display window to match the image dimensions
screen = pygame.display.set_mode((image_width, image_height))
pygame.display.set_caption("Click Coordinate Finder")

def get_scaled_coordinates(pixel_x, pixel_y):
    """
    Convert pixel coordinates to game map coordinates
    
    Args:
        pixel_x (int): X position in pixels on the image
        pixel_y (int): Y position in pixels on the image
        
    Returns:
        tuple: (x, y) scaled to the game map dimensions
    """
    scaled_x = (pixel_x / image_width) * GAME_MAP_WIDTH
    scaled_y = (pixel_y / image_height) * GAME_MAP_HEIGHT
    return scaled_x, scaled_y

# ----- Main Loop -----
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # Get pixel coordinates
                pixel_x, pixel_y = event.pos
                
                # Get scaled coordinates
                game_x, game_y = get_scaled_coordinates(pixel_x, pixel_y)
                
                # Display results in console
                print(f"Pixel coordinates: ({pixel_x}, {pixel_y})")
                print(f"Game map coordinates: ({int(game_x)}, {int(game_y)})")

    # Render the image to the screen
    screen.blit(image, (0, 0))
    pygame.display.flip()

# Clean up when exiting
pygame.quit()
sys.exit()