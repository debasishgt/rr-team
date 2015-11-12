__author__ = 'dthakurta'

import math


class CollisionResolver:
    def __init__(self):
        print "Resolver Init"
        self.rearResultAngle = 0
        self.fromAngle = 0
        self.toAngle = 0
        self.fromMagnitude = 0
        self.fromMagnitude = 0
        self.fromX = 0
        self.fromY = 0
        self.toX = 0
        self.toY = 0
        self.resultX = 0
        self.resultY = 0
        self.resultAngle = 0
        self.fromResultlinearSpeed = 0
        self.toResultlinearSpeed = 0

    def resolve(self, fromActor, toActor, isRearEnd=False):
        self.fromAngle = math.degrees(math.atan(fromActor.getY()/fromActor.getX()))
        self.toAngle = math.degrees(math.atan(toActor.getY()/toActor.getX()))
        if isRearEnd:
            self.toAngle += 180
            self.toAngle %= 360

        self.fromMagnitude = fromActor.mass * fromActor.linearSpeed
        self.toMagnitude = toActor.mass * toActor.linearSpeed

        self.fromX = self.fromMagnitude * math.cos(self.fromAngle)
        self.fromY = self.fromMagnitude * math.sin(self.fromAngle)

        self.toX = self.toMagnitude * math.cos(self.toAngle)
        self.toY = self.toMagnitude * math.sin(self.toAngle)

        self.resultX = self.fromX + self.toX
        self.resultY = self.fromY + self.toY

        self.resultAngle = math.degrees(math.atan(self.resultY/self.resultX))

        if self.resultAngle < 0:
            self.resultAngle += 360

        self.resultAngle %= 360
        print "Result angle: ", self.resultAngle

        self.fromResultlinearSpeed = (fromActor.mass * fromActor.linearSpeed) / (fromActor.mass + toActor.mass)
        print "From linearSpeed: ", self.fromResultlinearSpeed
        self.toResultlinearSpeed = (toActor.mass * toActor.linearSpeed) / (fromActor.mass + toActor.mass)
        print "To linearSpeed: ", self.toResultlinearSpeed

        fromCarNewAngle = self.resultAngle
        intoCarNewAngle = self.resultAngle
        if isRearEnd:
            self.resultAngle += 180
            self.resultAngle %= 360
            intoCarNewAngle = self.resultAngle
            print "To Car angle: ", self.rearResultAngle

        fromActor.setH(fromCarNewAngle)
        toActor.setH(intoCarNewAngle)
        fromActor.linearSpeed = self.fromResultlinearSpeed
        toActor.linearSpeed = self.toResultlinearSpeed
