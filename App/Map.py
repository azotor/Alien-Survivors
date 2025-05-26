import pygame

import App

class Map:
    def __init__( self, size = ( 0, 0 ) ):
        self.pos = pygame.Vector2( 0, 0 )
        self.size = size
        self.tile = pygame.image.load( 'Assets/Tiles/grass.png' )
        self.width = self.tile.get_width() * self.size[ 0 ]
        self.height = self.tile.get_height() * self.size[ 1 ]
        self.screen_offset = App.states_manager.currentState.offset + self.pos
    
    def update( self ):
        self.screen_offset = App.states_manager.currentState.offset + self.pos

    def render( self ):
        win = pygame.display.get_surface()

        for y in range( self.size[ 1 ] ):
            for x in range( self.size[ 0 ] ):
                win.blit( self.tile, ( x * self.tile.get_width() + self.screen_offset[ 0 ], y * self.tile.get_height() + self.screen_offset[ 1 ] ) )