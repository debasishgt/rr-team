from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from Character import Character
import datetime, time


class Dashboard(DirectObject):
    def __init__(self, character, taskMgr):
        self.total_players = 1
        self.rank = 1
        self.main_char = character
        self.speed = "0.0 km/h"
        self.start_time = datetime.datetime.now()
        self.time_elapsed = datetime.timedelta(milliseconds=0)
        # insert total time
        self.game_time = datetime.timedelta(minutes=8) - self.time_elapsed
        # print self.game_time

        # Timer
        self.display_timer = OnscreenText(text=str(self.game_time), style=1, fg=(1, 1, 1, 1), pos=(0, .9), scale=.1)

        # Mini-Map
        OnscreenText(text="mini-map", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, .95), align=TextNode.ALeft,
                     scale=.07)

        # Rank
        self.display_rank = OnscreenText(text=str(self.rank), style=1, fg=(1, 1, 1, 1),
                                         pos=(-.8, .85), align=TextNode.ALeft,
                                         scale=.15)
        OnscreenText(text="/", style=1, fg=(1, 1, 1, 1),
                     pos=(-.7, .85), align=TextNode.ALeft,
                     scale=.18)
        self.display_players = OnscreenText(text=str(self.total_players), style=1, fg=(1, 1, 1, 1),
                                            pos=(-.6, .85), align=TextNode.ALeft,
                                            scale=.15)

        # Ranking
        OnscreenText(text="1st", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, .5), align=TextNode.ALeft,
                     scale=.05)
        OnscreenText(text="2nd", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, .45), align=TextNode.ALeft,
                     scale=.05)
        OnscreenText(text="3rd", style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, .4), align=TextNode.ALeft,
                     scale=.05)

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

        # Display Speed
        self.display_speed = OnscreenText(text=self.speed, style=1, fg=(1, 1, 1, 1),
                                          pos=(1.3, -0.95), align=TextNode.ARight, scale=.07)

        taskMgr.doMethodLater(.1, self.show_speed, 'updateSpeed')
        taskMgr.doMethodLater(.1, self.show_timer, 'updateTimer')
        taskMgr.doMethodLater(.1, self.update_rank, 'updateRank')

    def show_speed(self, task):
        self.speed = str(format(self.main_char.vehicle.getCurrentSpeedKmHour(), '0.2f')) + "km/h"
        # print self.speed

        # Update Speed Display
        self.display_speed.destroy()
        self.display_speed = OnscreenText(text=self.speed, style=3, fg=(1, 1, 1, 1),
                                          pos=(1.3, -0.95), align=TextNode.ARight, scale=.1)
        return task.cont

    def show_timer(self, task):
        self.time_elapsed = datetime.datetime.now() - self.start_time
        game_time = str(datetime.timedelta(minutes=8) - self.time_elapsed)[2:11]
        self.display_timer.destroy()
        self.display_timer = OnscreenText(text=game_time, style=3, fg=(1, 1, 1, 1), pos=(0, .9), scale=.1)
        return task.cont

    # server updates client time in ms
    def force_timer(self, server_time):
        self.time_elapsed = datetime.timedelta(milliseconds=server_time)

    def update_rank(self, task):
        self.display_players.destroy()
        self.display_rank.destroy()

        # Rank
        self.display_rank = OnscreenText(text=str(self.rank), style=1, fg=(1, 1, 1, 1),
                                         pos=(-.8, .85), align=TextNode.ALeft,
                                         scale=.15)
        self.display_players = OnscreenText(text=str(self.total_players), style=1, fg=(1, 1, 1, 1),
                                            pos=(-.6, .85), align=TextNode.ALeft,
                                            scale=.15)
        return task.cont
