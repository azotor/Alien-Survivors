import App

class State:
    def __init__( self ):
        pass

    def change( self, _name ):
        App.states_manager.change( _name )

    def start( self ):
        pass

    def stop( self ):
        pass

    def update( self ):
        pass

    def render( self ):
        pass