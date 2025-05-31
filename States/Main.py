import pygame
import App

class Main( App.State ):
    def __init__( self ):
        super().__init__()
        self.background = pygame.image.load( 'Assets/Backgrounds/grass.png' )
        self.cooldown = App.Cooldown()

        screen_w = App.Config.SCREEN_WIDTH
        screen_h = App.Config.SCREEN_HEIGHT
        bg_w = self.background.get_width()
        bg_h = self.background.get_height()
        screen_max = max( screen_w, screen_h )
        bg_min = min( bg_w, bg_h )
        scale = screen_max / bg_min

        self.background = pygame.transform.scale( self.background, ( bg_w * scale, bg_h * scale ) )
        self.scroll = 0
        self.font = pygame.font.SysFont( 'Tahoma', 36, True )

        self.aliens = [ 'Beige', 'Blue', 'Green', 'Pink', 'Yellow' ]
        self.currentAlien = 0

        self.biggest_alien = 0
        self.aliens_image = []
        for alien in self.aliens:
            self.aliens_image.append( [
                pygame.image.load( f'Assets/Aliens/{ alien }/alien{ alien }_stand.png' ),
                pygame.image.load( f'Assets/Aliens/{ alien }/alien{ alien }_front.png' )
            ] )
            if self.aliens_image[ len( self.aliens_image ) - 1 ][ 0 ].get_height() > self.biggest_alien:
                self.biggest_alien = self.aliens_image[ len( self.aliens_image ) - 1 ][ 0 ].get_height()
        
        self.switch = pygame.mixer.Sound( 'Assets/Sounds/switch20.ogg' )

        self.switch_screen = App.SwitchSceen()
        
    def start( self ):

        pygame.mixer.music.load( 'Assets/Musics/Cheerful Annoyance.ogg' )
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume( .5 )
    
    def update( self ):

        if self.switch_screen.isStart():
            self.switch_screen.update()
            if self.switch_screen.isComplete():
                self.change( 'PLAY' )
        else:
            self.scroll -= 1
            self.scroll %= self.background.get_width()

            self.cooldown.update()

            if self.cooldown.timer == 0:
                if App.keys.RIGHT:
                    self.switch.play()
                    self.cooldown.start( 200 )
                    self.currentAlien += 1
                    if self.currentAlien >= len( self.aliens_image ):
                        self.currentAlien = 0
                elif App.keys.LEFT:
                    self.switch.play()
                    self.cooldown.start( 200 )
                    self.currentAlien -= 1
                    if self.currentAlien < 0:
                        self.currentAlien = len( self.aliens_image ) - 1
                elif App.keys.CONFIRM:
                    pygame.mixer.music.stop()
                    App.alien_type = self.aliens[ self.currentAlien ]
                    self.switch_screen.startIn()
                elif App.keys.CANCEL:
                    App.events.iterate = False
    
    def render( self ):
        win = pygame.display.get_surface()
        win.blit( self.background, ( self.scroll, 0 ) )
        win.blit( self.background, ( self.scroll - self.background.get_width(), 0 ) )
        text = self.font.render( 'Choose Your Alien', True, 'white' )
        shadow = self.font.render( 'Choose Your Alien', True, 'black' )
        text_rect = text.get_rect()
        text_rect.center = ( App.Config.SCREEN_WIDTH / 2 + 2, App.Config.SCREEN_HEIGHT / 2 - 198 )
        win.blit( shadow, text_rect )
        text_rect.center = ( App.Config.SCREEN_WIDTH / 2, App.Config.SCREEN_HEIGHT / 2 - 200 )
        win.blit( text, text_rect )

        x = App.Config.SCREEN_WIDTH - ( self.aliens_image[ 0 ][ 0 ].get_width() + 20 ) * len( self.aliens_image ) - 10
        y = App.Config.SCREEN_HEIGHT / 2 - 90
        for i in range( len( self.aliens_image ) ):
            alien = self.aliens_image[ i ][ 1 if self.currentAlien == i else 0 ]
            dy = y + self.biggest_alien - alien.get_height()
            if self.currentAlien == i:
                highlight = pygame.Surface( ( alien.get_width() + 20, alien.get_height() + 60 ), pygame.SRCALPHA )
                pygame.draw.rect( highlight, '#00000088', ( 0, 0, highlight.get_width(), highlight.get_height() ), 0, 20 )
                win.blit( highlight, ( x - 10, dy - 10 ) )
            win.blit( alien, ( x, dy ) )
            text = self.font.render( self.aliens[ i ], True, self.aliens[ i ] )
            text_rect = text.get_rect()
            text_rect.center = ( x + alien.get_width() / 2, y + self.biggest_alien + 20 )
            win.blit( text, text_rect )
            x += alien.get_width() + 20

        text = self.font.render( 'Press ENTER to Survive', True, 'white' )
        shadow = self.font.render( 'Press ENTER to Survive', True, 'black' )
        text_rect = text.get_rect()
        text_rect.center = ( App.Config.SCREEN_WIDTH / 2 + 2, App.Config.SCREEN_HEIGHT - 98 )
        win.blit( shadow, text_rect )
        text_rect.center = ( App.Config.SCREEN_WIDTH / 2, App.Config.SCREEN_HEIGHT - 100 )
        win.blit( text, text_rect )

        self.switch_screen.render()
        