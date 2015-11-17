__author__ = 'ASPIRE'

class Player:
    count = 0

    def __init__(self, tempworld):
        self.world = tempworld

        self.actor = Actor("models/ralph",
                           {"run": "models/ralph-run",
                            "walk": "models/ralph-walk"})
        self.actor.reparentTo(render)
        self.actor.setScale(.2)
        self.actor.setPos(30, 30, 0)

        # Create a collsion node for this object.
        self.cNode = CollisionNode('ralph')
        # Attach a collision sphere solid to the collision node.
        self.cNode.addSolid(CollisionSphere(0, 0, 3, 3))
        # Attach the collision node to the object's model.
        self.smileyC = self.actor.attachNewNode(self.cNode)
        # self.frowneyC.show()
        base.cTrav.addCollider(self.smileyC, self.world.pusher)
        self.world.pusher.addCollider(self.smileyC, self.actor, base.drive.node())

    def getActor(self):
        return self.actor