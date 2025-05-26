import pygame

class Icons_Loader:
    def __init__( self ):
        self.icons_image = pygame.image.load( 'Assets/Icons/Keyboard and Mouse.png' )
        self.size = 64

    def cut( self, _x, _y ):
        icon = pygame.Surface( ( self.size, self.size ), pygame.SRCALPHA )
        icon.blit( self.icons_image, ( 0, 0 ), ( _x * self.size, _y * self.size, self.size, self.size ) )
        return icon

loader = Icons_Loader()

class Icons:
    ARROW_UP = loader.cut( 3, 13 )
    ARROW_RIGHT = loader.cut( 1, 13 )
    ARROW_DOWN = loader.cut( 13, 14 )
    ARROW_LEFT = loader.cut( 15, 14 )