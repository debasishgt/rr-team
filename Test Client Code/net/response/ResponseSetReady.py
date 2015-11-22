from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSetReady(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponseSetReady - "
            self.username = data.getString()
            print self.username

        except:
            self.log('Bad [' + str(Constants.SMSG_HEALTH) + '] String Response')
            print_exc()
