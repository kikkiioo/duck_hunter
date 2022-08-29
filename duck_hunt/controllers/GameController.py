import time
from random import random

from controllers.DogController import DogController
from controllers.DuckController import DuckController
from models.Dog import Dog
from models.Duck import Duck
from models.EnumDuckState import EnumDuckState
from models.Game import Game
from models.EnumDogState import EnumDogState


class GameController:

    def __init__(self, view):
        self.view = view

    def startGame(self):
        self.view.start_main_loop(self.view)

    def updateScore(game, score):
        game.score += score


    # def updateSprites(game):

    def updateControllers(game,dt):

        for actor in game.actors:
            if actor.state == EnumDogState.SNIFF:
                DogController.sniff(actor, dt)
            if actor.state == EnumDogState.JUMP_UP:
                DogController.jumpUp(actor, dt)
            if actor.state == EnumDogState.JUMP_DOWN:
                DogController.jumpDown(actor, dt)
            if actor.state == EnumDuckState.RIGHTFLY:
                DuckController.flyRight(actor, dt)
            if actor.state == EnumDuckState.LEFTFLY:
                DuckController.flyLeft(actor, dt)
            if actor.state == EnumDuckState.FALL:
                DuckController.fall(actor, dt)
            if actor.state == EnumDogState.CATCHUP:
                DogController.catchUp(actor, dt)
            if actor.state == EnumDogState.CATCHDOWN:
                DogController.catchDown(actor, dt)

    def updateRender( game, dt):

        for actor in game.actors:
            if isinstance(actor, Dog):
                if actor.state == EnumDogState.SNIFF:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.frame += 15 * dt # slowing down animation
                    if actor.frame >= 3:
                        actor.frame = 0
                    if game.animation_duration > 3.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.SNIFF1

                if actor.state == EnumDogState.SNIFF1:

                    game.animation_duration = time.time() - game.animation_start_time

                    actor.frame += 15 * dt # slowing down animation
                    if actor.frame >= 2:
                        actor.frame = 0
                    if game.animation_duration > 2.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.LOOK

                if actor.state == EnumDogState.LOOK:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.frame = 0

                    if game.animation_duration > 1.5:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.JUMP_UP

                if actor.state == EnumDogState.JUMP_UP:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.frame = 0
                    if game.animation_duration > 2.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.JUMP_DOWN

                if actor.state == EnumDogState.JUMP_DOWN:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.frame = 0
                    if game.animation_duration > 1.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.NOTHING
                        for actor in game.actors:
                            if isinstance(actor,Duck):
                                actor.state = EnumDuckState.RIGHTFLY

                if actor.state == EnumDogState.CATCHUP:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.yPos = 270
                    actor.frame = 0

                    if game.animation_duration > 2.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.CATCHDOWN

                if actor.state == EnumDogState.CATCHDOWN:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.frame = 0

                    if game.animation_duration > 2.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.NOTHING


            if isinstance(actor, Duck):

                if actor.state == EnumDuckState.RIGHTFLY:
                    if actor.frame > 2:
                        actor.frame = 0
                    actor.frame += 7 * dt
                    if actor.xPos > 550 or actor.yPos < 0:
                        actor.flyingDirection = "left"
                        actor.state = EnumDuckState.LEFTFLY

                if actor.state == EnumDuckState.LEFTFLY:
                    if actor.frame > 2:
                        actor.frame = 0

                    actor.frame += 7 * dt
                    if actor.xPos < 0 or actor.yPos > 270:
                        actor.flyingDirection = "left"
                        actor.state = EnumDuckState.RIGHTFLY

                if actor.state == EnumDuckState.DIE:
                    game.animation_duration = time.time() - game.animation_start_time
                    actor.frame = 0

                    if game.animation_duration > 2.0:
                        game.animation_start_time = time.time()
                        actor.state = EnumDuckState.FALL

                if actor.state == EnumDuckState.FALL:


                    actor.frame += 15 * dt
                    if actor.frame>=2:
                        actor.frame=0

                    if actor.yPos > 280:
                        actor.state = EnumDuckState.NOTHING
                        duckActor = actor
                        duckActor.state = EnumDuckState.RIGHTFLY
                        for actor in game.actors:
                            if isinstance(actor, Dog):
                                actor.xPos = duckActor.xPos
                                actor.state = EnumDogState.CATCHUP

    def checkCollision( game, mouseX, mouseY):

        for actor in game.actors:
            if isinstance(actor,Duck):
                duckX1 = actor.xPos - 25
                duckX2 = actor.xPos + 25
                duckY1 = actor.yPos + 25
                duckY2 = actor.yPos - 25

                if duckY1 >= mouseY >= duckY2 and mouseX >= duckX1 and mouseX <= duckX2:
                    actor.state = EnumDuckState.DIE
                    actor.frame = 0
                    GameController.updateScore(game, actor.score)

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
