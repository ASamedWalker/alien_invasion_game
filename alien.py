import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent a single alien in the fleet."""
  
  def __init__(self, ai_game):
    """Initialize the alien and set its starting position."""
    super().__init__()
    self.screen = ai_game.screen
    
    # Load the alien image and set it's rect attribute.
    self.image1 = pygame.image.load('./alien_invasion_game/images/alien.bmp')
    self.image = pygame.transform.smoothscale(self.image1, (40, 40))
    self.rect = self.image.get_rect()
    
    
    # Start each new alien near the top left of the screen.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    
    # Store the alien's exact horizontal position.
    self.x = float(self.rect.x)