from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseTime(ServerResponse):

    def execute(self, data):

        try:
            self.type = data.getInt32()
            self.time = data.getLong32()
            print "\nResponseTime - "
            print self.type
            print self.time

        except:
            self.log('Bad [' + str(Constants.SMSG_TIMER) + '] String Response')
            print_exc()
