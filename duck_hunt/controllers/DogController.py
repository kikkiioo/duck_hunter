import pygame
from models.Dog import Dog
import UIMainWindow


class DogController:

    def sniff(dogActor):
        # time_last = time.time()
        for j in range(4):
            for i in UIMainWindow.dogDict["Sniff"]:
                #screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
                # dt = time.time() - time_last
                # time_last = time.time()
                pygame.display.update()
                dogActor.Xpos += 10 #*dt
                pygame.time.wait(100)
                UIMainWindow.displayGraphics()
                

        for l in range(4):
            for k in UIMainWindow.dogDict["Sniff1"]:
                #screen.blit(k,(dogActor.Xpos,dogActor.Ypos))
                pygame.display.update()
                pygame.time.wait(100)
                UIMainWindow.displayGraphics()


    def jump(dogActor):
        
        i = UIMainWindow.dogDict["Jump"][0]
        #screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
        pygame.display.update()
        pygame.time.wait(400)
        UIMainWindow.displayGraphics()
        for i in range(5):
            i = UIMainWindow.dogDict["Jump"][1]
            #screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
            pygame.display.update()
            dogActor.Xpos+=15
            dogActor.Ypos-=30
            pygame.time.wait(60)
            UIMainWindow.displayGraphics()
            
        for i in range(4):
            i = UIMainWindow.dogDict["Jump"][2]
            #screen.blit(i,(dogActor.Xpos,dogActor.Ypos))
            pygame.display.update()
            dogActor.Xpos+=15
            dogActor.Ypos+=30
            pygame.time.wait(100)
            UIMainWindow.displayGraphics()
            
