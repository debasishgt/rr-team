from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseAuth(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getUint16()

            print "ResponseAuth - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] String Response')
            print_exc()
