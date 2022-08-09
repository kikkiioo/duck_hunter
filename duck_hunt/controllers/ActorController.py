
from controllers.DuckController import DuckController
from controllers.DogController import DogController
from models.Duck import Duck
from models.Dog import Dog





class ActorsController:

    def __init__(self, view, actor):
        self.view = view
        self.actor = actor

    @staticmethod
    def execute_move(actor):

        if isinstance(actor, Dog):
            if actor.state == 'Sniff':
                DogController.sniff(actor)
            if actor.state == 'JumpUp':
                DogController.jumpUp(actor)
            if actor.state == 'JumpDown':
                DogController.jumpDown(actor)
            if actor.state == 'CatchUp':
                DogController.catchUp(actor)
            if actor.state == 'CatchDown':
                DogController.catchDown(actor)

        if isinstance(actor, Duck):
            if actor.state == 'RightFly':
                DuckController.flyRight(actor)
            if actor.state == 'LeftFly':
                DuckController.flyLeft(actor)
            if actor.state == 'Die':
                DuckController.die(actor)