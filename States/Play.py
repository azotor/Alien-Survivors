import pygame
import App, Entities

class Play( App.State ):
    def __init__( self ):
        super().__init__()
        self.switch_screen = App.SwitchSceen()
        self.map = None
        self.offset = pygame.Vector2( 0, 0 )
        self.entities = []
        self.screen_center = pygame.Vector2( App.Config.SCREEN_WIDTH / 2, App.Config.SCREEN_HEIGHT / 2 )
        self.begin = False
    
    def start( self ):
        self.switch_screen.startOut()
        self.map = App.Map( ( 13, 10 ) )
        self.entities = []
        self.entities.append( Entities.Player( pygame.Vector2( self.map.width / 2, self.map.height / 2 ) ) )
        player = self.entities[ 0 ]
        self.offset = player.pos - self.screen_center
        self.crosshair = App.Crosshair()
        pygame.mouse.set_visible( False )

        pygame.mixer.music.load( 'Assets/Musics/Infinite Descent.ogg' )
        pygame.mixer.music.set_volume( .3 )
        pygame.mixer.music.play()
    
    def stop( self ):
        pygame.mouse.set_visible( True )
        pygame.mixer.music.stop()

    def update( self ):
        if self.switch_screen.isComplete():
            if not self.begin and ( App.keys.UP or App.keys.RIGHT or App.keys.DOWN or App.keys.LEFT ):
                self.begin = True

            for entity in self.entities:
                entity.update()
            self.map.update()
            
            player = self.entities[ 0 ]
            d = player.screen_pos.distance_to( self.screen_center )
            if d > 5:
                screen_scroll = pygame.Vector2( player.screen_pos - self.screen_center )
                self.offset -= screen_scroll.normalize() * d * App.Config.FPS / 1000
            
            self.crosshair.update()
        else:
            self.switch_screen.update()
    
    def render( self ):
        win = pygame.display.get_surface()
        win.fill( '#222222' )
        
        self.map.render()
        for entity in self.entities:
            entity.render()

        if not self.begin:
            x = self.screen_center[ 0 ] - App.icons.ARROW_UP.get_width() / 2
            y = self.screen_center[ 1 ] - App.icons.ARROW_UP.get_height() / 2
            win.blit( App.icons.ARROW_UP, ( x, y - 100 ) )
            win.blit( App.icons.ARROW_RIGHT, ( x + 100, y ) )
            win.blit( App.icons.ARROW_DOWN, ( x, y + 100 ) )
            win.blit( App.icons.ARROW_LEFT, ( x - 100, y ) )

        self.crosshair.render()

        if not self.switch_screen.isComplete():
            self.switch_screen.render()
        