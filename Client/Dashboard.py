from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode


class Dashboard(DirectObject):
    def __init__(self):
        # Speed
        OnscreenText(text="Speed", style=1, fg=(1, 1, 1, 1),
                     pos=(1.3, -0.95), align=TextNode.ARight, scale=.07)
        # Timer
        OnscreenText(text="Timer", style=1, fg=(1, 1, 1, 1), pos=(0, .95), scale=.07)

        # Mini-Map
        OnscreenText(text="mini-map", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, .95), align=TextNode.ALeft,
                     scale=.07)

        # Rank
        OnscreenText(text="2", style=1, fg=(1, 1, 1, 1),
                     pos=(-.95, .85), align=TextNode.ALeft,
                     scale=.15)
        OnscreenText(text="/", style=1, fg=(1, 1, 1, 1),
                     pos=(-.85, .85), align=TextNode.ALeft,
                     scale=.18)
        OnscreenText(text="5", style=1, fg=(1, 1, 1, 1),
                     pos=(-.75, .85), align=TextNode.ALeft,
                     scale=.15)

        # Powerups
        OnscreenText(text="1", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, -.95), align=TextNode.ALeft,
                     scale=.07)
        OnscreenText(text="2", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.2, -.95), align=TextNode.ALeft,
                     scale=.07)
        OnscreenText(text="3", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.1, -.95), align=TextNode.ALeft,
                     scale=.07)
