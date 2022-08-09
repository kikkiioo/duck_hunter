from time import time
import pygame
import time


from controllers.GameController import GameController
from models.Game import Game
from models.EnumDuckState import EnumDuckState
from models.EnumDogState import EnumDogState
from models.BlackDuck import BlackDuck
from models.Dog import Dog
from models.Player import Player


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

        # Dog animations
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
        self.dogDict = {"Sniff": [self.sniff1, self.sniff2, self.sniff3, self.sniff4],
                        "Sniff1": [self.sniff5, self.sniff6],
                        "Jump": [self.jump1, self.jump2, self.jump3],
                        "Catch": [self.catch]}

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
                              "Die": [self.blackDuckDie1, self.blackDuckDie2, self.blackDuckDie3],
                              "LeftFly": [self.leftFlyBlack1, self.leftFlyBlack2, self.leftFlyBlack3]}

    def start_main_loop(self):
        self.__init__(self)
        self.displayGraphics(self)
        pygame.display.update()
        self.generateSprites(self)

        is_running = True
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
                    GameController.checkCollision(self, self.game, x, y)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.newGame(self)

            #GameController.updateSprites(self.game)  # update ducks !

            GameController.updateRender(self, self.game)
            GameController.updateControllers(self.game, dt)
            pygame.display.flip()
            self.clock.tick(60)
            self.displayGraphics(self)
            pygame.display.update()

        pygame.quit()

    @staticmethod
    def draw_Dog(self, actor, frame):

        if actor.state == 'Sniff':
            self.screen.blit(self.dogDict["Sniff"][frame], (actor.xPos, actor.yPos))

        if actor.state == 'Sniff1':
            self.screen.blit(self.dogDict["Sniff1"][frame], (actor.xPos, actor.yPos))

        if actor.state == 'Look':
            self.screen.blit(self.dogDict["Jump"][frame], (actor.xPos, actor.yPos))

        if actor.state == 'JumpUp':
            self.screen.blit(self.dogDict["Jump"][frame], (actor.xPos, actor.yPos))

        if actor.state == 'JumpDown':
            self.screen.blit(self.dogDict["Jump"][frame], (actor.xPos, actor.yPos))

        if actor.state == 'CatchUp':
            self.screen.blit(self.dogDict["Catch"][frame], (actor.xPos, actor.yPos))

        if actor.state == 'CatchDown':
            self.screen.blit(self.dogDict["Catch"][frame], (actor.xPos, actor.yPos))

    @staticmethod
    def draw_Duck(self, actor, frame):
        if isinstance(actor, BlackDuck):
            if actor.state == "RightFly":
                self.screen.blit(self.blackDuckDict["RightFly"][frame], (actor.xPos, actor.yPos))

            if actor.state == "LeftFly":
                self.screen.blit(self.blackDuckDict["LeftFly"][frame], (actor.xPos, actor.yPos))

            if actor.state == "Die":
                self.screen.blit(self.blackDuckDict["Die"][frame], (actor.xPos, actor.yPos))

    @staticmethod
    def displayGraphics(self):
        self.screen.blit(self.background_surf, (0, 0))
        pygame.draw.rect(self.screen, 'black', (86, 387, 35, 18), 200)
        self.screen.blit(self.level_surf, self.level_rect)
        self.displayScore(self)

    def displayGround(self):
        self.screen.blit(self.ground_surf, (0, 0))

    def generateSprites(self):

        player = Player(xPos=0, yPos=0, shotCount=3, hitCount=0, successShotCount=0)
        dogActor = Dog(xPos=10, yPos=320, state=EnumDogState.SNIFF)
        duckActor = BlackDuck(xPos=150, yPos=270, flyingSpeed=4.5, flyingDirection="right", endXpos=550, endYpos=0,
                                   blackScore=500, state=EnumDuckState.NOTHING)
        self.game.actors.append(player)
        self.game.actors.append(dogActor)
        self.game.actors.append(duckActor)

    @staticmethod
    def newGame(self):
        self.game = Game()
        self.generateSprites(self)
        self.start_main_loop(self)

    def displayScore(self):
        pygame.draw.rect(self.screen, 'black', (410, 419, 108, 18), 200)
        self.score_surf = self.test_font.render(str(self.game.score), True, 'white')
        self.screen.blit(self.score_surf, self.score_rect)


window = GameController(UIMainWindow)
window.startGame()