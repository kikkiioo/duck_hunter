import json
from time import time
import pygame
import time
from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json


from controllers.GameController import GameController
from models.Game import Game
from models.EnumDuckState import EnumDuckState
from models.EnumDogState import EnumDogState
from models.Duck import Duck
from models.Dog import Dog



class UIMainWindow:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Duck hunt')

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((550, 480))
        self.background_surf = pygame.image.load('graphics/background.png').convert_alpha()
        self.ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
        self.test_font = pygame.font.Font('font/Pixeltype.ttf', 30)
        self.level_surf = self.test_font.render('01', True, 'white')
        self.level_rect = self.level_surf.get_rect(topleft=(95, 388))
        self.score_surf = self.test_font.render('', True, 'white')
        self.score_rect = self.level_surf.get_rect(topleft=(470, 419))
        self.pause = pygame.image.load('graphics/pause.png').convert_alpha()

        # Dog animations
        self.sniff1 = pygame.image.load('graphics/dog/sniff1.png').convert_alpha()
        self.sniff2 = pygame.image.load('graphics/dog/sniff2.png').convert_alpha()
        self.sniff3 = pygame.image.load('graphics/dog/sniff3.png').convert_alpha()
        self.sniff4 = pygame.image.load('graphics/dog/sniff4.png').convert_alpha()
        self.sniff5 = pygame.image.load('graphics/dog/sniff5.png').convert_alpha()
        self.sniff6 = pygame.image.load('graphics/dog/sniff6.png').convert_alpha()
        self.look = pygame.image.load('graphics/dog/jump1.png').convert_alpha()
        self.jump2 = pygame.image.load('graphics/dog/jump2.png').convert_alpha()
        self.jump3 = pygame.image.load('graphics/dog/jump3.png').convert_alpha()
        self.catch = pygame.image.load('graphics/dog/catch.png').convert_alpha()
        self.dogDict = {"Sniff": [self.sniff1, self.sniff2, self.sniff3, self.sniff4],
                        "Sniff1": [self.sniff5, self.sniff6],
                        "Look":[self.look],
                        "JumpUp": [ self.jump2],
                        "JumpDown": [self.jump3],
                        "CatchUp": [self.catch],
                        "CatchDown": [self.catch]}

        # Duck animations
        self.rightFlyBlack1 = pygame.image.load('graphics/duck/blackDuck/fly1.png').convert_alpha()
        self.rightFlyBlack2 = pygame.image.load('graphics/duck/blackDuck/fly2.png').convert_alpha()
        self.rightFlyBlack3 = pygame.image.load('graphics/duck/blackDuck/fly3.png').convert_alpha()
        self.leftFlyBlack1 = pygame.image.load('graphics/duck/blackDuck/fly4.png').convert_alpha()
        self.leftFlyBlack2 = pygame.image.load('graphics/duck/blackDuck/fly5.png').convert_alpha()
        self.leftFlyBlack3 = pygame.image.load('graphics/duck/blackDuck/fly6.png').convert_alpha()

        self.blackDuckDie1 = pygame.image.load('graphics/duck/blackDuck/die1.png').convert_alpha()
        self.blackDuckDie2 = pygame.image.load('graphics/duck/blackDuck/die2.png').convert_alpha()
        self.blackDuckDie3 = pygame.image.load('graphics/duck/blackDuck/die3.png').convert_alpha()

        self.game = Game(list(), level=1, score=0, shotCount=0, isNextLevel=False, isGameOver=False,
                         animation_duration=0, animation_start_time = 0)

        self.blackDuckDict = {"RightFly": [self.rightFlyBlack1, self.rightFlyBlack2, self.rightFlyBlack3],
                              "Die": [self.blackDuckDie1],
                              "Fall": [self.blackDuckDie2, self.blackDuckDie3],
                              "LeftFly": [self.leftFlyBlack1, self.leftFlyBlack2, self.leftFlyBlack3]}

    def start_main_loop(self):

        self.displayGraphics()
        pygame.display.update()
        GameController.generateActors(self.game)

        is_running = True
        paused = False
        time_last = time.time()
        self.game.animation_start_time = time.time()

        while is_running:

            dt = time.time() - time_last
            time_last = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    GameController.checkCollision(self.game, x, y)
                    self.displayScore()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.game.actors.clear()
                        self.newGame()
                    if event.key == pygame.K_p:
                        paused = True
                        self.saveGame()
                    if event.key == pygame.K_r:
                        paused = False
                        self.resumeGame()

            if not paused:
                GameController.updateControllers(self.game, dt)
                self.displayGraphics()
                self.render()
                GameController.updateActors(self.game, dt)
                pygame.display.update()

        pygame.quit()

    def displayGraphics(self):
        self.screen.blit(self.background_surf, (0, 0))
        pygame.draw.rect(self.screen, 'black', (86, 387, 35, 18), 200)
        self.screen.blit(self.level_surf, self.level_rect)
        self.displayScore()

    def displayGround(self):
        self.screen.blit(self.ground_surf, (0, 0))


    def render(self):
        for actor in self.game.actors:
            if actor.state == "None":
                continue

            if isinstance(actor,Dog):
                state_png = self.dogDict[actor.state]
                self.screen.blit(state_png[int(actor.frame)],(actor.xPos,actor.yPos))

            if isinstance(actor,Duck):
                state_png = self.blackDuckDict[actor.state]
                self.screen.blit(state_png[int(actor.frame)],(actor.xPos,actor.yPos))

    def displayScore(self):
        pygame.draw.rect(self.screen, 'black', (410, 419, 108, 18), 200)
        self.score_surf = self.test_font.render(str(self.game.score), True, 'white')
        self.screen.blit(self.score_surf, self.score_rect)

    def newGame(self):
        self.start_main_loop()

    def saveGame(self):
        self.screen.blit(self.pause, (-20, 0))
        pygame.display.flip()
        savedGame = self.game
        json_file = savedGame.to_json()
        with open("data.json", "w") as outfile:
            outfile.write(json_file)
        for actor in self.game.actors:
            if isinstance(actor,Duck):
                actor.state = EnumDuckState.NOTHING
            if isinstance(actor,Dog):
                actor.state = EnumDogState.NOTHING

    def resumeGame(self):
        with open("data.json", 'r', encoding='utf-8') as f:
            data = f.read()
        print(data)
        self.game.from_json(data)


window = UIMainWindow()
window.start_main_loop()