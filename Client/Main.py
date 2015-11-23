# Roaming-Ralph was modified to remove collision part.

# import direct.directbase.DirectStart
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
import random, sys, os, math
from panda3d.core import Point3, Plane
from panda3d.core import CollisionTraverser, CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerQueue, CollisionRay, CollisionHandlerPusher, CollisionPlane
from direct.interval.IntervalGlobal import Sequence
from direct.task import Task
from Character import Character
from panda3d.core import NodePath
from panda3d.bullet import BulletVehicle
from panda3d.bullet import BulletWorld, BulletTriangleMesh, BulletTriangleMeshShape, BulletDebugNode, BulletPlaneShape, \
    BulletRigidBodyNode

from Track import Track
from Vehicle import Vehicle
from Camera import Camera
from SkyDome import SkyDome
# afrom Chat import Chat
import time

""" Custom Imports """
# import your modules
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager
from Dashboard import *

SPEED = 0.5


# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale=.05)


# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1),
                        pos=(1.3, -0.95), align=TextNode.ARight, scale=.07)


class World(DirectObject):
    gameStateDict = {"Login" : 0,"CreateLobby":4, "EnterGame": 1, "BeginGame": 2, "InitializeGame"}
    gameState = -1
    # Login , EnterGame , BeginGame
    responseValue = -1
    currentTime = 0
    idleTime = 0
    mySequence = None
    pandaPace = None
    jumpState = False
    isWalk = False
    previousPos = None  # used to store the mainChar pos from one frame to another
    host = ""
    port = 0
    characters = []  # Stores the list of all the others players characters

    def __init__(self):

        base.setFrameRateMeter(True)
        #input states
        inputState.watchWithModifiers('forward', 'w')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('brake', 's')
        inputState.watchWithModifiers('right', 'd')
        inputState.watchWithModifiers('turnLeft', 'q')
        inputState.watchWithModifiers('turnRight', 'e')

        self.keyMap = {"hello": 0, "left": 0, "right": 0, "forward": 0, "backward": 0, "cam-left": 0, "cam-right": 0,
                       "chat0": 0, "pow1": 0, "pow2": 0, "pow3": 0, "reset": 0}
        base.win.setClearColor(Vec4(0, 0, 0, 1))

        # Network Setup
        self.cManager = ConnectionManager(self)
        self.startConnection()
        # chat box
        # self.chatbox = Chat(self.cManager, self)

        # taskMgr.add(self.message, 'message')



        # Post the instructions

        # self.title = addTitle("Panda3D Tutorial: Roaming Ralph (Walking on the Moon)")
        # self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        # self.inst2 = addInstructions(0.90, "[A]: Rotate Ralph Left")
        # self.inst3 = addInstructions(0.85, "[D]: Rotate Ralph Right")
        # self.inst4 = addInstructions(0.80, "[W]: Run Ralph Forward")
        # self.inst4 = addInstructions(0.75, "[S]: Run Ralph Backward")
        # self.inst6 = addInstructions(0.70, "[Left Arrow]: Rotate Camera Left")
        # self.inst7 = addInstructions(0.65, "[Right Arrow]: Rotate Camera Right")
        # self.inst8 = addInstructions(0.60, "[L]: List Connected Users")
        # self.inst9 = addInstructions(0.55, "[0]: Toggle Chat Broadcast")
        # self.inst10 = addInstructions(0.50, "[1]: Toggle Private Chat")

        # Set up the environment
        #
        self.initializeBulletWorld(False)

        #self.createEnvironment()
        Track(self.bulletWorld)

        # Collision Code
        # Initialize the collision traverser.
        # base.cTrav = CollisionTraverser()
        # Initialize the Pusher collision handler.
        # self.pusher = CollisionHandlerPusher()

        # Create the main character, Ralph

        self.mainCharRef = Vehicle(self.bulletWorld, (0, 25, 16, 0, 0, 0))
        #self.mainCharRef = Character(self, self.bulletWorld, 0, "Me")
        self.mainChar = self.mainCharRef.chassisNP
        #self.mainChar.setPos(0, 25, 16)

        self.TestChar = Character(self, self.bulletWorld, 0, "test")
        self.TestChar.actor.setPos(0, 0, 0)

        #         self.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, [self.mainCharRef.type,
        #                                                                     self.mainChar.getX(),
        #                                                                     self.mainChar.getY(),
        #                                                                     self.mainChar.getZ()])

        self.previousPos = self.mainChar.getPos()
        taskMgr.doMethodLater(.1, self.updateMove, 'updateMove')

        # Set Dashboard
        self.dashboard = Dashboard(self.mainCharRef, taskMgr)

        # Creating Pandas
        # self.pandas = []
        # self.pandacount = 2
        # for x in range(self.pandacount):
        #     self.pandas.append(MyPanda(self))

        # Creating Stationary spheres
        # self.spheres = []
        # self.sphereCount = 3
        # for x in range(self.sphereCount):
        #     self.spheres.append(StationarySphere(self))

        # Create Car
        # self.car = MyCar(self)

        # Panda animation
        # for panda in self.pandas:
        #     taskMgr.add(panda.jumpPanda, "jumpPanda")
        #     taskMgr.add(panda.timerTask, 'timerTask')
        #     taskMgr.add(panda.pandaWalk, 'pandaWalk')
        #     taskMgr.add(panda.pandaStop, 'pandaStop')
        #
        # taskMgr.add(self.car.makeCircle, "makeCircle")
        #
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # floorNode = render.attachNewNode("Floor NodePath")

        # Create a collision plane solid.
        # collPlane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, 0)))
        # Call our function that creates a nodepath with a collision node.
        # floorCollisionNP = self.makeCollisionNodePath(floorNode, collPlane)

        # Accept the control keys for movement and rotation
        self.accept("escape", self.doExit)
        self.accept("a", self.setKey, ["left", 1])
        self.accept("d", self.setKey, ["right", 1])
        self.accept("w", self.setKey, ["forward", 1])
        self.accept("s", self.setKey, ["backward", 1])
        self.accept("arrow_left", self.setKey, ["cam-left", 1])
        self.accept("arrow_right", self.setKey, ["cam-right", 1])
        self.accept("a-up", self.setKey, ["left", 0])
        self.accept("d-up", self.setKey, ["right", 0])
        self.accept("w-up", self.setKey, ["forward", 0])
        self.accept("s-up", self.setKey, ["backward", 0])
        self.accept("arrow_left-up", self.setKey, ["cam-left", 0])
        self.accept("arrow_right-up", self.setKey, ["cam-right", 0])
        self.accept("h", self.setKey, ["hello", 1])
        self.accept("h-up", self.setKey, ["hello", 0])
        self.accept("0", self.setKey, ["chat0", 1])
        self.accept("0-up", self.setKey, ["chat0", 0])
        self.accept("1", self.use_powerup1)
        self.accept("2", self.use_powerup2)
        self.accept("3", self.use_powerup3)
        self.accept("r", self.doReset)

        taskMgr.add(self.move, "moveTask")

        # Game state variables
        self.isMoving = False

        # Sky Dome
        self.sky = SkyDome()

        # Set up the camera
        self.camera = Camera(self.mainChar)
        #base.disableMouse()
        #base.camera.setPos(self.mainChar.getX(), self.mainChar.getY() + 10, self.mainChar.getZ() + 2)

        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        directionalLight2 = DirectionalLight("directionalLight2")
        directionalLight2.setDirection(Vec3(5, 5, -5))
        directionalLight2.setColor(Vec4(1, 1, 1, 1))
        directionalLight2.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(directionalLight2))

        # Game initialisation
        self.gameState = self.gameStateDict["Login"]
        self.responseValue = -1

             #self.ConnectionManager.sendRequest(Constants.CMSG_LOGIN,"test1","1234")
             #taskMgr.add(self.enterGame,"EnterGame")

    def use_powerup1(self):
        self.use_powerup(1)

    def use_powerup2(self):
        self.use_powerup(2)

    def use_powerup3(self):
        self.use_powerup(3)

    def use_powerup(self, num):
        if self.mainCharRef.power_ups[num - 1] == 0:
            print "power-up slot empty"
        else:
            print "power-up", num, "used"

    def doExit(self):
        self.cleanup()
        sys.exit(1)

    def cleanup(self):
#         self.cManager.sendRequest(Constants.CMSG_DISCONNECT)
        self.cManager.closeConnection()
        self.world = None
        self.outsideWorldRender.removeNode()

    def doReset(self):
        self.mainCharRef.reset()

    def enterGame(self, task):
        if self.gameState == self.gameStateDict["Login"]:
            #responseValue = 1 indicates that this state has been finished
            if self.responseValue == 1:
                # Authentication succeeded
                self.cManager.sendRequest(Constants.CMSG_CREATE_LOBBY, ["game1",0])
                self.gameState = self.gameStateDict["CreateLobby"]
                self.responseValue = -1
        elif self.gameState == self.gameStateDict["CreateLobby"]:
            if self.responseValue == 1:
                # Lobby Created
                #Let's join it
                self.cManager.sendRequest(Constants.CMSG_ENTER_GAME_NAME, "game1")
                self.gameState = self.gameStateDict["EnterGame"]
                self.responseValue = -1
        elif self.gameState == self.gameStateDict["EnterGame"]:
            if self.responseValue == 1:
#               Everyone is in the game, we send ReqReady, and the server will send positions when every client did
                self.cManager.sendRequest(Constants.CMSG_READY)
#                 When the positions are sent, an acknowledgment is sent and we begin the InitializeGame
                self.responseValue = -1

        elif self.gameState == self.gameStateDict["InitializeGame"]:
            if self.responseValue == 1:
                # Set up the camera
                self.camera = Camera(self.mainChar)

                self.cManager.sendRequest(Constants.CMSG_READY)
                self.responseValue = -1

        elif self.gameState == self.gameStateDict["BeginGame"]:
            if self.responseValue == 1:

                taskMgr.add(self.move, "moveTask")
                return task.done

        return task.cont

    def createEnvironment(self):
        self.environ = loader.loadModel("models/square")
        self.environ.reparentTo(render)
        self.environ.setPos(0, 0, 0)
        self.environ.setScale(500, 500, 1)
        self.moon_tex = loader.loadTexture("models/moon_1k_tex.jpg")
        self.environ.setTexture(self.moon_tex, 1)

        shape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        node = BulletRigidBodyNode('Ground')
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(0, 0, 0)

        self.bulletWorld.attachRigidBody(node)

        self.visNP = loader.loadModel('models/track.egg')
        self.tex = loader.loadTexture("models/tex/Main.png")
        self.visNP.setTexture(self.tex)

        geom = self.visNP.findAllMatches('**/+GeomNode').getPath(0).node().getGeom(0)
        mesh = BulletTriangleMesh()
        mesh.addGeom(geom)
        trackShape = BulletTriangleMeshShape(mesh, dynamic=False)

        body = BulletRigidBodyNode('Bowl')
        self.visNP.node().getChild(0).addChild(body)
        bodyNP = render.anyPath(body)
        bodyNP.node().addShape(trackShape)
        bodyNP.node().setMass(0.0)
        bodyNP.setTexture(self.tex)

        self.bulletWorld.attachRigidBody(bodyNP.node())

        self.visNP.reparentTo(render)

        self.bowlNP = bodyNP
        self.visNP.setScale(70)

    def initializeBulletWorld(self, debug=False):
        self.outsideWorldRender = render.attachNewNode('world')

        self.bulletWorld = BulletWorld()
        self.bulletWorld.setGravity(Vec3(0, 0, -9.81))
        if debug:
            self.debugNP = self.outsideWorldRender.attachNewNode(BulletDebugNode('Debug'))
            self.debugNP.show()
            self.debugNP.node().showWireframe(True)
            self.debugNP.node().showConstraints(True)
            self.debugNP.node().showBoundingBoxes(True)
            self.debugNP.node().showNormals(False)
            self.bulletWorld.setDebugNode(self.debugNP.node())

    def makeCollisionNodePath(self, nodepath, solid):
        '''
        Creates a collision node and attaches the collision solid to the
        supplied NodePath. Returns the nodepath of the collision node.
        '''
        # Creates a collision node named after the name of the NodePath.
        collNode = CollisionNode("%s c_node" % nodepath.getName())
        collNode.addSolid(solid)
        collisionNodepath = nodepath.attachNewNode(collNode)

        return collisionNodepath

    # Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def getDist(self):
        mainCharX = self.mainChar.getPos().x
        mainCharY = self.mainChar.getPos().y
        pandaX = self.pandaActor2.getPos().x
        pandaY = self.pandaActor2.getPos().y
        dist = math.sqrt(abs(mainCharX - pandaX) ** 2 + abs(mainCharY - pandaY) ** 2)
        return dist

    def move(self, task):
        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.

        #dt = globalClock.getDt()

        #update camera
        self.camera.update(self.mainChar)

        #base.camera.lookAt(self.mainChar)
        #if (self.keyMap["cam-left"] != 0):
        #    base.camera.setX(base.camera, -20 * dt)
        #if (self.keyMap["cam-right"] != 0):
        #    base.camera.setX(base.camera, +20 * dt)

        # save mainChar's initial position so that we can restore it,
        # in case he falls off the map or runs into something.
        #
        #startpos = self.mainChar.getPos()
        #
        # If a move-key is pressed, move ralph in the specified direction.
        # If a move-key is pressed, move ralph in the specified direction.
        # Steering info
        #steering = 0.0  # degree
        #steeringClamp = 70.0  # degree
        #steeringIncrement = 180.0  # degree per second
        #
        # Process input
        #engineForce = 0.0
        #brakeForce = 0.0
        #if (self.keyMap["forward"] != 0):
        #    # checks for vehicle's max speed
        #    if self.mainCharRef.vehicle.getCurrentSpeedKmHour() <= self.mainCharRef.max_speed:
        #        engineForce = 2000.0
        #        brakeForce = 0.0
        #
        #if (self.keyMap["backward"] != 0):
        #    if self.mainCharRef.vehicle.getCurrentSpeedKmHour() <= 0:
        #        engineForce = -500.0
        #        brakeForce = 0.0
        #    else:
        #        engineForce = 0.0
        #        brakeForce = 100.0
        #
        #if (self.keyMap["left"] != 0):
        #    steering += dt * steeringIncrement
        #    steering = min(steering, steeringClamp)
        #
        #if (self.keyMap["right"] != 0):
        #    steering -= dt * steeringIncrement
        #    steering = max(steering, -steeringClamp)
        #
        # Apply steering to front wheels
        #self.mainCharRef.vehicle.setSteeringValue(steering, 0)
        #self.mainCharRef.vehicle.setSteeringValue(steering, 1)
        #
        # Apply engine and brake to rear wheels
        #self.mainCharRef.vehicle.applyEngineForce(engineForce, 2)
        #self.mainCharRef.vehicle.applyEngineForce(engineForce, 3)
        #self.mainCharRef.vehicle.setBrake(brakeForce, 2)
        #self.mainCharRef.vehicle.setBrake(brakeForce, 3)

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.
        #if (self.keyMap["forward"] != 0) or (self.keyMap["backward"] != 0) or (self.keyMap["left"] != 0) or (
        #            self.keyMap["right"] != 0):
        #    if self.isMoving is False:
        #        self.mainCharRef.run()
        #        self.isMoving = True
        #
        #else:
        #    if self.isMoving:
        #        self.mainCharRef.walk()
        #        self.isMoving = False

        dt = globalClock.getDt()

        self.mainCharRef.processInput(inputState, dt)
        self.bulletWorld.doPhysics(dt, 10, 0.02)

        # use power-ups
        if self.keyMap["pow1"] != 0:
            print "power up 1 activated"
        if self.keyMap["pow2"] != 0:
            print "power up 2 activated"
        if self.keyMap["pow3"] != 0:
            print "power up 3 activated"

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        #camvec = self.mainChar.getPos() - base.camera.getPos()
        #camvec.setZ(0)
        #camdist = camvec.length()
        #camvec.normalize()
        #if (camdist > 10.0):
        #    base.camera.setPos(base.camera.getPos() + camvec * (camdist - 10))
        #    camdist = 10.0
        #if (camdist < 5.0):
        #    base.camera.setPos(base.camera.getPos() - camvec * (5 - camdist))
        #    camdist = 5.0

        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.

        #self.floater.setPos(self.mainChar.getPos())
        #self.floater.setZ(self.mainChar.getZ() + 2.0)
        #base.camera.lookAt(self.floater)

        self.bulletWorld.doPhysics(dt)

        return task.cont

    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True

    # Chat
    # def message(self, task):
    #     # hide all chatboxes
    #     if self.keyMap["chat0"] != 0:
    #         if self.chatbox.getVisible() is False:
    #             self.chatbox.setVisible(True)
    #             self.chatbox.show(0)
    #         else:
    #             self.chatbox.setVisible(False)
    #             self.chatbox.hide()
    #         self.keyMap["chat0"] = 0
    #     if self.keyMap["chat1"] != 0:
    #         if self.chatbox.getVisible() is False:
    #             self.chatbox.setVisible(True)
    #             self.chatbox.show(1)
    #         else:
    #             self.chatbox.setVisible(False)
    #             self.chatbox.hide()
    #         self.keyMap["chat1"] = 0
    #     elif self.keyMap["chat2"] != 0:
    #         if self.chatbox.getVisible() is False:
    #             self.chatbox.setVisible(True)
    #             self.chatbox.show(2)
    #         else:
    #             self.chatbox.setVisible(False)
    #             self.chatbox.hide()
    #         self.keyMap["chat2"] = 0
    #     elif self.keyMap["chat3"] != 0:
    #         if self.chatbox.getVisible() is False:
    #             self.chatbox.setVisible(True)
    #             self.chatbox.show(3)
    #         else:
    #             self.chatbox.setVisible(False)
    #             self.chatbox.hide()
    #         self.keyMap["chat3"] = 0
    #     elif self.keyMap["chat4"] != 0:
    #         if self.chatbox.getVisible() is False:
    #             self.chatbox.setVisible(True)
    #             self.chatbox.show(4)
    #         else:
    #             self.chatbox.setVisible(False)
    #             self.chatbox.hide()
    #         self.keyMap["chat4"] = 0
    #     elif self.keyMap["chat5"] != 0:
    #         if self.chatbox.getVisible() is False:
    #             self.chatbox.setVisible(True)
    #             self.chatbox.show(5)
    #         else:
    #             self.chatbox.setVisible(False)
    #             self.chatbox.hide()
    #         self.keyMap["chat5"] = 0
    #     return task.cont

    def updateMove(self, task):
        if self.isMoving == True:
            moving = self.mainChar.getPos() - self.previousPos

            self.cManager.sendRequest(Constants.CMSG_MOVE,
                                      [moving.getX(), moving.getY(), moving.getZ(), self.mainCharRef.actor.getH(),
                                       self.mainCharRef.actor.getP(),
                                       self.mainCharRef.actor.getR(), " "])


            # self.cManager.sendRequest(Constants.RAND_FLOAT, 1.0)
            self.previousPos = self.mainChar.getPos()

        return task.again


w = World()
run()
