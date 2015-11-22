from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogout(ServerResponse):

    def execute(self, data):

        try:
            print "ResponseLogout - "

        except:
            self.log('Bad [' + str(Constants.SMSG_DISCONNECT) + '] String Response')
            print_exc()
