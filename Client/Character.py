# Roaming-Ralph was modified to remove collision part.

import direct.directbase.DirectStart
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from panda3d.core import Point3, Plane
from panda3d.core import CollisionTraverser, CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerQueue, CollisionRay, CollisionHandlerPusher, CollisionPlane
from direct.interval.IntervalGlobal import Sequence
from direct.task import Task
import time


class Character:
    playerId = 1
    type = 0

    def __init__(self, tempworld, type):
        self.world = tempworld
        self.speed = 0
        self.acceleration = 1.5
        self.brakes = .7
        self.min_speed = 0
        self.max_speed = 200
        self.reverse_speed = 20
        self.reverse_limit = -40
        self.armor = 100
        self.health = 100
        self.a_timer_start = time.time()
        self.a_timer_end = time.time()

        if type == 0:
            self.actor = Actor("models/ralph",
                               {"run": "models/ralph-run",
                                "walk": "models/ralph-walk"})
        elif type == 1:
            self.actor = Actor("models/panda-model",
                               {"walk": "models/panda-walk4"})
        elif type == 2:
            self.actor = loader.loadModel("knucklehead.egg")
            self.tex = loader.loadTexture("knucklehead.jpg")
            self.actor.setTexture(self.car_tex, 1)

        self.actor.reparentTo(render)
        self.actor.setScale(.2)
        self.actor.setPos(50 * random.random(), 50 * random.random(), 0)

        # Create a collsion node for this object.
        self.cNode = CollisionNode('char')
        # Attach a collision sphere solid to the collision node.
        self.cNode.addSolid(CollisionSphere(0, 0, 3, 3))
        # Attach the collision node to the object's model.
        self.smileyC = self.actor.attachNewNode(self.cNode)
        # self.frowneyC.show()
        # base.cTrav.addCollider(self.smileyC, self.world.pusher)
        # self.world.pusher.addCollider(self.smileyC, self.actor, base.drive.node())

    def getActor(self):
        return self.actor

    def get_speed(self):
        return self.speed

    def accelerate(self):
        # check how long you were accelerating
        time_elapsed = time.time() - self.a_timer_end
        if time_elapsed > 1:  # in seconds last accelerated
            self.a_timer_start = time.time()

        if self.speed < self.max_speed:
            self.speed += self.acceleration * (time.time() - self.a_timer_start)
            print(time_elapsed)
        else:
            self.speed = self.max_speed
        # reset timer
        self.a_timer_end = time.time()

    def friction(self, friction):
        if self.speed > 0:
            self.speed -= friction
        else:
            self.speed = 0

    def brake(self):
        if self.speed > self.min_speed:
            self.speed -= self.brakes
            # reset acceleration timer
            self.a_timer_start = time.time()

    def reverse(self):
        if self.speed > self.reverse_limit:
            self.speed -= self.reverse_speed
