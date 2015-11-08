# Roaming-Ralph was modified to remove collision part.

import direct.directbase.DirectStart
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from panda3d.core import Point3, Plane
from panda3d.core import CollisionTraverser,CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerQueue,CollisionRay, CollisionHandlerPusher, CollisionPlane
from direct.interval.IntervalGlobal import Sequence
from direct.task import Task
import time

class Character:
    playerId = 1
    type = 0
    def __init__(self, tempworld, type):
        self.world = tempworld

        if type == 0:
          self.actor = Actor("models/ralph",
                         {"run":"models/ralph-run",
                          "walk":"models/ralph-walk"})
        elif type ==1 :
          self.actor=Actor("models/panda-model",
                     {"walk": "models/panda-walk4"})
        elif type == 2:
          self.actor = loader.loadModel("knucklehead.egg")
          self.tex = loader.loadTexture("knucklehead.jpg")
          self.actor.setTexture(self.car_tex, 1)

        self.actor.reparentTo(render)
        self.actor.setScale(.2)
        self.actor.setPos(50*random.random(), 50*random.random(), 0)

        # Create a collsion node for this object.
        self.cNode = CollisionNode('char')
        # Attach a collision sphere solid to the collision node.
        self.cNode.addSolid(CollisionSphere(0, 0, 3, 3))
        # Attach the collision node to the object's model.
        self.smileyC = self.actor.attachNewNode(self.cNode)
        #self.frowneyC.show()
        #base.cTrav.addCollider(self.smileyC, self.world.pusher)
        #self.world.pusher.addCollider(self.smileyC, self.actor, base.drive.node())

    def getActor(self):
        return self.actor
