
class DuckController:

    @staticmethod
    def flyRight(duckActor, dt):
        # dx,dy = (duckActor.endXpos - duckActor.xPos, duckActor.endYpos - duckActor.yPos  )
        # stepx,stepy = (dx/25., dy/25. )
        # duckActor.xPos += stepx
        # duckActor.yPos += stepy

        duckActor.xPos += 30 * dt
        duckActor.yPos -= 30 * dt

    @staticmethod
    def flyLeft(duckActor, dt):
        # dx,dy = (duckActor.endXpos - duckActor.xPos, duckActor.endYpos - duckActor.yPos  )
        # stepx,stepy = (dx/25., dy/25. )
        # duckActor.xPos += stepx
        # duckActor.yPos += stepy

        duckActor.xPos -= 30 * dt
        duckActor.yPos += 30 * dt

    @staticmethod
    def die(duckActor, dt):

        duckActor.yPos += 30 * dt