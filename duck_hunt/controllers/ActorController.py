from controllers.DogController import DogController
from models.Dog import Dog
import UIMainWindow


class ActorsController:

    def __init__(self,view, actor):
        self.view = view
        self.actor = actor
        
    @staticmethod
    def execute_move(self,actor):

        if isinstance(self.actor,Dog):
            if actor.State == 'Sniff':
                DogController.sniff(UIMainWindow.dogActor)
                self.actor.State = 'Jump'
            if actor.State == 'Jump':   
                DogController.jump(UIMainWindow.dogActor)