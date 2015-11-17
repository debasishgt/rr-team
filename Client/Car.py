__author__ = 'ASPIRE'


class MyCar():
    def __init__(self, inWorld):
        self.world = inWorld
        self.x = 1
        self.y = 0
        self.carNode = render.attachNewNode('models/dummy_car')
        self.world.car = loader.loadModel("models/knucklehead.egg")
        self.car_tex = loader.loadTexture("models/knucklehead.jpg")
        self.world.car.setTexture(self.car_tex, 1)
        self.world.car.reparentTo(self.carNode)
        self.world.car.setPos(20, 20, 0)
        self.world.car.setScale(.08)
        self.world.car.setP(-90)
        self.world.car.setColor(0.6, 0.6, 1.0, 1.0)
        self.world.car.setColorScale(0.6, 0.6, 1.0, 1.0)
        self.actor = self.world.car

    def makeCircle(self, task):
        distance = self.getDistance()
        if distance < 5:
            self.actor.setH(-500)
            self.actor.setPos(self.world.mainChar.getX() + distance * math.cos(self.x),
                              self.world.mainChar.getY() - distance * math.sin(self.x), 0)
            self.actor.lookAt(self.world.mainChar)
            self.actor.setP(-90)
            self.actor.setH(self.actor.getH() + 45)
            self.x = self.x + math.pi / 80
            if (self.x > 4 * math.pi):
                self.actor.setH(-500)
                tempInterval = self.actor.posInterval(5, Point3(self.actor.getX() + 10, self.world.mainChar.getY() - 10,
                                                                0),
                                                      startPos=Point3(self.actor.getX(), self.actor.getY(), 0))
                # Create and play the sequence that coordinates the intervals.

                driveAway = Sequence(tempInterval, name="driveAway")
                driveAway.start()
                self.x = -1
            time.sleep(0.01)

        return task.cont

    def getDistance(self):
        distanceVector = self.world.mainChar.getPos() - self.actor.getPos()
        distance = distanceVector.length()

        return distance


        # --------------------- MyCar Class END-------------------------------#
