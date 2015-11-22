from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseReady(ServerResponse):

    def execute(self, data):

        try:
            self.numOfPlayer = data.getInt32()
            self.username = data.getString()
            self.status = data.getInt32()
            print "\nResponseReady - "
            print self.numOfPlayer
            print self.username
            print self.status

        except:
            self.log('Bad [' + str(Constants.SMSG_READY) + '] String Response')
            print_exc()
