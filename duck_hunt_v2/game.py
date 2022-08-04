
from enum import Enum

from random import randint

from strenum import StrEnum
import enum
import string
import dataclasses
from time import time

from dacite import Dict
import pygame
import time
from sys import exit
from typing import List

from pydantic import Field
from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json
from sympy import false, true

#model


class EnumDogState(str, Enum):
    NOTHING = 'None'
    SNIFF = 'Sniff'
    SNIFF1 = 'Sniff1'
    LOOK = 'Look'
    JUMP_UP = 'JumpUp'
    JUMP_DOWN = 'JumpDown'
    CATCHUP = 'CatchUp'
    CATCHDOWN = 'CatchDown'
    GIGGLE = 'Giggle'


class EnumDuckState(str,Enum):
    NOTHING = 'None'
    RIGHTFLY = 'RightFly'
    LEFTFLY = 'LeftFly'
    DIE = 'Die'
    


class EnumPlayerState(str,Enum):
    NOTHING = 'None'


@dataclass_json
@dataclass
class Actor:
    xPos: int = 0
    yPos: int = 0

@dataclass_json
@dataclass
class Dog(Actor):
    state: EnumDogState = EnumDogState.NOTHING

@dataclass_json
@dataclass
class Duck(Actor):
    state: EnumDuckState = EnumDuckState.NOTHING
    flyingSpeed: float = 0
    flyingDirection: str = "left"
    endXpos: int = 0
    endYpos: int = 0

@dataclass_json
@dataclass
class BlackDuck(Duck):
    blackScore: int = 0

@dataclass_json
@dataclass
class BlueDuck(Duck):
    blueScore: int = 0

@dataclass_json
@dataclass
class RedDuck(Duck):
    redScore: int = 0

@dataclass_json
@dataclass
class Game:
    level : int = 0
    score: int = 0
    shotCount: int = 0
    actors: List[Actor] = dataclasses.field(default_factory= list)

@dataclass_json
@dataclass 
class Player(Actor):
    #state: EnumPlayerState.Nothing
    shotCount: int = 0
    hitCount: int = 0
    successShotCount: int = 0

#controller
class ActorsController:

    def __init__(self,view, actor):
        self.view = view
        self.actor = actor
        
    @staticmethod
    def execute_move(actor):

        if isinstance(actor,Dog):
            if actor.state == 'Sniff':
                DogController.sniff(UIMainWindow.dogActor)
            if actor.state == 'JumpUp':   
                DogController.jumpUp(UIMainWindow.dogActor)
            if actor.state == 'JumpDown':   
                DogController.jumpDown(UIMainWindow.dogActor)
            if actor.state == 'CatchUp':
                DogController.catchUp(UIMainWindow.dogActor)
            if actor.state == 'CatchDown':
                DogController.catchDown(UIMainWindow.dogActor)
        if isinstance(actor,Duck):
            if actor.state == 'RightFly':
                DuckController.flyRight(UIMainWindow.duckActor)
            if actor.state == 'LeftFly':
                DuckController.flyLeft(UIMainWindow.duckActor)
            if actor.state == 'Die':
                DuckController.die(UIMainWindow.duckActor)

class GameController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    
    def startGame(self):
        self.view.start_main_loop(UIMainWindow)

class DogController:

    @staticmethod
    def sniff(dogActor):
        dogActor.xPos += 10 

    def jumpUp(dogActor):
        dogActor.xPos+=15
        dogActor.yPos-=30
            
    def jumpDown(dogActor):
        dogActor.xPos+=15
        dogActor.yPos+=30

    def catchUp(dogActor):
        dogActor.yPos-=5

    def catchDown(dogActor):
        dogActor.yPos+=5

class DuckController:

    @staticmethod
    def flyRight(duckActor):
        # dx,dy = (duckActor.endXpos - duckActor.xPos, duckActor.endYpos - duckActor.yPos  )
        # stepx,stepy = (dx/25., dy/25. )
        # duckActor.xPos += stepx      
        # duckActor.yPos += stepy 
        duckActor.xPos += 2 * duckActor.flyingSpeed
        duckActor.yPos -= 2 * duckActor.flyingSpeed
    def flyLeft(duckActor):
        # dx,dy = (duckActor.endXpos - duckActor.xPos, duckActor.endYpos - duckActor.yPos  )
        # stepx,stepy = (dx/25., dy/25. )
        # duckActor.xPos += stepx      
        # duckActor.yPos += stepy 
        duckActor.xPos -= 2 * duckActor.flyingSpeed
        duckActor.yPos += 2 * duckActor.flyingSpeed

    def die(duckActor):
        duckActor.yPos +=15

#view 
class UIMainWindow:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Duck hunt')

        self.screen = pygame.display.set_mode((550,480))
        self.background_surf = pygame.image.load('graphics/background.png').convert_alpha()
        self.ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
        self.test_font = pygame.font.Font('font/Pixeltype.ttf',30)
        self.level_surf = self.test_font.render('01', True , 'white')
        self.level_rect = self.level_surf.get_rect(topleft = (95, 388))
        self.score_surf = self.test_font.render('01', True , 'white')
        self.score_rect = self.level_surf.get_rect(topleft = (95, 388))
        
        
        
       
        #Dog animations
        self.sniff1 = pygame.image.load('graphics/dog/sniff1.png').convert_alpha()
        self.sniff2 = pygame.image.load('graphics/dog/sniff2.png').convert_alpha()
        self.sniff3 = pygame.image.load('graphics/dog/sniff3.png').convert_alpha()
        self.sniff4 = pygame.image.load('graphics/dog/sniff4.png').convert_alpha()
        self.sniff5 = pygame.image.load('graphics/dog/sniff5.png').convert_alpha()
        self.sniff6 = pygame.image.load('graphics/dog/sniff6.png').convert_alpha()
        self.jump1 = pygame.image.load('graphics/dog/jump1.png').convert_alpha()
        self.jump2 = pygame.image.load('graphics/dog/jump2.png').convert_alpha()
        self.jump3 = pygame.image.load('graphics/dog/jump3.png').convert_alpha()
        self.catch = pygame.image.load('graphics/dog/catch.png').convert_alpha()
        self.dogDict = {"Sniff": [self.sniff1,self.sniff2,self.sniff3,self.sniff4],
                    "Sniff1": [self.sniff5,self.sniff6],
                    "Jump": [self.jump1,self.jump2,self.jump3],
                    "Catch":[self.catch]}
        
        self.dogActor = Dog(xPos = 10, yPos = 320, state = EnumDogState.SNIFF)
        self.duckActor = BlackDuck(xPos = 150, yPos= 270, flyingSpeed = 4.5 , flyingDirection = "right", endXpos = 550, endYpos = 0, blackScore = 500,state = EnumDuckState.RIGHTFLY )
        
        #Duck animations
        self.rightFlyBlack1 = pygame.image.load('graphics/duck/blackDuck/fly1.png').convert_alpha()
        self.rightFlyBlack2 = pygame.image.load('graphics/duck/blackDuck/fly2.png').convert_alpha()
        self.rightFlyBlack3 = pygame.image.load('graphics/duck/blackDuck/fly3.png').convert_alpha()
        self.leftFlyBlack1 = pygame.image.load('graphics/duck/blackDuck/fly4.png').convert_alpha()
        self.leftFlyBlack2 = pygame.image.load('graphics/duck/blackDuck/fly5.png').convert_alpha()
        self.leftFlyBlack3 = pygame.image.load('graphics/duck/blackDuck/fly6.png').convert_alpha() 

        self.blackDuckDie1 = pygame.image.load('graphics/duck/blackDuck/die1.png').convert_alpha()
        self.blackDuckDie2 = pygame.image.load('graphics/duck/blackDuck/die2.png').convert_alpha()
        self.blackDuckDie3 = pygame.image.load('graphics/duck/blackDuck/die3.png').convert_alpha()
    
        self.blackDuckDict = {"RightFly": [self.rightFlyBlack1,self.rightFlyBlack2,self.rightFlyBlack3],
        "Die":[self.blackDuckDie1,self.blackDuckDie2,self.blackDuckDie3],
        "LeftFly": [self.leftFlyBlack1,self.leftFlyBlack2,self.leftFlyBlack3]}

        
        self.player = Player(xPos=0,yPos=0,shotCount=3,hitCount=0,successShotCount=0)
        
         
    def start_main_loop(self):
        self.__init__(self)
        self.displayGraphics(self)

        #self.game = Game(1,0,3,None)
        intro_active = True
        game_active = True
        is_running = True
        generate_sprites = True
        frame = 0 

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if game_active:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if self.rightFlyBlack1.get_rect(center = (self.duckActor.xPos,self.duckActor.yPos)).collidepoint(event.pos) or self.rightFlyBlack2.get_rect(center = (self.duckActor.xPos,self.duckActor.yPos)).collidepoint(x,y) or self.rightFlyBlack3.get_rect(center = (self.duckActor.xPos,self.duckActor.yPos)).collidepoint(x,y):
                            self.duckActor.state = EnumDuckState.DIE
                            
            # GAME INTRO     
            if intro_active:
                self.dogActor.xPos = 10
                self.dogActor.yPos = 320
                self.dogActor.state = EnumDogState.SNIFF

                for i in range(4):
                    for j in range(4):
                        self.draw_Dog(self,self.dogActor,j)
                        pygame.display.update()
                        pygame.time.wait(100)
                        self.displayGraphics(self)
                        pygame.display.update()
                        ActorsController.execute_move(self.dogActor)

                self.dogActor.state = EnumDogState.SNIFF1

                for l in range(4):
                    for k in range(2):
                        self.draw_Dog(self,self.dogActor,k)
                        pygame.display.update()
                        pygame.time.wait(100)
                        self.displayGraphics(self)
                        pygame.display.update()
                        
                self.dogActor.state = EnumDogState.LOOK

                self.draw_Dog(self,self.dogActor,frame = 0)
                pygame.display.update()
                pygame.time.wait(400)
                self.displayGraphics(self)

                self.dogActor.state = EnumDogState.JUMP_UP

                for i in range(5):
                    self.draw_Dog(self,self.dogActor,frame = 1)
                    pygame.display.update()
                    pygame.time.wait(60)
                    self.displayGraphics(self)
                    ActorsController.execute_move(self.dogActor)
                        
                self.dogActor.state = EnumDogState.JUMP_DOWN

                for i in range(4):
                    self.draw_Dog(self,self.dogActor,frame = 2)
                    pygame.display.update()
                    pygame.time.wait(100)
                    self.displayGraphics(self)
                    ActorsController.execute_move(self.dogActor)
                            #ActorsController.execute_move(ActorsController,UIMainWindow.duckActor)
                            #action = PlayerController.update_action(self.game)

                self.dogActor.state = EnumDogState.NOTHING
                self.duckActor.state = EnumDuckState.RIGHTFLY
                intro_active = False
                game_active = True


            ###  Game starts here!!! 
            if game_active:
                if generate_sprites:
                    self.duckActor = BlackDuck(xPos = randint(10,540), yPos= 270, flyingSpeed = 4.5 ,
                     flyingDirection = "right", endXpos = 550, endYpos = 0, blackScore = 500, state = EnumDuckState.RIGHTFLY )
                    generate_sprites = False

                nextLevel = False
                if nextLevel == False:
                     #randint(1,2)
                    if self.duckActor.flyingDirection == "right":
                        
                        if self.duckActor.state == EnumDuckState.RIGHTFLY :
                            
                            self.draw_Duck(self,self.duckActor,frame)
                            pygame.display.update()
                            pygame.time.wait(100)
                            self.displayGraphics(self)
                            pygame.display.update()
                            ActorsController.execute_move(self.duckActor)
                            frame += 1
                            if frame > 2:
                                frame = 0
                            if self.duckActor.xPos > 550 or self.duckActor.yPos < 0:
                                self.duckActor.flyingDirection = "left"
                                frame = 0  
                                self.duckActor.state = EnumDuckState.LEFTFLY

                        if self.duckActor.state == EnumDuckState.DIE:
                            frame = 0
                            self.draw_Duck(self,self.duckActor,frame)
                            pygame.display.update()
                            pygame.time.wait(700)
                            self.displayGraphics(self)
                            pygame.display.update()
                            falling = True
                            while falling:
                                frame = 1
                                self.draw_Duck(self,self.duckActor,frame)
                                pygame.display.update()
                                pygame.time.wait(100)
                                self.displayGraphics(self)
                                frame = 2
                                self.draw_Duck(self,self.duckActor,frame)
                                pygame.display.update()
                                pygame.time.wait(100)
                                self.displayGraphics(self)
                                ActorsController.execute_move(self.duckActor)
                                if self.duckActor.yPos >=280:
                                    self.dogActor.state = EnumDogState.CATCHUP
                                    self.dogActor.xPos = self.duckActor.xPos
                                    self.dogActor.yPos = self.duckActor.yPos
                                    for i in range(6):
                                        frame=0
                                        self.draw_Dog(self,self.dogActor,frame)
                                        pygame.display.update()
                                        
                                        self.displayGraphics(self)
                                        pygame.time.wait(100)
                                        pygame.display.update()
                                        ActorsController.execute_move(self.dogActor)
                                    self.dogActor.state = EnumDogState.CATCHDOWN   
                                    for i in range(6):
                                        frame=0
                                        self.draw_Dog(self,self.dogActor,frame)
                                        pygame.display.update()
                                        
                                        self.displayGraphics(self)
                                        pygame.time.wait(100)
                                        pygame.display.update()
                                        ActorsController.execute_move(self.dogActor)
                                    falling = False
                            

                            nextLevel = True
                            game_active = False
                            intro_active = True
                            generate_sprites = True
                    
                    if self.duckActor.flyingDirection == "left":

                        if self.duckActor.state == EnumDuckState.LEFTFLY :
                            
                            self.draw_Duck(self,self.duckActor,frame)
                            pygame.display.update()
                            pygame.time.wait(100)
                            self.displayGraphics(self)
                            pygame.display.update()
                            ActorsController.execute_move(self.duckActor)
                            frame += 1
                            if frame > 2:
                                frame = 0
                            if self.duckActor.xPos < 0 or self.duckActor.yPos > 270:
                                self.duckActor.flyingDirection = "right"
                                frame = 0  
                                self.duckActor.state = EnumDuckState.RIGHTFLY  

                        if self.duckActor.state == EnumDuckState.DIE:
                            frame = 0
                            self.draw_Duck(self,self.duckActor,frame)
                            pygame.display.update()
                            pygame.time.wait(700)
                            self.displayGraphics(self)
                            pygame.display.update()
                            falling = True
                            while falling:
                                frame = 1
                                self.draw_Duck(self,self.duckActor,frame)
                                pygame.display.update()
                                pygame.time.wait(100)
                                self.displayGraphics(self)
                                frame = 2
                                self.draw_Duck(self,self.duckActor,frame)
                                pygame.display.update()
                                pygame.time.wait(100)
                                self.displayGraphics(self)
                                ActorsController.execute_move(self.duckActor)
                                if self.duckActor.yPos >=280:
                                    self.dogActor.state = EnumDogState.CATCHUP
                                    self.dogActor.xPos = self.duckActor.xPos
                                    self.dogActor.yPos = self.duckActor.yPos
                                    for i in range(6):
                                        frame=0
                                        self.draw_Dog(self,self.dogActor,frame)
                                        pygame.display.update()
                                        
                                        self.displayGraphics(self)
                                        pygame.time.wait(100)
                                        pygame.display.update()
                                        ActorsController.execute_move(self.dogActor)
                                    self.dogActor.state = EnumDogState.CATCHDOWN   
                                    for i in range(6):
                                        frame=0
                                        self.draw_Dog(self,self.dogActor,frame)
                                        pygame.display.update()
                                        
                                        self.displayGraphics(self)
                                        pygame.time.wait(100)
                                        pygame.display.update()
                                        ActorsController.execute_move(self.dogActor)
                                    falling = False
                            

                            nextLevel = True
                            game_active = False
                            intro_active = True
                            generate_sprites = True          


    
                  
        pygame.quit()
        
    @staticmethod
    def draw_Dog(self,actor,frame):

        if actor.state == 'Sniff':
            self.screen.blit(self.dogDict["Sniff"][frame],(actor.xPos,actor.yPos))

        if actor.state == 'Sniff1':
            self.screen.blit(self.dogDict["Sniff1"][frame],(actor.xPos,actor.yPos))

        if actor.state == 'Look':
            self.screen.blit(self.dogDict["Jump"][frame],(actor.xPos,actor.yPos))

        if actor.state == 'JumpUp':
            self.screen.blit(self.dogDict["Jump"][frame],(actor.xPos,actor.yPos))

        if actor.state == 'JumpDown':
            self.screen.blit(self.dogDict["Jump"][frame],(actor.xPos,actor.yPos))

        if actor.state == 'CatchUp':
            self.screen.blit(self.dogDict["Catch"][frame],(actor.xPos,actor.yPos))

        if actor.state == 'CatchDown':
            self.screen.blit(self.dogDict["Catch"][frame],(actor.xPos,actor.yPos))

    @staticmethod          
    def draw_Duck(self,actor,frame):
        if isinstance(actor,BlackDuck): 
            if actor.state == "RightFly":
                self.screen.blit(self.blackDuckDict["RightFly"][frame],(actor.xPos,actor.yPos))

            if actor.state == "LeftFly":
                self.screen.blit(self.blackDuckDict["LeftFly"][frame],(actor.xPos,actor.yPos))

            if actor.state == "Die":
                self.screen.blit(self.blackDuckDict["Die"][frame],(actor.xPos,actor.yPos))

    def displayGraphics(self):
        self.screen.blit(self.background_surf,(0,0))
 
        pygame.draw.rect(self.screen, 'black', (86, 387, 35, 18), 200)
        self.screen.blit(self.level_surf,self.level_rect)
        pygame.draw.rect(self.screen, 'black', (410, 419, 108, 18), 200)
        self.screen.blit(self.score_surf,self.score_rect)

    def displayGround(self):
        self.screen.blit(self.ground_surf,(0,0))    

window = GameController(Game,UIMainWindow)
window.startGame()
