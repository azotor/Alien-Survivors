import pygame
import App

class Crosshair:
    def __init__( self ):
        self.pos = pygame.Vector2( 0, 0 )
        self.icon = [
            pygame.image.load( 'Assets/Icons/crosshair1.png' ),
            pygame.image.load( 'Assets/Icons/crosshair0.png' )
        ]
        self.state = 0  # 0 - brak kolizji z namierzonym przeciwnikiem, 1 - kolizja z namierzonym przeciwnikiem
        self.reset()
    
    def reset( self ):
        win = pygame.display.get_surface()
        self.pos = pygame.Vector2( win.get_width() / 2, win.get_height() / 2 )
    
    def update( self ):
        pass

    def render( self ):
        win = pygame.display.get_surface()
        icon = self.icon[ self.state ]
        win.blit( icon, ( App.mouse.X - icon.get_width() / 2, App.mouse.Y - icon.get_height() / 2 ) )