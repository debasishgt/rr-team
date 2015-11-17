from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeHealth(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseChangeHealth - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_HEALTH) + '] String Response')
            print_exc()
