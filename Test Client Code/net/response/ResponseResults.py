from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseResults(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponseResults - "
            self.place = data.getInt32()
            self.numOfPlayers = data.getInt32()
            print self.place
            print self.numOfPlayers
        except:
            self.log('Bad [' + str(Constants.SMSG_RESULTS) + '] String Response')
            print_exc()
