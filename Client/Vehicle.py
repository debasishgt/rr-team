from panda3d.core import Vec3
from panda3d.core import Vec4
from panda3d.core import Point3
from panda3d.core import TransformState
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletDebugNode
from panda3d.bullet import BulletVehicle
from panda3d.bullet import ZUp
import math


class Vehicle(object):
    COUNT = 0

    def __init__(self, bulletWorld, pos,username):
        self.world = bulletWorld
        self.username = username
        self.brakeForce = 100.0
        self.mass = 800.0  # kg
        self.max_speed = 150  # km
        self.armor = 100
        self.health = 100
        self.maxWheelForce = 2000.0  # acceleration
        self.power_ups = [0, 0, 0]

        self.specs = {"mass": self.mass, "maxWheelForce": self.maxWheelForce, "brakeForce": self.brakeForce,
                      "steeringLock": 45.0}
        self.vehicleControlState = {"throttle": 0, "reverse": False, "brake": 0.0, "steering": 0.0}

        # Steering change per second, normalised to steering lock
        # Eg. 45 degrees lock and 1.0 rate means 45 degrees per second
        self.steeringRate = 0.2
        self.centreingRate = 3.0

        self.pos = pos

        self.setupVehicle(bulletWorld)

        COUNT = 1

    def processInput(self, inputState, dt):
        # print self.chassisNP.getPos()
        # print self.chassisNP.getH()
        """Use controls to update the player's car"""
        # For keyboard throttle and brake are either 0 or 1
        if inputState.isSet('forward') and self.vehicle.getCurrentSpeedKmHour() <= self.max_speed:
            # only continues accelerating if player's max speed is not reached
            self.vehicleControlState["throttle"] = 1.0
        else:
            self.vehicleControlState["throttle"] = 0.0

        velocity = self.chassisNode.getLinearVelocity()
        speed = math.sqrt(sum(v ** 2 for v in velocity))
        # Update braking and reversing
        if inputState.isSet('brake'):
            if speed < 0.5 or self.vehicleControlState["reverse"]:
                # If we're stopped, then start reversing
                # Also keep reversing if we already were

                self.vehicleControlState["reverse"] = True
                self.vehicleControlState["throttle"] = 1.0
                self.vehicleControlState["brake"] = 0.0
            else:
                self.vehicleControlState["reverse"] = False
                self.vehicleControlState["brake"] = 1.0
        else:
            self.vehicleControlState["reverse"] = False
            self.vehicleControlState["brake"] = 0.0

        # steering is normalised from -1 to 1, corresponding
        # to the steering lock right and left
        steering = self.vehicleControlState["steering"]
        if inputState.isSet('left'):
            steering += dt * self.steeringRate
            steering = min(steering, 1.0)
        elif inputState.isSet('right'):
            steering -= dt * self.steeringRate
            steering = max(steering, -1.0)
        else:
            # gradually re-center the steering
            if steering > 0.0:
                steering -= dt * self.centreingRate
                if steering < 0.0:
                    steering = 0.0
            elif steering < 0.0:
                steering += dt * self.centreingRate
                if steering > 0.0:
                    steering = 0.0
        self.vehicleControlState["steering"] = steering

        # """Updates acceleration, braking and steering
        # These are all passed in through a controlState dictionary
        # """
        # Update acceleration and braking
        wheelForce = self.vehicleControlState["throttle"] * self.specs["maxWheelForce"]
        self.reversing = self.vehicleControlState["reverse"]
        if self.reversing:
            # Make reversing a bit slower than moving forward
            wheelForce *= -0.5

        brakeForce = self.vehicleControlState["brake"] * self.specs["brakeForce"]

        # Update steering
        # Steering control state is from -1 to 1
        steering = self.vehicleControlState["steering"] * self.specs["steeringLock"]

        # Apply steering to front wheels
        self.vehicle.setSteeringValue(steering, 0)
        self.vehicle.setSteeringValue(steering, 1)
        # Apply engine and brake to rear wheels
        self.vehicle.applyEngineForce(wheelForce, 2)
        self.vehicle.applyEngineForce(wheelForce, 3)
        self.vehicle.setBrake(brakeForce, 2)
        self.vehicle.setBrake(brakeForce, 3)

    def setupVehicle(self, bulletWorld):
        # Chassis
        shape = BulletBoxShape(Vec3(1, 2.2, 0.5))
        ts = TransformState.makePos(Point3(0, 0, .7))
        self.chassisNode = BulletRigidBodyNode('Vehicle')
        self.chassisNP = render.attachNewNode(self.chassisNode)
        self.chassisNP.node().addShape(shape, ts)
        self.chassisNP.node().notifyCollisions(True)
        self.chassisNP.setPosHpr(self.pos[0], self.pos[1], self.pos[2], self.pos[3], self.pos[4], self.pos[5])
        # self.chassisNP.setPos(-5.34744, 114.773, 6)
        # self.chassisNP.setPos(49.2167, 64.7968, 10)
        self.chassisNP.node().setMass(self.mass)
        self.chassisNP.node().setDeactivationEnabled(False)

        bulletWorld.attachRigidBody(self.chassisNP.node())

        # np.node().setCcdSweptSphereRadius(1.0)
        # np.node().setCcdMotionThreshold(1e-7)

        # Vehicle
        self.vehicle = BulletVehicle(bulletWorld, self.chassisNP.node())
        self.vehicle.setCoordinateSystem(ZUp)
        bulletWorld.attachVehicle(self.vehicle)

        self.carNP = loader.loadModel('models/batmobile-chassis.egg')
        # self.yugoNP.setScale(.7)
        self.carNP.reparentTo(self.chassisNP)

        # Right front wheel
        np = loader.loadModel('models/batmobile-wheel-right.egg')
        np.reparentTo(render)
        self.addWheel(Point3(1, 1.1, .7), True, np)

        # Left front wheel
        np = loader.loadModel('models/batmobile-wheel-left.egg')
        np.reparentTo(render)
        self.addWheel(Point3(-1, 1.1, .7), True, np)

        # Right rear wheel
        np = loader.loadModel('models/batmobile-wheel-right.egg')
        np.reparentTo(render)
        self.addWheel(Point3(1, -2, .7), False, np)

        # Left rear wheel
        np = loader.loadModel('models/batmobile-wheel-left.egg')
        np.reparentTo(render)
        self.addWheel(Point3(-1, -2, .7), False, np)

    def addWheel(self, pos, front, np):
        wheel = self.vehicle.createWheel()

        wheel.setNode(np.node())
        wheel.setChassisConnectionPointCs(pos)
        wheel.setFrontWheel(front)

        wheel.setWheelDirectionCs(Vec3(0, 0, -1))
        wheel.setWheelAxleCs(Vec3(1, 0, 0))
        wheel.setWheelRadius(0.33)
        wheel.setMaxSuspensionTravelCm(40.0)

        wheel.setSuspensionStiffness(40.0)
        wheel.setWheelsDampingRelaxation(2.3)
        wheel.setWheelsDampingCompression(4.4)
        wheel.setFrictionSlip(100.0)
        wheel.setRollInfluence(0.1)

    def reset(self):
        self.chassisNP.setP(0)
        self.chassisNP.setR(0)
