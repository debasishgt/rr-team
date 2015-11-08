__author__ = 'ASPIRE'


class StationarySphere():
    count = 0

    def __init__(self, tempworld):
        self.world = tempworld
        StationarySphere.count += 1
        self.sizescale = 0.6  # Planet size scale
        if StationarySphere.count == 1:
            # Load the Sun
            self.world.sun = loader.loadModel("models/planet_sphere")
            self.sun_tex = loader.loadTexture("models/sun_1k_tex.jpg")
            self.world.sun.setTexture(self.sun_tex, 1)
            self.world.sun.reparentTo(render)
            self.world.sun.setScale(2 * self.sizescale)
            xDim, yDim, zDim = self.getDimensions(self.world.sun)
            self.world.sun.setPos(-25, -25, zDim / 2.0)
            self.actor = self.world.sun
            self.boundingRadius = zDim
        elif StationarySphere.count == 2:
            # Load Venus
            self.world.venus = loader.loadModel("models/planet_sphere")
            self.venus_tex = loader.loadTexture("models/venus_1k_tex.jpg")
            self.world.venus.setTexture(self.venus_tex, 1)
            self.world.venus.reparentTo(render)
            self.world.venus.setScale(0.923 * self.sizescale)
            xDim, yDim, zDim = self.getDimensions(self.world.venus)
            self.world.venus.setPos(-20, 20, zDim / 2.0)
            self.boundingRadius = zDim
        elif StationarySphere.count == 3:
            # Load Earth
            self.world.earth = loader.loadModel("models/planet_sphere")
            self.earth_tex = loader.loadTexture("models/earth_1k_tex.jpg")
            self.world.earth.setTexture(self.earth_tex, 1)
            self.world.earth.reparentTo(render)
            self.world.earth.setScale(self.sizescale)
            xDim, yDim, zDim = self.getDimensions(self.world.earth)
            self.world.earth.setPos(20, 20, zDim / 2.0)
            self.boundingRadius = zDim

    def getDimensions(self, nPath):
        pt1, pt2 = nPath.getTightBounds()
        xDim = pt2.getX() - pt1.getX()
        yDim = pt2.getY() - pt1.getY()
        zDim = pt2.getZ() - pt1.getZ()
        return [xDim, yDim, zDim]


        # --------------------- StationarySphere Class END-------------------------------#
