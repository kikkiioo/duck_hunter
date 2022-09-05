import time
import random as rand

from controllers.DogController import DogController
from controllers.DuckController import DuckController
from models.Dog import Dog
from models.Duck import Duck
from models.EnumDuckState import EnumDuckState
from models.Game import Game
from models.EnumDogState import EnumDogState


class GameController:


    def updateScore(game, score):
        game.score += score


    def updateDucks(game):
        flying_direction = rand.randint(0,1)
        duckActor = Duck(xPos=150, yPos=270, actorType = 'Duck', flyingSpeed=4.5, endXpos=550, endYpos=0,flyingDirection="up",
                         duckType="black", score=500, frame=0)
        duckActor2 = Duck(xPos=150, yPos=270,actorType = 'Duck', flyingSpeed=4.5, endXpos=550, endYpos=0,flyingDirection = "up",
                         duckType="black", score=500, frame=0, state = "RightFly")

        if flying_direction == 0:

            duckActor.state = "LeftFly"
            duckActor.xPos = rand.randint(0, 500)


        if flying_direction == 1:

            duckActor.state = "RightFly"
            duckActor.xPos = rand.randint(0, 500)

        duckCount = 0
        for actor in game.actors:
            if isinstance(actor, Duck):
                duckCount+=1

        if duckCount == 1:
            game.actors.append(duckActor)
        if duckCount == 0:
            game.actors.append(duckActor)
            game.actors.append(duckActor2)




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

    def updateActors( game, dt):

        for actor in game.actors:
            if isinstance(actor, Dog):
                if actor.state == EnumDogState.SNIFF:
                    game.animation_duration += dt
                    actor.frame += 15 * dt # slowing down animation
                    if actor.frame >= 3:
                        actor.frame = 0
                    if game.animation_duration > 3.0:
                        game.animation_duration = 0
                        actor.state = EnumDogState.SNIFF1

                if actor.state == EnumDogState.SNIFF1:

                    game.animation_duration += dt

                    actor.frame += 15 * dt # slowing down animation
                    if actor.frame >= 2:
                        actor.frame = 0
                    if game.animation_duration > 2.0:
                        game.animation_duration = 0
                        actor.state = EnumDogState.LOOK

                if actor.state == EnumDogState.LOOK:
                    game.animation_duration += dt
                    actor.frame = 0

                    if game.animation_duration > 1.5:
                        game.animation_duration = 0
                        actor.state = EnumDogState.JUMP_UP

                if actor.state == EnumDogState.JUMP_UP:
                    game.animation_duration += dt
                    actor.frame = 0
                    if game.animation_duration > 2.0:
                        game.animation_duration = 0
                        actor.state = EnumDogState.JUMP_DOWN

                if actor.state == EnumDogState.JUMP_DOWN:
                    game.animation_duration += dt
                    actor.frame = 0
                    if game.animation_duration > 1.0:

                        actor.state = EnumDogState.NOTHING
                        for actor in game.actors:
                            if isinstance(actor,Duck):
                                actor.state = EnumDuckState.RIGHTFLY
                                actor.xPos = rand.randint(0, 500)
                                game.animation_duration = 0

                if actor.state == EnumDogState.CATCHUP:
                    game.animation_duration += dt
                    actor.frame = 0

                    if game.animation_duration > 0.5:
                        game.animation_duration = 0
                        actor.state = EnumDogState.CATCHDOWN

                if actor.state == EnumDogState.CATCHDOWN:
                    game.animation_duration += dt
                    actor.frame = 0

                    if game.animation_duration > 0.5:
                        game.animation_start_time = time.time()
                        actor.state = EnumDogState.NOTHING
                        GameController.updateDucks(game)


            if isinstance(actor, Duck):

                if actor.state == EnumDuckState.RIGHTFLY:
                    if actor.frame > 2:
                        actor.frame = 0
                    actor.frame += 7 * dt
                    if actor.xPos > 550 or actor.yPos < 0:
                        actor.flyingDirection = "down"
                        actor.state = EnumDuckState.LEFTFLY
                    if actor.xPos < 0 or actor.yPos > 270:
                        actor.flyingDirection = "up"
                        actor.state = EnumDuckState.LEFTFLY

                if actor.state == EnumDuckState.LEFTFLY:
                    if actor.frame > 2:
                        actor.frame = 0

                    actor.frame += 7 * dt
                    if actor.xPos < 0 or actor.yPos > 270:
                        actor.flyingDirection = "up"
                        actor.state = EnumDuckState.RIGHTFLY

                    if  actor.yPos < -1:
                        actor.flyingDirection = "down"
                        actor.state = EnumDuckState.RIGHTFLY

                if actor.state == EnumDuckState.DIE:
                    game.animation_duration += dt
                    actor.frame = 0

                    if game.animation_duration > 2.0:
                        game.animation_duration = 0

                        actor.state = EnumDuckState.FALL

                if actor.state == EnumDuckState.FALL:

                    actor.frame += 15 * dt
                    if actor.frame>=2:
                        actor.frame=0

                    if actor.yPos > 280:
                        actor.state = EnumDuckState.NOTHING
                        duckActor = actor
                        duckActor.state = EnumDuckState.RIGHTFLY
                        duckActor.xPos = rand.randint(0, 500)
                        game.actors.remove(duckActor)
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

    def generateActors(game):

        dogActor = Dog(xPos=10, yPos=320, actorType = 'Dog',state=EnumDogState.SNIFF, frame = 0 )
        duckActor = Duck(xPos=150, yPos=270, actorType = 'Duck',flyingSpeed=4.5, flyingDirection="up", endXpos=550, endYpos=0,duckType = "black", score = 500, frame = 0)
        duckActor2 = Duck(xPos=200, yPos=270, actorType = 'Duck',flyingSpeed=4.5, flyingDirection="up", endXpos=550, endYpos=0,duckType = "black", score = 500, frame = 0 )

        game.actors.append(dogActor)
        game.actors.append(duckActor)
        game.actors.append(duckActor2)

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
