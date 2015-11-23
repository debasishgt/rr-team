
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText,TextNode
from direct.task import Task

countDownStart = 6

class LoadingScreen:
    def __init__(self):
        self.imageObject = OnscreenImage(image = 'images/loading.jpg', pos = (0, 0, 0))
        self.imageObject.reparentTo(render2d)
        base.graphicsEngine.renderFrame()
        base.graphicsEngine.renderFrame()

    def finish(self):
        self.imageObject.destroy()
        self.countDownText = OnscreenText(text=str(countDownStart), style=1, fg=(1,1,1,1),
                pos=(0.01, 0.1), align = TextNode.ACenter, scale = .2, mayChange = 1)
        taskMgr.add(self.countDown,"countDownTask")

    def countDown(self,task):
        timeLeft = "%01d" % (countDownStart - task.time)
        if (countDownStart - task.time) > 1:
            self.countDownText.setText(timeLeft)
            return task.cont
        elif 1 > (countDownStart - task.time) > 0:
            self.countDownText.setText("GO!")
            return task.cont
        else:
            self.canMove = True
            self.countDownText.destroy()
            return task.done

