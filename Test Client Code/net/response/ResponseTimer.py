from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseTimer(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseTimer - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_TIMER) + '] String Response')
            print_exc()
