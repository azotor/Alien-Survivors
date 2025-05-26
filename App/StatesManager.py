import States

class StatesManager:

    currentState = None

    def __init__( self ):
        self.states = {
            'PRELOAD' : States.Preload(),
            'MAIN' : States.Main(),
            'PLAY' : States.Play()
        }
        self.currentState = self.states[ 'PRELOAD' ]
        self.currentState.start()

    def change( self, _name ):
        self.currentState.stop()
        self.currentState = self.states[ _name ]
        self.currentState.start()
    
    def update( self ):
        self.currentState.update()
    
    def render( self ):
        self.currentState.render()