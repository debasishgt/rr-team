import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject

from pandac.PandaModules import TextNode

#add some text
bk_text = "This is my Demo"
textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95),
scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)

#callback function to set  text
def setText(arg):
    bk_text = str(arg)
    textObject.setText(bk_text)
#end setText




#clear the text
def clearText():
    entry.enterText('')
#end clearText

parentFrame = True

def toggleParent():
    global parentFrame
    if parentFrame:
        setText('Parented to World')
        entry.reparentTo(render2d)
        label.reparentTo(render2d)
        parentFrame = False
    else:
        setText('Parented to Frame')
        entry.reparentTo(frame)
        label.reparentTo(frame)
        parentFrame = True
    #end if
#end toggleParent


frame = DirectFrame(frameSize = (-.5,.5,-.5,.5), frameColor=(.3,.2,.1,1))
#frame.reparentTo(render2d)

entry = DirectEntry( pos = (-.5,0,-.5), text = "" ,scale=.05,command=setText,
initialText="Type Something", numLines = 2,focus=1,focusInCommand=clearText)

entry.reparentTo(frame)



label = DirectLabel(parent =frame,text="this is a label", scale = 0.05,pos = (-.5,0,.8))


input = DirectObject()
input.accept('a', toggleParent)

run()