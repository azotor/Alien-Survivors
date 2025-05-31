from App.Config import Config
from App.Events import Events
from App.Controls import Keys, Mouse
from App.State import State
from App.Entity import Entity, EnitiesTypes
from App.Cooldown import Cooldown
from App.SwitchSceen import SwitchSceen
from App.Map import Map
from App.StatesManager import StatesManager
from App.Game import Game
from App.Icons import Icons
from App.Crosshair import Crosshair

icons = Icons()
keys = Keys()
mouse = Mouse()
states_manager = StatesManager()
events = Events()

alien_type = None