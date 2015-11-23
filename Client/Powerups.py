__author__ = 'dthakurta'

from direct.task import Task
from common.Constants import Constants
from panda3d.core import Vec3
import time, threading
import math
import copy


class PowerupTypes:
    def __init__(self):
        self.list = {1: {"name": "SHIELD", "rating": 20, "time": 5},
                     2: {"name": "BOOST", "rating": 20, "time": 5},
                     3: {"name": "INVINCIBLE", "rating": 0, "time": 5},
                     4: {"name": "HEALTH", "rating": 0, "time": 5}}


class PowerupPositions:
    def __init__(self):
        self.positions = {
                1: {"id": 1, "x": 0, "y": 25, "z": 8},
                2: {"id": 2, "x": 20, "y": 20, "z": 0},
                3: {"id": 3, "x": 30, "y": 30, "z": 0},
                4: {"id": 4, "x": 40, "y": 40, "z": 0},
                5: {"id": 5, "x": 50, "y": 50, "z": 0},
                6: {"id": 6, "x": 60, "y": 60, "z": 0},
                7: {"id": 6, "x": 70, "y": 70, "z": 0},
                8: {"id": 6, "x": 80, "y": 80, "z": 0}
            }

class PowerupIcon:
    def __init__(self, powerupInfo):
        self.id = powerupInfo['id']
        self.posX = powerupInfo['x']
        self.posY = powerupInfo['y']
        self.posZ = powerupInfo['z']
        self.powerName = powerupInfo['item']['name']
        self.powerRating = powerupInfo['item']['rating']
        self.powerTime = powerupInfo['item']['time']
        self.player = None
        
        self.itemIcon = loader.loadModel("models/speedpowerup.egg")

        if self.powerName == "SHIELD":
            self.shield_tex = loader.loadTexture("models/power_ups/shieldtext.png")
            self.itemIcon.setTexture(self.shield_tex, 1)
        elif self.powerName == "BOOST":
            self.boost_tex = loader.loadTexture("models/power_ups/speedtext.png")
            self.itemIcon.setTexture(self.boost_tex, 1)
        elif self.powerName == "INVINCIBLE":
            self.invincible_tex = loader.loadTexture("models/power_ups/invinstext.png")
            self.itemIcon.setTexture(self.invincible_tex, 1)
        elif self.powerName == "HEALTH":
            self.health_tex = loader.loadTexture("models/power_ups/healthtext.png")
            self.itemIcon.setTexture(self.health_tex, 1)

        self.itemIcon.reparentTo(render)
        self.itemIcon.setPos(self.posX, self.posY, self.posZ)
        
        self.rotate()

    def removeFromField(self):
        # move the powerup under the map
        self.itemIcon.setPos(self.posX, self.posY, self.posZ - 6)
    
    def returnToField(self):
        self.itemIcon.setPos(self.posX, self.posY, self.posZ)
        
    def rotate(self):
        self.spinPowerUp = self.itemIcon.hprInterval(1, Vec3(360, 0, 0))
        self.spinPowerUp.loop()

class ShieldPowerup(PowerupIcon):
    def __init__(self, powerupInfo):
        PowerupIcon.__init__(self, powerupInfo)
        self.pickable = False
        
    def useAbility(self):
        print "ShieldPowerup"
        #print "armor: ", self.player.armor
        #self.player.armor += 15
        #if self.player.armor > self.player.maxArmor:
        #    self.player.armor = self.player.maxArmor
        #print "armor ", self.player.armor      
    
class HealthPowerup(PowerupIcon):
    def __init__(self, powerupInfo):
        PowerupIcon.__init__(self, powerupInfo)
        self.pickable = False
        
    def useAbility(self):
        print "HealthPowerup"
        #print "Health: ", self.player.health
        #self.player.health += 15
        #if self.player.health > self.player.maxHealth:
        #    self.player.health = self.player.maxHealth
        #print "health ", self.player.health      
             

class BoostPowerup(PowerupIcon):
    def __init__(self, powerupInfo):
        PowerupIcon.__init__(self, powerupInfo)
        self.pickable = True
        
    def useAbility(self):
        print "BoostPowerup"
        #self.player.speed += 200
        #print "used boost"

class InvinciblePowerup(PowerupIcon):
    def __init__(self, powerupInfo):
        PowerupIcon.__init__(self, powerupInfo)
        self.pickable = True
        
    def useAbility(self):
        print "Invincible Powerup"
    
class PowerupManager:
    #Max number of each powerup
    MAX_COUNT = 2
    POWERUP_RESET_TIME = 10

    def __init__(self, cManager, actors=None):
        self.actors = actors
        self.takenPowers = {}
        self.activePowers = {}
        self.cManager = cManager

        powerupTypes = PowerupTypes()
        powerupPositions = PowerupPositions()
        for pwrKey, pwrVal in powerupTypes.list.iteritems():
            for x in range(PowerupManager.MAX_COUNT):
                #print key, val["id"], val["rating"], val["time"]
                posKey, posValue = powerupPositions.positions.popitem()
                posValue["item"] = pwrVal
                #newPowerup = PowerupIcon(posValue)
                newPowerup = self.createPowerup(posValue)
                #print key, value
                self.activePowers[posKey] = newPowerup
                #print self.freeSlots
    
    def createPowerup(self, powerupInfo):
        if (powerupInfo['item']['name'] == "SHIELD"):
            return ShieldPowerup(powerupInfo)
        elif(powerupInfo['item']['name'] == "BOOST"):
            return BoostPowerup(powerupInfo)
        elif(powerupInfo['item']['name'] == "INVINCIBLE"):
            return InvinciblePowerup(powerupInfo)
        elif(powerupInfo['item']['name'] == "HEALTH"):
            return HealthPowerup(powerupInfo)
    
    def setActors(self, actors):
        self.actors = actors

    def checkPowerPickup(self, task):
        for actor in self.actors:
            actorRef = actor.chassisNP
            powerObtain = self.powerPickup(actor, actorRef.getPos(), 5.0)#actor.actorRadius)
            
            if powerObtain is not None:
                powerObtain.player = actor
                actor.pickedPowerup(powerObtain)
        return task.cont

    def powerPickup(self, actor, actorPos, actorRadius):
        powerObtained = None
        for key, powerUp in self.activePowers.iteritems():
            if (math.pow((actorPos.x - powerUp.posX), 2) + math.pow((actorPos.y - powerUp.posY), 2) + math.pow((actorPos.z - powerUp.posZ), 2) <= math.pow(actorRadius, 2)
                and actor.canPickUpPowerup()):

                self.cManager.sendRequest(Constants.SMSG_POWER_UP_PICK_UP, powerUp.id)
                
                powerObtained = copy.deepcopy(powerUp)
                print "obtain Power"
                self.resetPowerupsTask(key)
                break

        return powerObtained

    def resetPowerupsTask(self, powerupId):
        processThread = threading.Thread(target=self.resetPowerup, args=(powerupId,))
        #Remove powerup from available list and add to taken list
        self.takenPowers[powerupId] = self.activePowers.get(powerupId)
        self.takenPowers[powerupId].removeFromField()
        self.activePowers.pop(powerupId, 0)
        #print self.activePowers
        #dprint self.takenPowers
        #Start thread to reset powerup spawn
        processThread.start()

    def resetPowerup(self, powerupId):
        time.sleep(PowerupManager.POWERUP_RESET_TIME)
        #print self.takenPowers.get(powerupId)
        self.activePowers[powerupId] = self.takenPowers.get(powerupId)
        self.activePowers[powerupId].returnToField()
        self.takenPowers.pop(powerupId, 0)
        print self.activePowers
        print self.takenPowers   
