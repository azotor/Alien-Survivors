import pygame

import App

class Events:
    def __init__( self ):
        self.iterate = True
    
    def update( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.iterate = False
        
        keys = pygame.key.get_pressed()
        App.keys.UP = keys[ pygame.K_UP ] or keys[ pygame.K_w ]
        App.keys.RIGHT = keys[ pygame.K_RIGHT ] or keys[ pygame.K_d ]
        App.keys.DOWN = keys[ pygame.K_DOWN ] or keys[ pygame.K_s ]
        App.keys.LEFT = keys[ pygame.K_LEFT ] or keys[ pygame.K_a ]
        App.keys.CONFIRM = keys[ pygame.K_RETURN ]
        App.keys.CANCEL= keys[ pygame.K_ESCAPE ]

        
        mouse_pos = pygame.mouse.get_pos()
        App.mouse.X = mouse_pos[ 0 ]
        App.mouse.Y = mouse_pos[ 1 ]
        mouse_keys = pygame.mouse.get_pressed()
        App.mouse.LEFT = mouse_keys[ 0 ]
        App.mouse.RIGHT = mouse_keys[ 2 ]
        App.mouse.FOCUSE = pygame.mouse.get_focused()