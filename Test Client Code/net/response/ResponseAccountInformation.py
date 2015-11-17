from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseAccountInformation(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponseAccountInformation - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_FORGOT_PASSWORD) + '] String Response')
            print_exc()
