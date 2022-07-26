from cgi import test
from enum import Enum
import enum
from multiprocessing.dummy import Array
from pickle import FALSE
import string
from time import time

from types import NoneType
from dacite import Dict
import pygame
import time
from sys import exit
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

from sympy import fps

from controllers.ActorController import ActorsController
from controllers.GameController import GameController
from models.Game import Game
from models.Dog import Dog



global screen 
screen = pygame.display.set_mode((550,480))





#view 
class UIMainWindow:
    def __init__(self):
        self.background_surf = pygame.image.load('graphics/background.png').convert_alpha()
        self.level0 = pygame.image.load('graphics/level_numbers/0.png').convert_alpha()
        self.sniff1 = pygame.image.load('graphics/dog/sniff1.png').convert_alpha()
        self.sniff2 = pygame.image.load('graphics/dog/sniff2.png').convert_alpha()
        self.sniff3 = pygame.image.load('graphics/dog/sniff3.png').convert_alpha()
        self.sniff4 = pygame.image.load('graphics/dog/sniff4.png').convert_alpha()
        self.sniff5 = pygame.image.load('graphics/dog/sniff5.png').convert_alpha()
        self.sniff6 = pygame.image.load('graphics/dog/sniff6.png').convert_alpha()
        self.jump1 = pygame.image.load('graphics/dog/jump1.png').convert_alpha()
        self.jump2 = pygame.image.load('graphics/dog/jump2.png').convert_alpha()
        self.jump3 = pygame.image.load('graphics/dog/jump3.png').convert_alpha()
        self.dogDict = {"Sniff": [self.sniff1,self.sniff2,self.sniff3,self.sniff4],
                    "Sniff1": [self.sniff5,self.sniff6],
                    "Jump": [self.jump1,self.jump2,self.jump3]}

        dogActor = Dog(Xpos = 10, Ypos=320,State= 'Sniff')

    def start_main_loop(self):
        self.game = Game(1,0,3,None)
        self.displayGraphics()

        
        ActorsController.execute_move(UIMainWindow.dogActor)
   

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
    def displayGraphics(self):

        pygame.init()
        screen = pygame.display.set_mode((550,480))
        
        pygame.display.set_caption('Duck hunt')
    
        
        screen.blit(UIMainWindow.background_surf,(0,0))
        screen.blit(UIMainWindow.level0,(86,388))
        pygame.display.update()
            

   
window = GameController(Game,UIMainWindow)
window.startGame()

