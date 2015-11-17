from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpUse(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()
            print "ResponsePowerUpUse - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_UP) + '] String Response')
            print_exc()
