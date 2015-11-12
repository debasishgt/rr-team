from direct.actor.Actor import Actor
from panda3d.core import CollisionSphere, CollisionBox, CollisionNode
from panda3d.core import Point3

class CarActor(Actor):
    def __init__(self, carType, playerID):
        if carType == 'ralph':
            Actor.__init__(self, "models/ralph", {"run":"models/ralph-run","walk":"models/ralph-walk"})
            self.maxLinearSpeed = 3
            self.linearSpeed = 0
            self.angularSpeed = 1
            self.setScale(0.2)
        elif carType == 'bike':
            self.maxSpeed = 20
            self.currentSpeed = 0
            print "It's a bike"
        Actor.setPythonTag(self, "subclass", self)
        if playerID == "Me":
            self.setPos(30,0,0)
            self.mass = 1
        else:
            self.setPos(10,0,0)
            self.mass = 500

        self.showBounds()
        self.isMoving = False
        self.playerID = playerID
        self.collisionNodeNames = []
        self.collisionNodePaths = []
        self.addCollisionNodes()

    def addCollisionNodes(self):
        carRadius = 3.22886
        # minPt, maxPt = Point3(), Point3()
        # self.calcTightBounds(minPt, maxPt)
        # xDim = abs(maxPt.getX() - minPt.getX())
        # yDim = abs(maxPt.getY() - minPt.getY())
        # zDim = abs(maxPt.getZ() - minPt.getZ())
        # bounds = self.getBounds()
        # radius = bounds.getRadius()
        radius = carRadius/2.0
        self.addCollisionNode('r', Point3(-radius-1.5, 0, carRadius), radius, radius, carRadius)
        self.addCollisionNode('l', Point3(radius+1.5, 0, carRadius), radius, radius, carRadius)
        self.addCollisionNode('b', Point3(0, radius+1.5, carRadius), radius, radius, carRadius)
        self.addCollisionNode('f', Point3(0, -radius-1.5, carRadius), radius, radius, carRadius)




    def addCollisionNode(self, sideTitle, center, dx, dy, dz):
        nodeName = sideTitle+self.playerID
        self.collisionNodeNames.append(nodeName)
        self.cNodePath = self.attachNewNode(CollisionNode(nodeName))
        if sideTitle == 'f':
            sphere = CollisionSphere(center.x, center.y, center.z, dy)
            self.cNodePath.node().addSolid(sphere)
        else:
            box = CollisionBox(center, dx, dy, dz)
            self.cNodePath.node().addSolid(box)
        self.cNodePath.show()
        self.collisionNodePaths.append(self.cNodePath)

    def updateLinearSpeed(self, linearSpeed):
        self.linearSpeed += linearSpeed
        self.clampLinearSpeed()
        self.setY(self, -25 * self.linearSpeed * globalClock.getDt())

    def clampLinearSpeed(self):
        self.linearSpeed =  max(min(self.maxLinearSpeed, self.linearSpeed), 0)

    def steerLeft(self):
        self.setH(self.getH() + 300 * globalClock.getDt())

    def steerRight(self):
        self.setH(self.getH() - 300 * globalClock.getDt())

    def walk(self):
        self.stop()
        self.pose("walk",5)
        self.isMoving = False

    def run(self):
        self.loop("run")
        self.isMoving = True
