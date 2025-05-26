import pygame
import App

class Preload( App.State ):
    def __init__( self ):
        super().__init__()
    
    def update( self ):
        self.change( 'MAIN' )
    
    def render( self ):
        win = pygame.display.get_surface()
        win.fill( '#222222' )