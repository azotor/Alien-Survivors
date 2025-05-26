import pygame
import App

class Entity:
    def __init__( self, _pos, _type, _max_speed = 40 ):
        print( _pos )
        self.pos = pygame.Vector2( _pos )
        self.screen_pos = pygame.Vector2( 0, 0 )
        self.dir = pygame.Vector2( 0, 0 )
        self.speed = 40
        self.maxSpeed = _max_speed
        self.facing = 1
        self.type = _type

        self.animations = {}
        self.currentAnimation = None
        self.currentFrame = 0

        self.frameTime = 0
        self.maxFrameTime = 200
    
    def loadImage( self, _file, _scale = 1 ):
        img = pygame.image.load( _file )
        if _scale != 1:
            img = pygame.transform.scale( img, ( img.get_width() * _scale, img.get_height() * _scale ) )
        return img
    
    def switchAnimation( self, _name ):
        self.currentAnimation = _name
        self.currentFrame = 0
    
    def update( self ):
        if self.dir[ 0 ] != 0 or self.dir[ 1 ] != 0:
            self.dir.normalize()
        
        self.pos += self.dir * ( self.speed * App.Config.FPS / 1000 )
        
        self.frameTime += 1000 / App.Config.FPS
        if self.frameTime >= self.maxFrameTime:
            self.frameTime -= self.maxFrameTime
            self.currentFrame += 1
            if self.currentFrame >= len( self.animations[ self.currentAnimation ] ):
                self.currentFrame = 0

    def render( self ):
        win = pygame.display.get_surface()
        frame = self.animations[ self.currentAnimation ][ self.currentFrame ]
        if self.facing == -1:
            frame = pygame.transform.flip( frame, -1, 0 )
        win.blit( frame, self.pos )

class EnitiesTypes:
    PLAYABLE = 1