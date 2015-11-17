from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpPickUp(ServerResponse):

    def execute(self, data):
        try:
            self.msg = data.getString()
            print "ResponsePowerUpPickUp - ", self.msg

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_PICKUP) + '] String Response')
            print_exc()
