import pygame
import App

class Player( App.Entity ):
    def __init__( self, _pos ):
        super().__init__( _pos, App.EnitiesTypes.PLAYABLE, 50 )
        self.screen_pos = pygame.Vector2( App.Config.SCREEN_WIDTH / 2, App.Config.SCREEN_HEIGHT / 2 )
        self.name = App.alien_type
        self.animations = {
            'CLIMB' :  [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_climb1.png', .25 ), self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_climb2.png', .25 ) ],
            'DUCK' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_duck.png', .25 ) ],
            'FRONT' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_front.png', .25 ) ],
            'HIT' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_hit.png', .25 ) ],
            'JUMP' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_jump.png', .25 ) ],
            'STAND' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_stand.png', .25 ) ],
            'SWIM' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_swim1.png', .25 ), self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_swim2.png', .25 ) ],
            'WALK' : [ self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_walk1.png', .25 ), self.loadImage( f'Assets/Aliens/{ self.name }/alien{ self.name }_walk2.png', .25 ) ]
        }
        self.switchAnimation( 'STAND' )
    
    def update( self ):

        if App.keys.RIGHT:
            self.dir[ 0 ] = 1
            self.facing = 1
        elif App.keys.LEFT:
            self.dir[ 0 ] = -1
            self.facing = -1
        else:
            self.dir[ 0 ] = 0

        if App.keys.DOWN:
            self.dir[ 1 ] = 1
        elif App.keys.UP:
            self.dir[ 1 ] = -1
        else:
            self.dir[ 1 ] = 0
        
        match( self.currentAnimation ):
            case 'STAND' :
                if self.dir[ 0 ] != 0 or self.dir[ 1 ] != 0:
                    self.switchAnimation( 'WALK' )
            case 'WALK' :
                if self.dir[ 0 ] == 0 and self.dir[ 1 ] == 0:
                    self.switchAnimation( 'STAND' )

        super().update()
        
        frame = self.animations[ self.currentAnimation ][ self.currentFrame ]
        if self.pos[ 0 ] < frame.get_width() / 2:
            self.pos[ 0 ] = frame.get_width() / 2
        elif self.pos[ 0 ] > App.states_manager.currentState.map.width - frame.get_width() / 2:
            self.pos[ 0 ] = App.states_manager.currentState.map.width - frame.get_width() / 2

        if self.pos[ 1 ] < frame.get_height():
            self.pos[ 1 ] = frame.get_height()
        elif self.pos[ 1 ] > App.states_manager.currentState.map.height:
            self.pos[ 1 ] = App.states_manager.currentState.map.height

        self.screen_pos = App.states_manager.currentState.offset + self.pos

    def render( self ):
        win = pygame.display.get_surface()
        frame = self.animations[ self.currentAnimation ][ self.currentFrame ]
        if self.facing == -1:
            frame = pygame.transform.flip( frame, -1, 0 )
        pos = self.screen_pos - ( frame.get_width() / 2, frame.get_height() )
        win.blit( frame, pos )
        pygame.draw.line( win, "red", self.screen_pos - ( 10, 0 ),  self.screen_pos + ( 10, 0 ) )
        pygame.draw.line( win, "red", self.screen_pos - ( 0, 10 ),  self.screen_pos + ( 0, 10 ) )