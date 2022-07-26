from cgi import test
from enum import Enum
import enum
from multiprocessing.dummy import Array
from pickle import FALSE
import string
from time import time
from tokenize import Double
from types import NoneType
from dacite import Dict
import pygame
import time
from sys import exit
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

from sympy import fps


global screen 
screen = pygame.display.set_mode((550,480))

#model
@dataclass_json
@dataclass 
class Actor:
    Xpos: Double = 0
    Ypos: Double = 0

@dataclass_json
@dataclass 
class Game:
    Level : int
    Score: int
    ShotCount: int
    actors: List[Actor] = field(default_factory= list)

@dataclass_json
@dataclass
class EnumDogState():
    Nothing = 'None'
    Sniff = 'Sniff'
    Jump = 'Jump'
    Catch = 'Catch'
    Giggle = 'Giggle'
    Bark = 'Bark'

@dataclass_json
@dataclass
class Dog(Actor):
    State: EnumDogState = 'None'

@dataclass_json
@dataclass
class EnumDuckState:
    Nothing = 'None'
    Fly = 'Fly'
    Die = 'Die'
    Quack = 'Quack'

@dataclass_json
@dataclass
class Duck(Actor):
    state: EnumDuckState = 'None'
    flyingSpeed: Double = 0
    flyingDirection: string = "left"
    endXpos: Double = 0
    endYpos: Double = 0

@dataclass_json
@dataclass
class RedDuck(Duck):
    redScore: int = 0

@dataclass_json
@dataclass    
class BlueDuck(Duck):
    blueScore: int = 0

@dataclass_json
@dataclass 
class BlackDuck(Duck):
    blackScore: int =0

@dataclass_json
@dataclass 
class EnumPlayerState:
    Nothing = 'None'

@dataclass_json
@dataclass 
class Player(Actor):
    state: EnumPlayerState = 'None'
    shotCount: int = 0
    hitCount: int = 0
    successShotCount: int = 0

#controllers

class GameController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def startGame(self):
        self.view.start_main_loop(UIWindow)

class ActorsController:

    def __init__(self,view, actor):
        self.view = view
        self.actor = actor

    def execute_move(self,actor):

        if isinstance(self.actor,Dog):
            if actor.State == 'Sniff':
                DogController.sniff(UIWindow.dogActor)
                self.actor.State = 'Jump'
            if actor.State == 'Jump':   
                DogController.jump(UIWindow.dogActor)

class DogController:

    def sniff(dogActor):
        # time_last = time.time()
        for j in range(4):
            for i in UIWindow.dogDict["Sniff"]:
                screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
                # dt = time.time() - time_last
                # time_last = time.time()
                pygame.display.update()
                dogActor.Xpos += 10 #*dt
                pygame.time.wait(100)
                UIWindow.displayGraphics()
                

        for l in range(4):
            for k in UIWindow.dogDict["Sniff1"]:
                screen.blit(k,(dogActor.Xpos,dogActor.Ypos))
                pygame.display.update()
                pygame.time.wait(100)
                UIWindow.displayGraphics()


    def jump(dogActor):
        
        i = UIWindow.dogDict["Jump"][0]
        screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
        pygame.display.update()
        pygame.time.wait(400)
        UIWindow.displayGraphics()
        for i in range(5):
            i = UIWindow.dogDict["Jump"][1]
            screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
            pygame.display.update()
            dogActor.Xpos+=15
            dogActor.Ypos-=30
            pygame.time.wait(60)
            UIWindow.displayGraphics()
            
        for i in range(4):
            i = UIWindow.dogDict["Jump"][2]
            screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
            pygame.display.update()
            dogActor.Xpos+=15
            dogActor.Ypos+=30
            pygame.time.wait(100)
            UIWindow.displayGraphics()
            

#view 
class UIWindow:

    background_surf = pygame.image.load('graphics/background.png').convert_alpha()
    level0 = pygame.image.load('graphics/level_numbers/0.png').convert_alpha()
    sniff1 = pygame.image.load('graphics/dog/sniff1.png').convert_alpha()
    sniff2 = pygame.image.load('graphics/dog/sniff2.png').convert_alpha()
    sniff3 = pygame.image.load('graphics/dog/sniff3.png').convert_alpha()
    sniff4 = pygame.image.load('graphics/dog/sniff4.png').convert_alpha()
    sniff5 = pygame.image.load('graphics/dog/sniff5.png').convert_alpha()
    sniff6 = pygame.image.load('graphics/dog/sniff6.png').convert_alpha()
    jump1 = pygame.image.load('graphics/dog/jump1.png').convert_alpha()
    jump2 = pygame.image.load('graphics/dog/jump2.png').convert_alpha()
    jump3 = pygame.image.load('graphics/dog/jump3.png').convert_alpha()
    dogDict = {"Sniff": [sniff1,sniff2,sniff3,sniff4],"Sniff1": [sniff5,sniff6],
                "Jump": [jump1,jump2,jump3]}

    dogActor = Dog(Xpos = 10, Ypos=320,State= 'Sniff')

    def start_main_loop(self):
        self.game = Game(1,0,3,None)
        self.displayGraphics()

        dogCon = ActorsController(UIWindow,UIWindow.dogActor)
        ActorsController.execute_move(dogCon,UIWindow.dogActor)
   

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
    def displayGraphics():

        pygame.init()
        screen = pygame.display.set_mode((550,480))
        
        pygame.display.set_caption('Duck hunt')
    
        
        screen.blit(UIWindow.background_surf,(0,0))
        screen.blit(UIWindow.level0,(86,388))
        pygame.display.update()
            

   
window = GameController(Game,UIWindow)
window.startGame()

