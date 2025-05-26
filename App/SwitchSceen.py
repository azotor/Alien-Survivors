import pygame
import App

class SwitchSceen:
    def __init__( self ):
        self.speed = 100
        self.type = 1
        self.progress = 0
        self.start = False
        self.currentFrame = 0
        self.frameTime = 0
        self.frameMaxTime = 100
        self.animation = []
        self.pos = pygame.Vector2( 0, 0 )

    def startIn( self, speed = 100 ):
        self.start = True
        self.speed = speed
        self.type = 1
        self.progress = 0
        self.animation = [
            pygame.image.load( f'Assets/Aliens/{ App.alien_type }/alien{ App.alien_type }_walk1.png' ),
            pygame.image.load( f'Assets/Aliens/{ App.alien_type }/alien{ App.alien_type }_walk2.png' )
        ]
        self.pos = pygame.Vector2( ( App.Config.SCREEN_WIDTH - self.animation[ 0 ].get_width() ) / -2, ( App.Config.SCREEN_HEIGHT - self.animation[ 0 ].get_height() ) / 2 )
    
    def startOut( self, speed = 100 ):
        self.start = True
        self.speed = speed
        self.type = -1
        self.progress = 100
        self.animation = [
            pygame.image.load( f'Assets/Aliens/{ App.alien_type }/alien{ App.alien_type }_walk1.png' ),
            pygame.image.load( f'Assets/Aliens/{ App.alien_type }/alien{ App.alien_type }_walk2.png' )
        ]
        self.pos = pygame.Vector2( ( App.Config.SCREEN_WIDTH - self.animation[ 0 ].get_width() ) / 2, ( App.Config.SCREEN_HEIGHT - self.animation[ 0 ].get_height() ) / 2 )
    
    def isComplete( self ):
        return ( self.type == 1 and self.progress == 100 ) or ( self.type == -1 and self.progress == 0 )
    
    def isStart( self ):
        return self.start

    def update( self ):
        self.frameTime += 1000 / App.Config.FPS
        if self.frameTime > self.frameMaxTime:
            self.frameTime -= self.frameMaxTime
            self.currentFrame = 1 if self.currentFrame == 0 else 0
        
        self.pos += ( App.Config.SCREEN_WIDTH * App.Config.FPS / 1000, 0 )

        if self.type == 1 and self.progress < 100:
            self.progress += self.speed * App.Config.FPS / 1000
            if self.progress > 100:
                self.progress = 100
                self.start = False
        elif self.type == -1 and self.progress > 0:
            self.progress -= self.speed * App.Config.FPS / 1000
            if self.progress < 0:
                self.progress = 0
                self.start = False

    def render( self ):
        win = pygame.display.get_surface()
        width = App.Config.SCREEN_WIDTH * self.progress / 100
        if self.type == 1:
            pygame.draw.rect( win, '#222222', ( 0, 0, width, App.Config.SCREEN_HEIGHT ) )
        elif self.type == -1:
            pygame.draw.rect( win, '#222222', ( App.Config.SCREEN_WIDTH - width, 0, width, App.Config.SCREEN_HEIGHT ) )
        if len( self.animation ):
            win.blit( self.animation[ self.currentFrame ], self.pos )
