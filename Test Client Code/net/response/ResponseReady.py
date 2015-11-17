from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseReady(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseReady - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_READY) + '] String Response')
            print_exc()
