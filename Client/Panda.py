__author__ = 'ASPIRE'


class MyPanda:
    count = 0

    def __init__(self, tempworld):
        self.isWalk = False
        self.jumpState = False
        self.currentTime = 0
        self.idleTime = 0
        self.pandaPosIntervalX = 0
        self.pandaPaceX = None
        self.pandaPace = None
        self.mySequence = None
        MyPanda.count += 1
        self.myInterval1 = 0
        self.myInterval2 = 0
        self.myInterval3 = 0
        self.myInterval4 = 0
        self.pandaPosInterval1 = 0
        self.id = MyPanda.count
        self.world = tempworld

        self.pandaNode = render.attachNewNode('pandaNode')
        self.actor = Actor("models/panda-model",
                           {"walk": "models/panda-walk4"})
        self.actor.reparentTo(self.pandaNode)
        cPos = int(self.id) * 20
        self.actor.setPos(cPos, 0, 0)
        self.actor.setScale(0.002, 0.002, 0.002)

        # Create a collsion node for this object.
        self.cNode = CollisionNode('panda')
        # Attach a collision sphere solid to the collision node.
        self.cNode.addSolid(CollisionSphere(2, 0, 400, 500))
        # Attach the collision node to the object's model.
        self.frowneyC = self.actor.attachNewNode(self.cNode)
        # self.frowneyC.show()
        base.cTrav.addCollider(self.frowneyC, self.world.pusher)
        self.world.pusher.addCollider(self.frowneyC, self.actor, base.drive.node())

        self.setJumpSequence()

    def setJumpSequence(self):
        self.myInterval1 = self.actor.posInterval(0.3, Point3(self.actor.getX(), self.actor.getY(), 0))
        self.myInterval2 = self.actor.posInterval(0.3, Point3(self.actor.getX(), self.actor.getY(), 1))
        self.myInterval3 = self.actor.posInterval(0.2, Point3(self.actor.getX(), self.actor.getY(), 1))
        self.myInterval4 = self.actor.posInterval(0.1, Point3(self.actor.getX(), self.actor.getY(), 0))
        self.mySequence = Sequence(self.myInterval1, self.myInterval2, self.myInterval3, self.myInterval4)

    def getActor(self):
        return self.actor

    def timerTask(self, task):
        self.currentTime = int(task.time)
        return Task.cont

    def jumpPanda(self, task):
        if (int(self.currentTime) - int(self.idleTime) > 20 and self.jumpState == False and self.getDist() > 20):
            self.setJumpSequence()
            self.jumpState = True
            print "Jump"
            self.mySequence.start()
            self.mySequence.loop()
        return Task.cont

    def getDist(self):
        distanceVector = self.world.mainChar.getPos() - self.actor.getPos()
        dist = distanceVector.length()

        return dist

    def getId(self):
        return self.id

    def walkSequence(self):
        if self.isWalk == False:
            self.actor.play("walk")
            self.actor.loop("walk")
            self.isWalk = True
        self.actor.setPos(self.actor, 0, 5, 0)
        self.pandaMovement = self.pandaNode.hprInterval(10.0, Point3(0, 0, 0),
                                                        startHpr=Point3(self.actor.getX(), self.actor.getY(), 0))

    def pandaWalk(self, task):
        if (self.getDist() < 15 and self.getDist() > 3.5):
            self.idleTime = self.currentTime
            # Look at Ralph
            self.actor.find('**/+GeomNode').setH(180)
            self.actor.lookAt(self.world.mainChar)

            if self.jumpState == True:
                print "Stop Jump"
                self.jumpState = False
                # self.idleTime = self.currentTime
                self.mySequence.pause()
                self.actor.setPos(self.actor.getX(), self.actor.getY(), 0)
                print "Start Walk"

            self.walkSequence()
        if self.getDist() < 15 and self.actor.getZ() != 0:
            self.actor.setPos(self.actor.getX(), self.actor.getY(), 0)
        return Task.cont

    def pandaStop(self, task):
        if (self.getDist() > 15 or self.getDist() < 3.5) and self.isWalk:
            print "Stop Walk"
            self.isWalk = False
            self.actor.stop()
        return Task.cont

# --------------------- MyPanda Class END-------------------------------#