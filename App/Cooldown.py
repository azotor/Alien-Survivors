import App

class Cooldown:
    def __init__( self ):
        self.timer = 0
    
    def start( self, time ):
        self.timer = time
    
    def update( self ):
        if self.timer > 0:
            self.timer -= 1000 / App.Config.FPS
            if self.timer < 0:
                self.timer = 0