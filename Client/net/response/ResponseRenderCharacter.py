from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
# from finalhw1 import Character
from Vehicle import Vehicle


class ResponseRenderCharacter(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.CarType = data.getInt32()
            self.CarPaint = data.getInt32()
            self.CarTires = data.getInt32()

            char = Vehicle(self.world,self.world.bulletWorld, (0,0,0,0,0,0), self.username)

            self.world.vehiclelist.append(char)

            print "ResponseRenderCharacter - ", self.username

        except:
            self.log('Bad [' + str(Constants.SMSG_RENDER_CHARACTER) + '] Render Character Response')
            print_exc()
