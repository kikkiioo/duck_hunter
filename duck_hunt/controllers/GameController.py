import time
from controllers.DogController import DogController
from controllers.DuckController import DuckController
from models.Dog import Dog
from models.EnumDuckState import EnumDuckState
from models.Game import Game
from models.EnumDogState import EnumDogState


class GameController:

    def __init__(self, view):
        self.view = view

    def startGame(self):
        self.view.start_main_loop(self.view)

    def updateScore(self, game, score):
        game.score += score
        self.displayScore(self)

    # def updateSprites(game):

    def updateControllers(game,dt):
        dogActor = game.actors[1]
        duckActor = game.actors[2]

        if dogActor.state == EnumDogState.SNIFF:
            DogController.sniff(dogActor, dt)
        if dogActor.state == EnumDogState.JUMP_UP:
            DogController.jumpUp(dogActor, dt)
        if dogActor.state == EnumDogState.JUMP_DOWN:
            DogController.jumpDown(dogActor, dt)
        if duckActor.state == EnumDuckState.RIGHTFLY:
            DuckController.flyRight(duckActor, dt)
        if duckActor.state == EnumDuckState.LEFTFLY:
            DuckController.flyLeft(duckActor, dt)
        if duckActor.state == EnumDuckState.DIE:
            DuckController.die(duckActor, dt)
        if dogActor.state == EnumDogState.CATCHUP:
            DogController.catchUp(dogActor, dt)
        if dogActor.state == EnumDogState.CATCHDOWN:
            DogController.catchDown(dogActor, dt)

    def updateRender(self, game):

        dogActor = game.actors[1]
        duckActor = game.actors[2]

        if dogActor.state == EnumDogState.SNIFF:
            game.animation_duration = time.time() - game.animation_start_time

            if game.frame >= 3:
                game.frame = 0
            self.draw_Dog(self, dogActor, int(game.frame))
            game.frame += 0.2 # slowing down animation

            if game.animation_duration > 3.0:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.SNIFF1

        if dogActor.state == EnumDogState.SNIFF1:

            game.animation_duration = time.time() - game.animation_start_time
            if game.frame >= 2:
                game.frame = 0
            self.draw_Dog(self, dogActor, int(game.frame))
            game.frame += 0.2 # slowing down animation

            if game.animation_duration > 2.0:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.LOOK

        if dogActor.state == EnumDogState.LOOK:
            game.animation_duration = time.time() - game.animation_start_time
            game.frame = 0
            self.draw_Dog(self, dogActor, int( game.frame))
            if game.animation_duration > 1.5:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.JUMP_UP

        if dogActor.state == EnumDogState.JUMP_UP:
            game.animation_duration = time.time() - game.animation_start_time
            game.frame = 1
            self.draw_Dog(self, dogActor, int( game.frame))
            if game.animation_duration > 2.0:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.JUMP_DOWN

        if dogActor.state == EnumDogState.JUMP_DOWN:

            game.animation_duration = time.time() - game.animation_start_time
            game.frame = 2
            self.draw_Dog(self, dogActor, game.frame)
            if game.animation_duration > 1.0:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.NOTHING
                duckActor.state = EnumDuckState.RIGHTFLY

        if duckActor.state == EnumDuckState.RIGHTFLY:

            if game.frame > 2:
                game.frame = 0
            self.draw_Duck(self, duckActor, int(game.frame))
            game.frame += 0.2
            if duckActor.xPos > 550 or duckActor.yPos < 0:
                duckActor.flyingDirection = "left"
                duckActor.state = EnumDuckState.LEFTFLY

        if duckActor.state == EnumDuckState.LEFTFLY:

            if game.frame > 2:
                game.frame = 0
            self.draw_Duck(self, duckActor, int(game.frame))
            game.frame += 0.2
            if duckActor.xPos < 0 or duckActor.yPos > 270:
                duckActor.flyingDirection = "left"
                duckActor.state = EnumDuckState.RIGHTFLY

        if duckActor.state == EnumDuckState.DIE:

            if game.frame >= 3:
                game.frame = 1
            self.draw_Duck(self, duckActor, int(game.frame))
            game.frame += 0.2
            if duckActor.yPos > 280:
                duckActor.state = EnumDuckState.NOTHING
                dogActor.xPos = duckActor.xPos
                dogActor.state = EnumDogState.CATCHUP

        if dogActor.state == EnumDogState.CATCHUP:
            game.animation_duration = time.time() - game.animation_start_time
            dogActor.yPos = 270
            game.frame = 0
            self.draw_Dog(self, dogActor, int(game.frame))
            if game.animation_duration > 2.0:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.CATCHDOWN

        if dogActor.state == EnumDogState.CATCHDOWN:
            game.animation_duration = time.time() - game.animation_start_time
            game.frame = 0
            self.draw_Dog(self, dogActor, int(game.frame))
            if game.animation_duration > 2.0:
                game.animation_start_time = time.time()
                dogActor.state = EnumDogState.NOTHING
                duckActor.state = EnumDuckState.RIGHTFLY

    def checkCollision(self, game, mouseX, mouseY):

        duckActor = game.actors[2]
        duckX1 = duckActor.xPos - 25
        duckX2 = duckActor.xPos + 25
        duckY1 = duckActor.yPos + 25
        duckY2 = duckActor.yPos - 25

        if duckY1 >= mouseY >= duckY2 and mouseX >= duckX1 and mouseX <= duckX2:
            duckActor.state = EnumDuckState.DIE
            GameController.updateScore(self, game, duckActor.blackScore)

    @staticmethod
    def isGameOver(game):
        if game.isGameOver == True:
            result = True
            return result

    @staticmethod
    def isNextLevel(game):
        if game.isNextLevel == True:
            result = True
            return result
