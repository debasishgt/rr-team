from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpPickUp(ServerResponse):

    def execute(self, data):
        try:
            print "\nResponsePowerUpPickUp - "
            self.username = data.getString()
            self.power = data.getInt32()
            print self.username
            print self.power

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_PICKUP) + '] String Response')
            print_exc()
