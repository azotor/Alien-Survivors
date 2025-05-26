import pygame

import App

class Game:
    def __init__( self ):
        pygame.display.set_mode( ( App.Config.SCREEN_WIDTH, App.Config.SCREEN_HEIGHT ) )
        pygame.display.set_caption( App.Config.TITLE )
        self.clock = pygame.time.Clock()
        self.loop()

    def loop( self ):
        while App.events.iterate:
            App.events.update()
            App.states_manager.update()
            App.states_manager.render()
            pygame.display.update()
            self.clock.tick( App.Config.FPS )