from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSetPosition(ServerResponse):

    def execute(self, data):

        try:
            playerCount = data.getInt32()
            
            for x in range(0, playerCount):
                vehicle = self.world.vehiclelist[data.getString()]
                vehicle.setPos(data.getFloat32(), data.getFloat32(), data.getFloat32(), data.getFloat32())

        except:
            self.log('Bad [' + str(Constants.SMSG_SET_POSITION) + '] Set Position Response')
            print_exc()
