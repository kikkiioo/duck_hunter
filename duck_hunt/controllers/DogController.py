class DogController:

    @staticmethod
    def sniff(dogActor,dt):
        dogActor.xPos +=  50 * dt

    @staticmethod
    def jumpUp(dogActor, dt):
        dogActor.xPos += 45 * dt
        dogActor.yPos -= 55 * dt

    @staticmethod
    def jumpDown(dogActor, dt):
        dogActor.xPos += 15 * dt
        dogActor.yPos += 30 * dt

    @staticmethod
    def catchUp(dogActor, dt):
        dogActor.yPos -= 10 * dt

    @staticmethod
    def catchDown(dogActor, dt):
        dogActor.yPos += 10 * dt



