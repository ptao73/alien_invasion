import pygame
import os

def fix_transparency(input_path, output_path):
    pygame.init()
    # Need a display mode to use convert_alpha()
    pygame.display.set_mode((1, 1), pygame.HIDDEN)
    
    # Load the image
    surface = pygame.image.load(input_path)
    # Ensure it has an alpha channel
    surface = surface.convert_alpha()
    
    # Get direct access to pixels
    width, height = surface.get_size()
    for x in range(width):
        for y in range(height):
            r, g, b, a = surface.get_at((x, y))
            # If the pixel is fuchsia (or very close to it)
            if r > 200 and g < 50 and b > 200:
                surface.set_at((x, y), (0, 0, 0, 0))
    
    # Save the result
    pygame.image.save(surface, output_path)
    print(f"Transparency fixed! Saved to {output_path}")

if __name__ == "__main__":
    input_file = "/Users/ragepatti/.gemini/antigravity/brain/63830d14-82c2-4c5d-a595-fd4030fde861/flame_red_ship_v3_fuchsia_bg_1775959910198.png"
    output_file = "/Users/ragepatti/Documents/AI_Workspace/alien/images/ship.png"
    fix_transparency(input_file, output_file)
