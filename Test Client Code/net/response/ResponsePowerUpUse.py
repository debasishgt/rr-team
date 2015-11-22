from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpUse(ServerResponse):

    def execute(self, data):

        try:
            print "\nResponsePowerUpUse - "
            self.username = data.getString()
            self.powerId = data.getInt32()
            print self.username
            print self.powerId

        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_UP) + '] String Response')
            print_exc()
