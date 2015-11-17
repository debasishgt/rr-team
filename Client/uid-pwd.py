__author__ = 'debasish'

from pandac.PandaModules import *
from direct.gui.DirectGui import *
import direct.directbase.DirectStart
from random import random
from net.ConnectionManager import ConnectionManager
import Main
import time
from common.Constants import Constants

class DirectButtonHandler:
    def __init__(self, type, zPos, parentObj=None):
        self.parentObj = parentObj
        if type == "Register" or type == "Login":
            self.asset = DirectButton(text=type, scale=.1, pos=(0,0, zPos), command=self.registeruser)
        elif type == "Select Character":
            self.asset = DirectButton(text=type, scale=.1, pos=(0,0, zPos), command=self.getCharChoice)

    def getAsset(self):
        return self.asset
    def setUidPwd(self, uid, pwd):
        self.de = uid
        self.de2 = pwd
    def setCharHandle(self, inHandle):
        self.charHandle = inHandle
    def registeruser(self):
        username = self.de.getAsset().get()
        password = self.de2.getAsset().get()
        #print username, password
        self.parentObj.connectionManager.sendRequest(Constants.CMSG_AUTH, [username, password])
        while self.parentObj.loginState == -1:
            time.sleep(5)
            print "Waiting"
            pass

        if self.parentObj.loginState == 1:
            self.parentObj.worldManager.runWorld()

    def getCharChoice(self):
        print "GetCharChoice"
        print self.charHandle.getChoice()


class DirectEntryHandler:
    def __init__(self, zPos, isObscured):
        self.asset = DirectEntry(initialText="", scale=.1, width=11, numLines=1, obscured=isObscured, pos=Vec3(-.55,0,zPos), command=self.setasset)
        # DirectEntry(initialText="password",scale=.4,width=10,numLines=1, command=setpassword)

    def setasset(self):
        print self.asset.get()

    def getAsset(self):
        return self.asset


class DirectRadioButtonHandler:
    def __init__(self):
        # Add button
        self.v = [1]
        self.buttons = [
            DirectRadioButton(text = 'Ralph', indicatorValue=0, variable=self.v, value=[1], scale=0.07, pos=(-0.3,0,0.2), command=self.setText),
            DirectRadioButton(text = 'Panda', indicatorValue=0, variable=self.v, value=[2], scale=0.07, pos=(0.1,0,0.2), command=self.setText),
            DirectRadioButton(text = 'Car', indicatorValue=0, variable=self.v, value=[3], scale=0.07, pos=(0.5,0,0.2), command=self.setText)
        ]
        for self.button in self.buttons:
            self.button.setOthers(self.buttons)

    def setText(self, status=None):
        self.bk_text = "%s"%self.v
        #print self.bk_text

    def getChoice(self):
        return self.bk_text

    def hide(self):
        for self.button in self.buttons:
            self.button.hide()

class UserGUIHandler:
    def __init__(self):
        print "UserGUIHandler Init"
        self.loginState = -1
        self.worldManager = Main.WorldManager()
        self.world = self.worldManager.w
        self.connectionManager = ConnectionManager(self)
        self.world.setConnectionManager(self.connectionManager)
        self.connectionManager.startConnection()

    def register(self):

        self.createFrame(-0.7)

        self.dl = DirectLabel(text="Welcome To Game Registration Page", pos=Vec3(0,0,0.8),frameColor=(.5,.5,.5,.5), scale=0.11)

        self.dl2 = DirectLabel(text="USERNAME", pos=Vec3(0,0,0.4),frameColor=(.5,.5,.5,.5), scale=0.1)
        self.uid = DirectEntryHandler(0.2, 0)

        self.dl3 = DirectLabel(text="PASSWORD", pos=Vec3(0,0,0.0),frameColor=(.5,.5,.5,.5), scale=0.1)
        self.pwd = DirectEntryHandler(-0.2, 1)

        self.reg = DirectButtonHandler("Register", -0.4)
        self.reg.setUidPwd(self.uid, self.pwd)

    def setLogin(self, state):
        self.loginState = state

    def createFrame(self, inLength):
        self.frame = DirectFrame(relief = DGG.RAISED, borderWidth = (0.05,0.05), frameSize = (-1,1,-1,1), frameColor=(.3,.2,.1,.5))
        self.buttonFrame = DirectFrame(parent=self.frame, relief=DGG.RAISED, borderWidth=(0.05,0.05), frameSize=(-.7,.7,inLength,.7), frameColor=(.5,.5,.5,.5), pos=(-0,0,0))

    def login(self):
        self.createFrame(-0.7)

        self.dl = DirectLabel(text="Enter Your Personal Details To Login", pos=Vec3(0,0,0.8),frameColor=(.5,.5,.5,.5), scale=0.11)

        self.dl2 = DirectLabel(text="USERNAME", pos=Vec3(0,0,0.4),frameColor=(.5,.5,.5,.5), scale=0.1)
        self.uid = DirectEntryHandler(0.2, 0)

        self.dl3 = DirectLabel(text="PASSWORD", pos=Vec3(0,0,0.0),frameColor=(.5,.5,.5,.5), scale=0.1)
        self.pwd = DirectEntryHandler(-0.2, 1)

        self.reg = DirectButtonHandler("Login", -0.4, self)
        self.reg.setUidPwd(self.uid, self.pwd)

    def characterSelect(self):
        self.createFrame(-0.3)

        self.directRadioButtonHandler = DirectRadioButtonHandler()
        self.lbl = DirectLabel(parent = self.buttonFrame, text="Choose Character", pos=Vec3(0,0,0.4),frameColor=(.5,.5,.5,.5), scale=0.1)
        self.submit = DirectButton(parent = self.buttonFrame, text = ("Submit", "Submit", "Submit", "disabled"),scale=.1, pos=Vec3(0,0,0), command=self.buttonAction)

        #self.runWorld = finalhw1.RunWorld()

    def buttonAction(self):
        self.characterChoice = self.directRadioButtonHandler.getChoice()
        print self.characterChoice
        self.clearCharacterSelectView()

    def clearCharacterSelectView(self):
        self.buttonFrame.hide()
        self.submit.hide()
        self.lbl.hide()
        self.directRadioButtonHandler.hide()

    def clearRegisterView(self):
        print ""


    def setText(self, status=None):
        if(self.v):
            print "0"
        else:
            print self.v
        bk_text = "CurrentValue : %s"%self.v
        print bk_text
        #textObject.setText(bk_text)


if __name__ == '__main__':

    # Class for handling GUI
    userGUIHandler = UserGUIHandler()

    #Login Page
    userGUIHandler.login()

    #Registration Page
    #userGUIHandler.register()

    #Select Character UI Page
    #userGUIHandler.characterSelect()
    run()



