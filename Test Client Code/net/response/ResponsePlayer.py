from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePlayer(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponsePlayer - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_PLAYER) + '] String Response')
            print_exc()
