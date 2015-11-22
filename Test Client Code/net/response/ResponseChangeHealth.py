from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeHealth(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponseChangeHealth - "
            self.username = data.getString()
            self.healthChange = data.getInt32()
            print self.username
            print self.healthChange

        except:
            self.log('Bad [' + str(Constants.SMSG_HEALTH) + '] String Response')
            print_exc()
