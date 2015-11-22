from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseReady(ServerResponse):

    def execute(self, data):

        try:
            self.playerCount = data.getInt32()
            self.readyPlayers = {data.getString() : data.getInt32()}

            # for x in range(0, self.playerCount-1)
            #     self.readyPlayers[data.getString()] = data.getInt32()

            print "ResponseReady - ",self.playerCount

        except:
            self.log('Bad [' + str(Constants.SMSG_READY) + '] Ready Response')
            print_exc()
