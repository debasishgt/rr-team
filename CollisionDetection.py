# Roaming-Ralph was modified to remove collision part.
from math import sqrt, pow

import direct.directbase.DirectStart
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from panda3d.core import TextureStage, Texture
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from panda3d.core import CollisionSphere, CollisionNode
from panda3d.core import CollisionTraverser, CollisionHandlerEvent
from CarActor import CarActor

path = ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', '', 'f', '', '', 'f', 'f', 'f', '', 'f', 'f', 'f',
        'f', '', 'f', '', 'f', 'f', 'f', 'f', 'f', '', 'f', 'f', '', 'f', '', 'f', 'f', 'f', 'f', 'f',
        'f', '', 'f', '', 'f', 'f', 'f', 'f', 'f', '', '', '', '', 'f', '', 'f', '', '', '', '', '', '',
        'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', '', 'f', '', '', 'f', 'f', 'f', '', 'f', 'f', 'f',
        'f', '', 'f', '', 'f', 'f', 'f', 'f', 'f', '', 'f', 'f', '', 'f', '', 'f', 'f', 'f', 'f', 'f',
        'f', '', 'f', '', 'f', 'f', 'f', 'f', 'f', '', '', '', '', 'f', '', 'f', '', '', '', '', '', '',
        'u']

class World(DirectObject):

    def __init__(self):

        # Initialize the traverser.
        base.cTrav = CollisionTraverser()

        # Initialize the handler.
        self.collHandEvent = CollisionHandlerEvent()
        self.collHandEvent.addInPattern('into-%in')
        # self.collHandEvent.addOutPattern('outof-%in')

        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        base.win.setClearColor(Vec4(0,0,0,1))

        # Set up the environment
        #
        self.environ = loader.loadModel("models/square")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.environ.setScale(100,100,1)
        self.moon_tex = loader.loadTexture("models/tex.jpg")
        self.moon_tex.setWrapU(Texture.WMRepeat)
        self.moon_tex.setWrapV(Texture.WMRepeat)
    	self.environ.setTexture(self.moon_tex, 1)

        self.car = CarActor('ralph', 'Me')
        self.car.reparentTo(render)
        # base.cTrav.addCollider(self.car.cNodePath, self.collHandEvent)
        self.accept('into-fMe', self.collide)
        self.accept('outof-fMe', self.collide)
        self.accept('into-bMe', self.collide)
        self.accept('outof-bMe', self.collide)
        self.accept('into-rMe', self.collide)
        self.accept('outof-rMe', self.collide)
        self.accept('into-lMe', self.collide)
        self.accept('outof-lMe', self.collide)
        for cNodePath in self.car.collisionNodePaths:
            base.cTrav.addCollider(cNodePath, self.collHandEvent)
        # for nodeName in self.car.collisionNodeNames:
        #     string = 'into-'+nodeName
        #     print string
        #     self.accept(nodeName, self.collide)
        #     string = 'outof-'+nodeName
        #     self.accept(nodeName, self.collide)

        self.crazyCar = CarActor('ralph', 'CrazyDriver')
        self.crazyCar.reparentTo(render)
        # base.cTrav.addCollider(self.crazyCar.cNodePath, self.collHandEvent)
        self.accept('into-fCrazyDriver', self.collide)
        self.accept('outof-fCrazyDriver', self.collide)
        self.accept('into-bCrazyDriver', self.collide)
        self.accept('outof-bCrazyDriver', self.collide)
        self.accept('into-lCrazyDriver', self.collide)
        self.accept('outof-lCrazyDriver', self.collide)
        self.accept('into-rCrazyDriver', self.collide)
        self.accept('outof-rCrazyDriver', self.collide)
        for cNodePath in self.crazyCar.collisionNodePaths:
            base.cTrav.addCollider(cNodePath, self.collHandEvent)
        # for nodeName in self.crazyCar.collisionNodeNames:
        #     string = 'into-'+nodeName
        #     print string
        #     self.accept(nodeName, self.collide)
        #     string = 'outof-'+nodeName
        #     self.accept(nodeName, self.collide)
        self.pathCounter = 0

        # Create a floater object.  We use the "floater" as a temporary
        # variable in a variety of calculations.
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # Accept the control keys for movement and rotation
        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left",1])
        self.accept("arrow_right", self.setKey, ["right",1])
        self.accept("arrow_up", self.setKey, ["forward",1])
        self.accept("a", self.setKey, ["cam-left",1])
        self.accept("s", self.setKey, ["cam-right",1])
        self.accept("arrow_left-up", self.setKey, ["left",0])
        self.accept("arrow_right-up", self.setKey, ["right",0])
        self.accept("arrow_up-up", self.setKey, ["forward",0])
        self.accept("a-up", self.setKey, ["cam-left",0])
        self.accept("s-up", self.setKey, ["cam-right",0])

        taskMgr.add(self.move,"moveTask")
        taskMgr.add(self.moveCrazyCar,"moveCrazyCarTask")

        # Set up the camera
        base.disableMouse()
        base.camera.setPos(self.car.getX(),self.car.getY()+10,2)

        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))

    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value

    def moveCrazyCar(self, task):
        move = path[self.pathCounter]
        linearSpeed = -0.01
        if (move == 'u'):
            self.crazyCar.setH(self.crazyCar.getH() - 180)
        if (move == 'f'):
            linearSpeed = 0.01

        self.crazyCar.updateLinearSpeed(linearSpeed)
        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.
        if (move == 'f') or (move == 'l') or (move == 'r'):
            if self.crazyCar.isMoving is False:
                self.crazyCar.run()
        else:
            if self.car.isMoving and self.car.linearSpeed == 0:
                self.crazyCar.walk()

        self.pathCounter += 1
        if self.pathCounter > len(path)-1:
            self.pathCounter = 0

        return task.cont

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):
        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.
        base.camera.lookAt(self.car)
        if (self.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())

        # If a move-key is pressed, move ralph in the specified direction.
        linearSpeed = -0.1
        if (self.keyMap["left"]!=0):
            self.car.steerLeft()
        if (self.keyMap["right"]!=0):
            self.car.steerRight()
        if (self.keyMap["forward"]!=0):
            linearSpeed = 0.1

        self.car.updateLinearSpeed(linearSpeed)
        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.
        if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
            if self.car.isMoving is False:
                self.car.run()
        else:
            if self.car.isMoving and self.car.linearSpeed == 0:
                self.car.walk()

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.
        camvec = self.car.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0

        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.
        self.floater.setPos(self.car.getPos())
        self.floater.setZ(self.car.getZ() + 2.0)
        base.camera.lookAt(self.floater)
        return task.cont

    # Collision Handler events
    def collide(self, collEntry):
        fromNodePath = collEntry.getFromNodePath()
        intoNodePath = collEntry.getIntoNodePath()

        # Point where collision occurs
        impactPoint = collEntry.getSurfacePoint(render)

        # following two variables may have values l, r, f, b
        # where l stands for left side, r for right, f for front, b for back
        fromSide = fromNodePath.getName()[0] # tells from what side car hits
        intoSide = intoNodePath.getName()[0] # tells what side of car gets hit

        # following two variables are of type CarActor
        fromCar = fromNodePath.getParent().getPythonTag("subclass") # car that hits
        intoCar = intoNodePath.getParent().getPythonTag("subclass") # car that gets hit

        # linear speeds for both cars
        fromCar.linearSpeed
        intoCar.linearSpeed
        # mass for both cars
        fromCar.mass
        intoCar.mass
        # heading of both cars
        fromCar.getH()
        intoCar.getH()
        print "--------------------------------------------"
        print fromCar.playerID, " hits ", intoCar.playerID, " into ", intoSide, " from ", fromSide, " at ", impactPoint
        print "--------------------------------------------"

w = World()
run()
