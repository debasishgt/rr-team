from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseReady(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            print "\nResponseReady - "
            print self.username

        except:
            self.log('Bad [' + str(Constants.SMSG_READY) + '] String Response')
            print_exc()
