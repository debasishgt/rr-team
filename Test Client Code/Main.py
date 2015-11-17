import __builtin__

""" Python Imports """
from hashlib import md5
from sys import exit
from time import strftime
import random, sys

""" Panda3D Imports """
from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject

from panda3d.core import Texture
from panda3d.core import WindowProperties

""" Custom Imports """
# import your modules
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager

class Main(DirectObject):

    def __init__(self):
        
	    # Network Setup
        self.cManager = ConnectionManager()
        self.startConnection()
        
        taskMgr.add(self.menu, "Menu")

    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True
    
    def menu(self, task):
        # Accept raw_input choice
        choice = input("1 - Rand int\n2 - Rand string\n3 - Rand short\n4 - Rand float\n6 - Exit\n101 - login\n102 - Disconnect\n103 - Register\n104 - Forget Password\n105 - Create Character\n106 - Chat\n107 - Move\n108 - Power Up\n109 - Power Pick Up\n110 - Health\n122 - Results\n123 - Rankings\n124 - Prizes\n125 - Collistion\n126 - Dead\n127 - Ready\n")
        
        msg = 0
        username = 0
        password = 0
        
        if choice is 1: msg = random.randint(-(2**16), 2**16 - 1)
        elif choice is 2: msg = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(7))
        elif choice is 3: msg = random.randint(0, 2**16 - 1)
        elif choice is 4: msg = 100 * random.random()
        elif choice is 101:
            username = "vatsal"
            password = "sevak"
            self.cManager.sendRequest(choice, username+" "+password)
        elif choice is 102:
            self.cManager.sendRequest(choice, msg)
        elif choice is 103:
            username = "vatsal"
            password = "sevak"
            email = "vatsalsevak@gmail.com"
            self.cManager.sendRequest(choice, username+" "+password+" "+email)
        elif choice is 104:
            username = "vatsal"
            email = "vatsalsevak@gmail.com"
            self.cManager.sendRequest(choice, username+" "+email)
        elif choice is 105:
            username = "vatsal"
            classtype = 1
            self.cManager.sendRequest(choice, username+" "+str(classtype))
        elif choice is 106:
            message = "Hi How are you?"
            self.cManager.sendRequest(choice, message)
        elif choice is 107:
            x = 0
            y = 0
            z = 0
            h = 0
            keys = "keys"
            self.cManager.sendRequest(choice, ""+str(x)+" "+str(y)+" "+str(z)+" "+str(h)+" "+keys)
        elif choice is 108: 
            x = 5
            self.cManager.sendRequest(choice, x)
        elif choice is 109:
            x = 10
            self.cManager.sendRequest(choice, x)
        elif choice is 110:
            username = "vatsal"
            healthChange = 2
            self.cManager.sendRequest(choice, username+" "+str(healthChange))
        elif choice is 122:
            gameId = 1
            self.cManager.sendRequest(choice, gameId)
        elif choice is 123:
            gameId = 1
            self.cManager.sendRequest(choice, gameId)
        elif choice is 124:
            username = "vatsal"
            self.cManager.sendRequest(choice, username)
        elif choice is 125:
            playerId = 1
            damage = 1
            self.cManager.sendRequest(choice, ""+str(playerId)+" "+str(damage))
        elif choice is 126:
            dead = 1
            self.cManager.sendRequest(choice, dead)
        elif choice is 127:
            ready = 1
            self.cManager.sendRequest(choice, ready)
        elif choice is 6: 
            sys.exit()
        else: print "Invalid input"

        #if choice is 101:
        #else:
        #	self.cManager.sendRequest(choice, msg);
        
        return task.again

m = Main()
run()
